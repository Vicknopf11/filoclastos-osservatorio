# Schema — assets/data/pensioni.json

Aggiornato il 2026-07-23. Struttura del file dati per la pagina `/pensioni/`.

## Stato dei blocchi

| Blocco | Stato | Fonte |
|---|---|---|
| `totali` (IVS/GIAS) | ⏳ da fare | Osservatorio INPS + RGS |
| `per_gestione` | ⏳ da fare | Osservatorio INPS, filtro gestione |
| `per_tipologia` | ✅ popolato (2026-07-23) | Osservatorio INPS, "Complesso delle pensioni vigenti" |
| `per_regione` | ✅ popolato (2026-07-23) | Osservatorio INPS, "...per residenza del titolare" |
| `per_genere` | ⏳ da fare | Osservatorio INPS |
| `per_eta` | ✅ popolato (2026-07-23) | Osservatorio INPS, "Complesso delle pensioni vigenti" |
| `distribuzione_importi` | ⏳ da fare | Osservatorio INPS, tavola per fasce di importo |
| `serie_storiche` | ⏳ da fare | Bilancio Sociale INPS + ISTAT |
| `rapporto_contributi_prestazioni` | ⏳ da fare | INPS Bilancio + RGS Conto Annuale |

## Modifica rispetto allo schema originale (2026-07-09)

`per_tipologia` è stato esteso da **4 a 5 voci**. La tavola INPS reale distingue
"Pensioni/assegni sociali" da "Invalidi civili" — entrambe assistenziali ma di
natura diversa (la prima legata a età e condizione economica, la seconda al
riconoscimento di un'invalidità civile). Il vecchio schema le accorpava in una
sola voce "assistenziali"; si è preferito mantenerle separate per fedeltà al
dato piuttosto che perdere questa distinzione.

```json
"per_tipologia": [
  { "tipo": "vecchiaia_anticipata", "label": "Vecchiaia/Anticipata", "numero_pensioni": null, "importo_medio_mensile_eur": null },
  { "tipo": "invalidita", "label": "Invalidità", "numero_pensioni": null, "importo_medio_mensile_eur": null },
  { "tipo": "superstiti", "label": "Superstiti", "numero_pensioni": null, "importo_medio_mensile_eur": null },
  { "tipo": "assegni_sociali", "label": "Assegno/pensione sociale", "numero_pensioni": null, "importo_medio_mensile_eur": null },
  { "tipo": "invalidi_civili", "label": "Invalidi civili", "numero_pensioni": null, "importo_medio_mensile_eur": null }
]
```

## per_eta — nota sulle fasce

Le 4 fasce larghe (`under_65`, `65_74`, `75_84`, `85_plus`) sono ottenute
aggregando le 14 classi d'età originali della tavola INPS (`Fino a 14`, `15-19`,
..., `90 ed oltre`). L'importo medio di ciascuna fascia larga è una **media
ponderata** sul numero di pensioni delle sotto-fasce che la compongono, non una
media semplice.

## Fonti — tabella completa

| Blocco | Fonte primaria | Note |
|---|---|---|
| `totali` | Osservatorio INPS, tavola "Complesso delle gestioni" | Il rapporto pensioni/pensionati va calcolato (una persona può avere più trattamenti) |
| `per_gestione` | Osservatorio INPS, filtro per gestione | FPLD = privato, GDP = pubblico ex INPDAP |
| `per_tipologia` | Osservatorio INPS, tavola per categoria di pensione | Vecchiaia/anzianità, invalidità, superstiti, assegni sociali, invalidi civili (5 voci, vedi nota sopra) |
| `per_regione` | Osservatorio INPS, "Complesso delle pensioni vigenti per residenza del titolare" | Territorio per residenza disponibile solo in questa tavola specifica |
| `per_genere` | Osservatorio INPS | Quasi sempre disponibile incrociato con gestione/tipologia |
| `per_eta` | Osservatorio INPS, "Complesso delle pensioni vigenti", classe di età | Età calcolata al 1° gennaio dell'anno di riferimento (non età al pensionamento) |
| `distribuzione_importi` | Osservatorio INPS, tavola per fasce di importo mensile | Serve l'importo medio *dentro* la fascia, non solo la soglia |
| `serie_storiche` | Bilancio Sociale INPS + ISTAT conto protezione sociale | Per i trend, coerente con l'approccio storico di `spesa-pubblica` |
| `rapporto_contributi_prestazioni` | INPS Bilancio + RGS Conto Annuale | Il più complesso: due fonti diverse, possibili disallineamenti di anno di riferimento |

## Vincolo noto: segreto statistico

L'incrocio diretto **regione × classe di età** è bloccato dall'Osservatorio INPS
per motivi di segreto statistico (art. 4 delle regole deontologiche). Per il
coefficiente di pensionamento standardizzato per regione (pubblicato in
`spesa-pubblica/index.md`, Sezione 08) è stata usata una standardizzazione
indiretta che aggira questo vincolo. Lo stesso vincolo si applicherà a qualsiasi
futuro tentativo di incrociare `per_regione` con `per_eta` direttamente da
questa fonte.
