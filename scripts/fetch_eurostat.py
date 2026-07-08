"""
Scarica dati di finanza pubblica da Eurostat e li scrive in un JSON statico,
datato e con fonte dichiarata — coerente con la nota metodologica
dell'Osservatorio ("dati statici, aggiornati periodicamente, mai generati
al momento").

Porta in Python la stessa logica già validata nel prototipo ItaliaSpende
(client-side JS): stessi dataset, stessi codici COFOG, stesso parsing
JSON-stat 2.0. Girare via GitHub Actions con rete propria, non nel
browser di chi visita il sito.
"""
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

EUROSTAT_BASE = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/"
TIMEOUT_S = 20
YEAR = "2023"

GEO_TO_LABEL = {
    "IT": "🇮🇹 Italia", "FR": "🇫🇷 Francia", "AT": "🇦🇹 Austria", "BE": "🇧🇪 Belgio",
    "FI": "🇫🇮 Finlandia", "DK": "🇩🇰 Danimarca", "SE": "🇸🇪 Svezia", "PT": "🇵🇹 Portogallo",
    "DE": "🇩🇪 Germania", "NL": "🇳🇱 Olanda", "ES": "🇪🇸 Spagna", "EL": "🇬🇷 Grecia",
    "IE": "🇮🇪 Irlanda",
}
GEO_CODES = list(GEO_TO_LABEL.keys())
GEO_QS = "&".join(f"geo={g}" for g in GEO_CODES)

COFOG_CODES = {
    "sanita":     {"dataset": "gov_10a_exp", "dim": "cofog99", "code": "GF07", "na_item": "TE"},
    "istruzione": {"dataset": "gov_10a_exp", "dim": "cofog99", "code": "GF09", "na_item": "TE"},
    "pensioni":   {"dataset": "gov_10a_exp", "dim": "cofog99", "code": "GF10", "na_item": "TE"},
    "interessi":  {"dataset": "gov_10a_main", "dim": None, "code": None, "na_item": "D41PAY"},
}


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "filoclastos-osservatorio-bot/1.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT_S) as r:
        return json.loads(r.read().decode())


def parse_single_dim(data: dict) -> dict:
    """Estrae {geoCode: valore} da una risposta JSON-stat 2.0 con 'geo' come
    unica dimensione libera. Stesso algoritmo del parser JS originale."""
    geo_dim = data["dimension"]["geo"]
    geo_index = geo_dim["category"]["index"]
    values = data["value"]
    result = {}
    for geo_code, idx in geo_index.items():
        v = values[idx] if isinstance(values, list) else values.get(str(idx))
        if v is not None:
            result[geo_code] = v
    return result


def plausible(v, max_v) -> bool:
    try:
        n = float(v)
        return 0 < n < max_v
    except (TypeError, ValueError):
        return False


def load_total_expenditure() -> dict:
    url = f"{EUROSTAT_BASE}gov_10a_main?format=JSON&unit=PC_GDP&na_item=TE&sector=S13&{GEO_QS}&time={YEAR}"
    return parse_single_dim(fetch_json(url))


def load_debt() -> dict:
    url = f"{EUROSTAT_BASE}gov_10dd_edpt1?format=JSON&unit=PC_GDP&na_item=GD&sector=S13&{GEO_QS}&time={YEAR}"
    return parse_single_dim(fetch_json(url))


def load_cofog(key: str) -> dict:
    spec = COFOG_CODES[key]
    if spec["dim"]:
        url = (f"{EUROSTAT_BASE}{spec['dataset']}?format=JSON&unit=PC_GDP&sector=S13"
               f"&{spec['dim']}={spec['code']}&na_item={spec['na_item']}&{GEO_QS}&time={YEAR}")
    else:
        url = (f"{EUROSTAT_BASE}{spec['dataset']}?format=JSON&unit=PC_GDP&sector=S13"
               f"&na_item={spec['na_item']}&{GEO_QS}&time={YEAR}")
    return parse_single_dim(fetch_json(url))


def main():
    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "year": YEAR,
        "source": "Eurostat — gov_10a_main, gov_10a_exp, gov_10dd_edpt1 (settore S13)",
        "source_url": "https://ec.europa.eu/eurostat/web/government-finance-statistics",
        "totale": {},
        "debito": {},
        "sanita": {},
        "istruzione": {},
        "pensioni": {},
        "interessi": {},
        "ok": [],
        "errori": [],
    }

    jobs = [
        ("totale", load_total_expenditure, 100),
        ("debito", load_debt, 250),
    ]
    for key in COFOG_CODES:
        jobs.append((key, lambda k=key: load_cofog(k), 40))

    for key, loader, max_v in jobs:
        try:
            values = loader()
            filtered = {g: v for g, v in values.items() if plausible(v, max_v)}
            output[key] = filtered
            if len(filtered) >= 5:
                output["ok"].append(key)
            else:
                output["errori"].append(f"{key}: solo {len(filtered)} paesi plausibili")
        except (urllib.error.URLError, KeyError, ValueError) as e:
            output["errori"].append(f"{key}: {e}")
            print(f"Errore su {key}: {e}")

    out_path = Path(__file__).resolve().parent.parent / "assets" / "data" / "eurostat.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Scritto {out_path}")
    print(f"Categorie aggiornate con successo: {output['ok']}")
    if output["errori"]:
        print(f"Categorie non aggiornate (restano i dati precedenti nel sito): {output['errori']}")


if __name__ == "__main__":
    main()
