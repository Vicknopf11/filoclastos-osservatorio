#!/usr/bin/env python3
"""
Calcola il coefficiente di pensionamento standardizzato per regione,
usando standardizzazione indiretta (stesso principio dello SMR
epidemiologico), per aggirare il blocco privacy INPS sull'incrocio
diretto regione x classe di età.

Fonti:
- inps_regioni.csv: pensioni vigenti (stock) per regione, Totale, INPS
- inps_eta_nazionale.csv: pensioni vigenti per classe di età, Italia, INPS
- Popolazione_residente*.csv: popolazione per singolo anno di età, ISTAT,
  una per regione (20 file)
- mappa_regioni.py: associazione file -> nome regione
"""

import csv
import re
from mappa_regioni import mappa_file_regione

# Fasce d'età usate da INPS in inps_eta_nazionale.csv
FASCE_INPS = [
    ("Fino a 14", 0, 14),
    ("15-19", 15, 19),
    ("20-29", 20, 29),
    ("30-39", 30, 39),
    ("40-49", 40, 49),
    ("50-54", 50, 54),
    ("55-59", 55, 59),
    ("60-64", 60, 64),
    ("65-69", 65, 69),
    ("70-74", 70, 74),
    ("75-79", 75, 79),
    ("80-84", 80, 84),
    ("85-89", 85, 89),
    ("90 ed oltre", 90, 999),
]


def pulisci_numero(s: str) -> float:
    s = s.strip().strip('"').strip()
    if s in ("-", "", ".."):
        return 0.0
    s = s.replace(".", "").replace(",", ".")
    return float(s)


def leggi_pensioni_nazionali_per_eta(path: str) -> dict:
    """Legge il numero di pensioni nazionali per fascia d'età (riga Totale)."""
    with open(path, encoding="utf-8", newline="") as f:
        testo = f.read()
    righe = testo.splitlines()
    riga_totale = None
    for r in righe:
        if r.startswith('"Totale";'):
            riga_totale = r
            break
    if riga_totale is None:
        raise ValueError("Riga Totale non trovata in " + path)

    campi = riga_totale.split(";")
    campi = [c.strip('"').strip() for c in campi]
    # Struttura: "Totale";"";  poi per ciascuna delle 14 fasce: NumeroPensioni;ImportoMedio
    # poi Totale generale: NumeroPensioni;ImportoMedio
    valori = campi[2:]  # salta "Totale" e il campo vuoto
    pensioni_per_fascia = {}
    for i, (nome_fascia, _, _) in enumerate(FASCE_INPS):
        num_pensioni = pulisci_numero(valori[i * 2])
        pensioni_per_fascia[nome_fascia] = num_pensioni
    return pensioni_per_fascia


def leggi_pensioni_regioni(path: str) -> dict:
    """Legge il numero di pensioni Totale (tutte le categorie) per regione."""
    with open(path, encoding="utf-8", newline="") as f:
        testo = f.read()
    righe = testo.splitlines()

    pensioni_regione = {}
    regioni_note = set(mappa_file_regione.values()) | {
        "Trentino -Alto-Adige", "Friuli -Venezia Giulia", "Emilia -Romagna",
        "Valle d'Aosta/Vallee d'Aoste",
    }

    for r in righe:
        if not r.strip():
            continue
        campi = r.split(";")
        campi = [c.strip('"').strip() for c in campi]
        if len(campi) < 3:
            continue
        area = campi[0]
        regione_raw = campi[1]

        nome_pulito = regione_raw.lstrip("+-").strip()
        nome_pulito = re.sub(r"\s+", " ", nome_pulito)

        # Normalizza nomi con variazioni di spaziatura/trattini INPS
        normalizzazioni = {
            "Trentino -Alto-Adige": "Trentino-Alto Adige",
            "Friuli -Venezia Giulia": "Friuli-Venezia Giulia",
            "Emilia -Romagna": "Emilia-Romagna",
            "Valle d'Aosta/Vallee d'Aoste": "Valle d'Aosta",
        }
        nome_pulito = normalizzazioni.get(nome_pulito, nome_pulito)

        if nome_pulito not in mappa_file_regione.values():
            continue
        if regione_raw.strip() == "Totale":
            continue

        # Gli ultimi 4 campi della riga sono Numero Pensioni, Importo medio,
        # Importo complessivo, Età media per la categoria "Totale"
        try:
            numero_pensioni_totale = pulisci_numero(campi[-4])
            eta_media_totale = pulisci_numero(campi[-1])
        except (IndexError, ValueError):
            continue

        pensioni_regione[nome_pulito] = {
            "numero_pensioni": numero_pensioni_totale,
            "eta_media": eta_media_totale,
        }

    return pensioni_regione


def leggi_popolazione_per_fascia(path: str) -> dict:
    """Legge popolazione per singolo anno d'età e raggruppa nelle fasce INPS."""
    pop_per_fascia = {nome: 0.0 for nome, _, _ in FASCE_INPS}
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # salta header
        for row in reader:
            eta_str = row[0].strip('"').strip()
            if eta_str == "Totale":
                continue
            if eta_str == "100 e oltre":
                eta = 100
            else:
                eta = int(eta_str)
            totale = pulisci_numero(row[3])
            for nome_fascia, eta_min, eta_max in FASCE_INPS:
                if eta_min <= eta <= eta_max:
                    pop_per_fascia[nome_fascia] += totale
                    break
    return pop_per_fascia


def main():
    cartella = "."

    print("→ Leggo pensioni nazionali per fascia d'età...")
    pensioni_naz_per_fascia = leggi_pensioni_nazionali_per_eta(
        f"{cartella}/inps_eta_nazionale.csv"
    )
    totale_pensioni_naz = sum(pensioni_naz_per_fascia.values())
    print(f"  Totale pensioni nazionali (somma fasce): {totale_pensioni_naz:,.0f}")

    print("→ Leggo pensioni per regione (stock, Totale categorie)...")
    pensioni_regione = leggi_pensioni_regioni(f"{cartella}/inps_regioni.csv")
    print(f"  {len(pensioni_regione)} regioni lette")

    print("→ Leggo popolazione per regione e fascia d'età (ISTAT)...")
    pop_per_regione_fascia = {}
    pop_naz_per_fascia = {nome: 0.0 for nome, _, _ in FASCE_INPS}
    for nome_file, nome_regione in mappa_file_regione.items():
        pop_fascia = leggi_popolazione_per_fascia(f"{cartella}/{nome_file}")
        pop_per_regione_fascia[nome_regione] = pop_fascia
        for nome_fascia in pop_naz_per_fascia:
            pop_naz_per_fascia[nome_fascia] += pop_fascia[nome_fascia]

    pop_naz_totale = sum(pop_naz_per_fascia.values())
    print(f"  Popolazione nazionale totale (somma regioni lette): {pop_naz_totale:,.0f}")

    # Tasso nazionale età-specifico: pensioni_fascia / popolazione_fascia
    tasso_naz_per_fascia = {}
    for nome_fascia, _, _ in FASCE_INPS:
        p = pensioni_naz_per_fascia[nome_fascia]
        pop = pop_naz_per_fascia[nome_fascia]
        tasso_naz_per_fascia[nome_fascia] = (p / pop) if pop > 0 else 0.0

    tasso_naz_grezzo = totale_pensioni_naz / pop_naz_totale

    print("\n→ Calcolo pensioni attese e coefficiente standardizzato per regione:\n")

    risultati = []
    for nome_regione in sorted(mappa_file_regione.values()):
        pop_fascia = pop_per_regione_fascia[nome_regione]
        pensioni_attese = sum(
            tasso_naz_per_fascia[nome_fascia] * pop_fascia[nome_fascia]
            for nome_fascia, _, _ in FASCE_INPS
        )
        dati_inps = pensioni_regione.get(nome_regione)
        if dati_inps is None:
            print(f"  ⚠ {nome_regione}: non trovata nel file INPS regionale, salto")
            continue
        pensioni_osservate = dati_inps["numero_pensioni"]
        pop_regione_totale = sum(pop_fascia.values())

        # Coefficiente standardizzato: (osservate / attese) * tasso grezzo nazionale
        # espresso per 1.000 residenti
        if pensioni_attese > 0:
            rapporto_oe = pensioni_osservate / pensioni_attese
            coefficiente_standardizzato = rapporto_oe * tasso_naz_grezzo * 1000
        else:
            coefficiente_standardizzato = None

        tasso_grezzo_regione = (
            (pensioni_osservate / pop_regione_totale * 1000)
            if pop_regione_totale > 0
            else None
        )

        risultati.append({
            "regione": nome_regione,
            "pensioni_osservate": pensioni_osservate,
            "pensioni_attese": pensioni_attese,
            "popolazione": pop_regione_totale,
            "eta_media": dati_inps["eta_media"],
            "tasso_grezzo_per_1000": tasso_grezzo_regione,
            "coefficiente_standardizzato_per_1000": coefficiente_standardizzato,
        })

    risultati.sort(key=lambda r: r["coefficiente_standardizzato_per_1000"] or 0)

    print(f"{'Regione':<22} {'Grezzo/1000':>12} {'Standard./1000':>15} {'Età media':>10}")
    print("-" * 65)
    for r in risultati:
        print(
            f"{r['regione']:<22} "
            f"{r['tasso_grezzo_per_1000']:>12.1f} "
            f"{r['coefficiente_standardizzato_per_1000']:>15.1f} "
            f"{r['eta_media']:>10.1f}"
        )

    print(f"\nTasso grezzo nazionale di riferimento: {tasso_naz_grezzo*1000:.1f} per 1.000 residenti")

    # Salva anche in CSV per uso successivo
    with open(f"{cartella}/coefficiente_pensionamento_regioni.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "regione", "pensioni_osservate", "pensioni_attese", "popolazione",
            "eta_media", "tasso_grezzo_per_1000", "coefficiente_standardizzato_per_1000"
        ])
        for r in risultati:
            writer.writerow([
                r["regione"],
                int(r["pensioni_osservate"]),
                round(r["pensioni_attese"], 1),
                int(r["popolazione"]),
                r["eta_media"],
                round(r["tasso_grezzo_per_1000"], 2),
                round(r["coefficiente_standardizzato_per_1000"], 2),
            ])
    print(f"\n✓ Risultati salvati in coefficiente_pensionamento_regioni.csv")


if __name__ == "__main__":
    main()
