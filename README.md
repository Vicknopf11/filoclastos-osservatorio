# Filoclastos

Scheletro Jekyll per filoclastos.it — osservatorio civico su spesa pubblica,
proprietà societaria, carriere politiche e norme.

## Struttura

```
index.md                    — home, elenco dei quattro Titoli
spesa-pubblica/index.md     — Titolo I
proprieta-societarie/index.md — Titolo II
persone/index.md            — Titolo III
norme/index.md              — Titolo IV
metodologia/index.md        — nota metodologica (voce di nav fissa)
changelog/index.md          — cronologia modifiche
_layouts/default.html       — layout unico (masthead, nav, footer)
_includes/nav.html          — barra di navigazione, generata da _config.yml
_includes/timbro.html       — il sigillo SVG, elemento distintivo del sito
assets/css/main.css         — tutto lo stile, a token (colori/tipografia in :root)
_config.yml                 — titolo, tagline, e l'elenco dei quattro Titoli
```

Per aggiungere un nuovo strumento dentro un Titolo esistente: crea una
pagina dentro la cartella corrispondente (es.
`proprieta-societarie/mps-dossier.md`) con `layout: default` in cima, e
collegala dalla pagina indice del Titolo. La struttura di alto livello
(home, quattro Titoli, metodologia, changelog) resta stabile.

## Nota — questo è un sottodominio del portale

Questo repository ospita solo l'Osservatorio civico, su
`osservatorio.filoclastos.it`. Il dominio principale `filoclastos.it` è
un repository separato (il portale, con i link a tutti i progetti) — vedi
`filoclastos-portal/`.

## Pubblicazione su GitHub Pages

1. Crea un nuovo repository su GitHub (pubblico, altrimenti GitHub Pages
   richiede un piano a pagamento), chiamato `filoclastos-osservatorio`.
2. Da questa cartella:

   ```bash
   cd filoclastos-osservatorio
   git init
   git add .
   git commit -m "Struttura iniziale del sito"
   git branch -M main
   git remote add origin https://github.com/Vicknopf11/filoclastos-osservatorio.git
   git push -u origin main
   ```

3. Su GitHub: **Settings → Pages**
   - Source: `Deploy from a branch`
   - Branch: `main`, cartella `/ (root)`
   - Salva. Dopo qualche minuto il sito sarà live su
     `https://Vicknopf11.github.io/filoclastos-osservatorio/` — è
     normale, arriva prima il dominio di GitHub, poi colleghiamo quello vero.
   - Nello stesso pannello, sotto **Custom domain**, inserisci
     `osservatorio.filoclastos.it` e salva. GitHub creerà/verificherà il
     file `CNAME` già presente in questo repository.
   - Spunta **Enforce HTTPS** (potrebbe richiedere qualche minuto per
     attivarsi dopo la verifica del DNS).

## DNS su Aruba

Nel pannello Aruba, sezione **Gestione DNS** del dominio `filoclastos.it`,
aggiungi un record CNAME per il sottodominio:

```
CNAME    osservatorio    Vicknopf11.github.io.
```

(Il punto finale dopo `.github.io.` va lasciato se il pannello Aruba lo
richiede in formato FQDN.)

I record per il dominio nudo (`filoclastos.it`) e per `www` riguardano
il repository del portale (`filoclastos-portal`), non questo.

La propagazione DNS può richiedere da pochi minuti fino a qualche ora.
Puoi verificarla con `dig filoclastos.it +noall +answer` da terminale, o
controllando lo stato nel pannello Pages di GitHub, che segnala se il DNS
è verificato correttamente.

## Sviluppo locale (opzionale)

Se vuoi vedere le modifiche prima di pubblicarle:

```bash
bundle install
bundle exec jekyll serve
```

Il sito sarà disponibile su `http://localhost:4000`.
