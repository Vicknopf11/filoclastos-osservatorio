---
layout: default
title: "Pensioni — dettaglio per regione, età e tipologia"
description: "Approfondimento sul sistema pensionistico italiano: numero di pensioni e importo medio per regione, fascia d'età e tipologia di prestazione, con fonti INPS sempre citate."
---
<div class="prose">
<span class="prose__kicker">Approfondimento</span>
<h1>Pensioni — dettaglio</h1>
<p>
  Questa pagina approfondisce il sistema pensionistico italiano oltre la panoramica
  già presente in <a href="{{ '/spesa-pubblica/#pensioni' | relative_url }}">Della spesa pubblica</a>,
  scomponendo i dati per regione, fascia d'età e tipologia di prestazione.
  Fonte: INPS — Osservatorio statistico sulle pensioni erogate (dati vigenti al 1° gennaio 2026).
  Alcune sezioni previste dallo schema di questa pagina sono ancora in fase di raccolta dati
  e sono segnalate esplicitamente più sotto, senza valori inventati nel frattempo.
  Metodo descritto per esteso nella <a href="{{ '/metodologia/' | relative_url }}">nota metodologica</a>.
</p>
</div>

<div class="ita-spende">

<nav>
  <div class="nav-brand">ITALIA<span>SPENDE</span></div>
  <button class="nav-toggle" id="navToggle" aria-label="Apri il menu" aria-expanded="false" aria-controls="navLinks">
    <span></span><span></span><span></span>
  </button>
  <div class="nav-links" id="navLinks">
    <a href="#pens-regione">Per regione</a>
    <a href="#pens-eta">Per età</a>
    <a href="#pens-tipologia">Per tipologia</a>
    <a href="#pens-ivs-gias">IVS/GIAS</a>
    <a href="#pensioni-dettaglio">Serie storica</a>
    <a href="#flussi">Flussi INPS</a>
    <a href="#pensioni-regioni">Regioni (standard.)</a>
    <a href="{{ '/spesa-pubblica/#pensioni' | relative_url }}">← Panoramica generale</a>
  </div>
</nav>

<main class="ita-spende__main">

<!-- SEZIONE 1: PER REGIONE -->
<section class="section" id="pens-regione">
  <div class="section-header">
    <span class="section-num">01 /</span>
    <h2 class="section-title">Pensioni per regione</h2>
  </div>
  <p class="section-desc">Numero di pensioni vigenti e importo medio mensile lordo per regione di residenza del titolare. Per il confronto corretto per struttura anagrafica (che tiene conto del fatto che le regioni più anziane hanno naturalmente più pensionati), vedi il <a href="#pensioni-regioni">coefficiente standardizzato</a> più sotto in questa pagina.</p>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Numero di pensioni vigenti per regione — 1.1.2026</div>
    <span class="source-tag static"><span class="source-dot"></span>INPS — Osservatorio statistico pensioni erogate, "Complesso delle pensioni vigenti per residenza del titolare"</span>
    <div class="canvas-wrap" style="height:520px;">
      <canvas id="pensRegioneChart" role="img" aria-label="Numero di pensioni vigenti per regione, dalla più bassa alla più alta.">Numero pensioni per regione, INPS 1.1.2026.</canvas>
    </div>
  </div>

  <div class="insight">
    <strong>Da leggere insieme alla popolazione regionale:</strong> Lombardia e Lazio hanno il numero assoluto più alto perché sono le regioni più popolose, non necessariamente perché hanno una quota di pensionati più alta in proporzione. Per il confronto proporzionale e corretto per età, usa il coefficiente standardizzato nella sezione Regioni della panoramica generale.
  </div>
</section>

<!-- SEZIONE 2: PER ETA -->
<section class="section" id="pens-eta">
  <div class="section-header">
    <span class="section-num">02 /</span>
    <h2 class="section-title">Pensioni per fascia d'età del titolare</h2>
  </div>
  <p class="section-desc">Età del titolare della pensione al 1° gennaio 2026 — non l'età al momento del pensionamento, che è un dato diverso e qui non trattato. Le fasce includono anche pensioni ai superstiti percepite da persone molto giovani (orfani, coniugi superstiti).</p>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Numero di pensioni vigenti per fascia d'età — 1.1.2026</div>
    <span class="source-tag static"><span class="source-dot"></span>INPS — Osservatorio statistico pensioni erogate, "Complesso delle pensioni vigenti", tutte le categorie</span>
    <div class="canvas-wrap" style="height:280px;">
      <canvas id="pensEtaChart" role="img" aria-label="Numero pensioni per fascia d'eta: under 65 3,38 milioni, 65-74 anni 6,50 milioni, 75-84 anni 6,78 milioni, 85 e oltre 4,59 milioni.">Numero pensioni per fascia d'età, INPS 1.1.2026.</canvas>
    </div>
  </div>

  <div class="insight">
    Quasi 3,4 milioni di pensioni sono percepite da persone under 65 — in parte pensioni di anzianità/anticipate liquidate prima dell'età di vecchiaia, in parte pensioni ai superstiti (incluse quelle di orfani minorenni) e pensioni di invalidità, che non hanno soglia minima di età.
  </div>
</section>

<!-- SEZIONE 3: PER TIPOLOGIA -->
<section class="section" id="pens-tipologia">
  <div class="section-header">
    <span class="section-num">03 /</span>
    <h2 class="section-title">Pensioni per tipologia di prestazione</h2>
  </div>
  <p class="section-desc">Le cinque categorie usate dall'INPS nella classificazione delle pensioni vigenti. Le ultime due (assegni sociali e invalidi civili) sono prestazioni assistenziali, finanziate dalla fiscalità generale (GIAS) e non dai contributi — a differenza delle prime tre, previdenziali.</p>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Numero di pensioni e importo medio mensile per tipologia — 1.1.2026</div>
    <span class="source-tag static"><span class="source-dot"></span>INPS — Osservatorio statistico pensioni erogate, "Complesso delle pensioni vigenti" per Categoria</span>
    <div style="display:flex;flex-wrap:wrap;gap:12px;margin:0.75rem 0;font-size:11px;color:var(--is-ink-3);">
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#1d4ed8;display:inline-block;"></span>Numero pensioni (scala sinistra)</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#c0392b;display:inline-block;"></span>Importo medio mensile € (scala destra)</span>
    </div>
    <div class="canvas-wrap" style="height:320px;">
      <canvas id="pensTipologiaChart" role="img" aria-label="Pensioni per tipologia: Vecchiaia/Anticipata 11,9 milioni a 1.717 euro medi, Invalidita 0,82 milioni a 1.144 euro, Superstiti 4,12 milioni a 878 euro, Assegno sociale 0,91 milioni a 556 euro, Invalidi civili 3,5 milioni a 509 euro.">Pensioni per tipologia, INPS 1.1.2026.</canvas>
    </div>
  </div>

  <div class="insight">
    <strong>Nota sulla classificazione assistenziale:</strong> "Pensioni/assegni sociali" e "Invalidi civili" sono voci distinte nella tavola INPS pur essendo entrambe prestazioni assistenziali: la prima è legata all'età e alla condizione economica, la seconda al riconoscimento di un'invalidità civile indipendentemente dall'età. Sommate, valgono circa 4,4 milioni di prestazioni — quasi un quarto di tutte le pensioni vigenti — e sono finanziate dalla fiscalità generale, non dai contributi previdenziali.
  </div>
</section>

<!-- SEZIONE 04: SCOMPOSIZIONE IVS / GIAS -->
<section class="section" id="pens-ivs-gias">
  <div class="section-header">
    <span class="section-num">04 /</span>
    <h2 class="section-title">Scomposizione IVS / GIAS</h2>
  </div>
  <p class="section-desc">Non tutta la spesa pensionistica italiana è finanziata dai contributi. Una parte è finanziata dalla fiscalità generale attraverso la <strong>GIAS</strong> — Gestione degli Interventi Assistenziali e di Sostegno alle gestioni previdenziali — una gestione separata dell'INPS che copre oneri di natura assistenziale (non contributiva). Distinguerla dalla componente <strong>IVS</strong> — Invalidità, Vecchiaia, Superstiti, cioè la gestione previdenziale ordinaria finanziata dai contributi — è necessario per non gonfiare il dato di spesa pensionistica italiana nei confronti con l'Europa, dove questa distinzione spesso non esiste o è contabilizzata diversamente.</p>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Spesa GIAS per tipologia di intervento — Consuntivo 2025</div>
    <span class="source-tag static"><span class="source-dot"></span>INPS — Rendiconto Generale 2025, Gestione n. 24 (GIAS), Conto Economico</span>
    <div style="overflow-x:auto; margin-top:0.75rem;">
      <table class="data-table">
        <thead>
          <tr>
            <th>Voce di spesa GIAS</th>
            <th class="num">2025 (mln €)</th>
          </tr>
        </thead>
        <tbody>
          <tr class="ita">
            <td>Oneri pensionistici</td>
            <td class="num" style="color:var(--red)">71.280</td>
          </tr>
          <tr>
            <td>Oneri per interventi a sostegno della famiglia</td>
            <td class="num">24.203</td>
          </tr>
          <tr>
            <td>Oneri per ADI e RDC (assegno di inclusione, reddito/pensione di cittadinanza)</td>
            <td class="num">5.620</td>
          </tr>
          <tr>
            <td>Oneri per il mantenimento del salario</td>
            <td class="num">6.781</td>
          </tr>
          <tr>
            <td>Oneri per riduzioni di oneri previdenziali</td>
            <td class="num">503</td>
          </tr>
          <tr>
            <td>Oneri per supporto alla formazione e al lavoro</td>
            <td class="num">439</td>
          </tr>
          <tr>
            <td>Oneri diversi</td>
            <td class="num">128</td>
          </tr>
          <tr>
            <td><strong>Totale spese per prestazioni istituzionali GIAS</strong></td>
            <td class="num"><strong>108.954</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="insight">
    <strong>Il numero che conta per il confronto europeo:</strong> su 108.954 milioni di euro di spesa GIAS nel 2025, <strong>71.280 milioni</strong> (contro i 72.340 milioni del 2024) sono classificati come "oneri pensionistici" — cioè finanziati dalla fiscalità generale, non dai contributi, ma che finiscono comunque dentro le statistiche aggregate di "spesa pensionistica" italiana. Questa componente assistenziale va tenuta distinta dalla spesa previdenziale/contributiva pura, gestita separatamente dalla Gestione Previdenziale e C/Terzi dell'INPS, che nel 2025 ha erogato prestazioni per 295.526 milioni di euro (288.776 milioni nel 2024).
  </div>

  <div class="insight" style="margin-top:1rem; border-color: var(--is-ink-3);">
    <strong>Limite dichiarato:</strong> la cifra di 295.526 milioni di euro della Gestione Previdenziale e C/Terzi include, oltre alle pensioni, anche altre prestazioni previdenziali non pensionistiche erogate dalle stesse gestioni (es. indennità di malattia e maternità, NASpI in alcuni casi). Non è quindi ancora possibile isolare da questa fonte una cifra "solo pensioni IVS" perfettamente pulita — per farlo servirebbe un'ulteriore tavola disaggregata dell'Osservatorio statistico INPS, che verrà integrata in un aggiornamento successivo.
  </div>
</section>

<!-- SEZIONE 05: PENSIONI DETTAGLIO -->
<section class="section" id="pensioni-dettaglio">
  <div class="section-header">
    <span class="section-num">05 /</span>
    <h2 class="section-title">Pensioni — serie storica e scomposizione</h2>
  </div>
  <p class="section-desc">Come è cambiata l'incidenza della spesa pensionistica sul PIL dal 1995 ad oggi, e come si distribuisce tra le principali categorie di pensione.</p>

  <!-- GRAFICO STORICO -->
  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Spesa pensionistica e protezione sociale % PIL — Italia 1995–2023</div>
    <span class="source-tag static" id="storiaSourceTag"><span class="source-dot"></span>caricamento da Eurostat…</span>
    <div class="canvas-wrap" style="height:320px;">
      <canvas id="storiaChart" role="img" aria-label="Serie storica spesa pensionistica italiana in percentuale del PIL">Serie storica disponibile dopo il caricamento dei dati.</canvas>
    </div>
    <div class="insight" style="margin-top:1rem;">
      La linea <strong>blu scuro</strong> mostra la spesa per protezione sociale totale (GF10, include pensioni, invalidità, superstiti, sussidi familiari). La linea <strong>rossa</strong> mostra la sola spesa per vecchiaia (GF1002), se disponibile nel dataset Eurostat per tutti gli anni. La tendenza di lungo periodo riflette l'invecchiamento demografico e le riforme successive: Dini (1995), Maroni (2004), Fornero (2011).
    </div>
  </div>

  <!-- METRICHE CHIAVE INPS -->
  <h3 style="font-size:1rem; font-weight:500; margin: 2.5rem 0 0.5rem;">Dati INPS — bilancio preventivo 2025–2026</h3>
  <p class="section-desc" style="margin-bottom:1.5rem;">Fonte: INPS — Bilancio preventivo 2025 (CA2024_0109) e Bilancio preventivo 2026 (CA2025_0181). I valori 2025 e 2026 sono previsioni approvate dal Consiglio di Amministrazione INPS. Non includono invalidi civili e pensioni assistenziali salvo dove indicato.</p>

  <div class="cards-grid" style="margin-bottom:1.5rem;">
    <div class="stat-card">
      <div class="stat-card-label">Pensioni totali 2025</div>
      <div class="stat-card-val">20,7 mln</div>
      <div class="stat-card-sub">incluse assistenziali e invalidi civili</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Solo gestioni contributive</div>
      <div class="stat-card-val">17,5 mln</div>
      <div class="stat-card-sub">escluse assistenziali e invalidi civili</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Spesa contributiva 2025</div>
      <div class="stat-card-val danger">320 mld €</div>
      <div class="stat-card-sub">solo gestioni previdenziali</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Importo medio annuo</div>
      <div class="stat-card-val warn">18.280 €</div>
      <div class="stat-card-sub">~1.523 €/mese lordi — gestioni contributive</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Contribuenti / 100 pensioni</div>
      <div class="stat-card-val warn">146,8</div>
      <div class="stat-card-sub">2025 — in lieve miglioramento vs 2024</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Pensioni previste 2026</div>
      <div class="stat-card-val">21,0 mln</div>
      <div class="stat-card-sub">+1,6% vs 2025 — previsione INPS</div>
    </div>
  </div>

  <!-- GRAFICO: PER TIPO -->
  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Pensioni per tipo — numero (mln) e spesa annua (mld €) — 2025</div>
    <span class="source-tag static"><span class="source-dot"></span>INPS — Bilancio preventivo 2025, Tabella pensioni vigenti al 31.12.2025</span>
    <div style="display:flex;flex-wrap:wrap;gap:12px;margin:0.75rem 0;font-size:11px;color:var(--is-ink-3);">
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#2a78d6;display:inline-block;"></span>Numero pensioni (scala sinistra)</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#e34948;display:inline-block;"></span>Spesa annua mld € (scala destra)</span>
    </div>
    <div class="canvas-wrap" style="height:260px;">
      <canvas id="tipoChart" role="img" aria-label="Pensioni per tipo: anzianità/anticipate 6,7 milioni per 186 miliardi, vecchiaia 5,8 milioni per 73 miliardi, indirette/reversibilità 4,2 milioni per 47 miliardi, invalidità 0,86 milioni per 12,8 miliardi.">Dati INPS bilancio preventivo 2025.</canvas>
    </div>
  </div>

  <!-- GRAFICO: IMPORTO MEDIO PER GESTIONE -->
  <h3 style="font-size:1rem; font-weight:500; margin: 2.5rem 0 0.5rem;">Scomposizione per gestione — pubblico, privato, autonomi</h3>
  <p class="section-desc" style="margin-bottom:1.5rem;">Le pensioni INPS si distribuiscono tra gestioni con storie contributive molto diverse. L'importo medio per le pensioni di anzianità/anticipate — quelle che meglio riflettono una carriera completa — rivela la profonda disomogeneità del sistema.</p>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Importo medio mensile lordo — pensioni anzianità/anticipate per gestione (€) — 2025</div>
    <span class="source-tag static"><span class="source-dot"></span>INPS — Bilancio preventivo 2025, importo medio annuo ÷ 12</span>
    <div class="canvas-wrap" style="height:320px;">
      <canvas id="gestioniChart" role="img" aria-label="Importo medio mensile pensioni di anzianità: ex INPDAI dirigenti 6203 euro, Ferrovie 2756, CTPS statali 2789, FPLD privati 2372, CPDEL enti locali 2351, commercianti 1828, artigiani 1696, coltivatori diretti 1235.">Dati INPS bilancio preventivo 2025 per gestione.</canvas>
    </div>
  </div>

  <!-- GRAFICO: RAPPORTO CONTRIBUENTI/PENSIONI -->
  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Rapporto contribuenti / 100 pensioni per gestione — 2025</div>
    <span class="source-tag static"><span class="source-dot"></span>INPS — Bilancio preventivo 2025, Tabella contribuenti/pensioni. Sotto 100 = deficit strutturale.</span>
    <div class="canvas-wrap" style="height:260px;">
      <canvas id="rapportoChart" role="img" aria-label="Contribuenti per 100 pensioni: FPLD privati 169, parasubordinati 167, CTPS statali 109, CPDEL enti locali 96, commercianti 92, artigiani 74, coltivatori diretti circa 60. Soglia di equilibrio: 100.">Rapporto contribuenti/pensioni per gestione INPS 2025.</canvas>
    </div>
  </div>

  <!-- GRAFICO: TREND 2024-2026 -->
  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Evoluzione pensioni per tipo — 2024 / 2025 / 2026 (milioni)</div>
    <span class="source-tag static"><span class="source-dot"></span>INPS — Bilancio preventivo 2025 (valori 2024 consuntivi, 2025 previsione) e Bilancio preventivo 2026 (previsione 2026)</span>
    <div style="display:flex;flex-wrap:wrap;gap:12px;margin:0.75rem 0;font-size:11px;color:var(--is-ink-3);">
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:16px;height:3px;background:#2a78d6;display:inline-block;"></span>Vecchiaia</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:16px;height:3px;background:#008300;display:inline-block;border-top: 3px dashed #008300;height:0;"></span>Anzianità/Anticipate</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:16px;height:3px;background:#e34948;display:inline-block;"></span>Invalidità</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:16px;height:3px;background:#eda100;display:inline-block;"></span>Indirette/Reversibilità</span>
    </div>
    <div class="canvas-wrap" style="height:240px;">
      <canvas id="trendPensioniChart" role="img" aria-label="Trend pensioni per tipo 2024-2026. Anzianità stabile a 6,7 milioni. Vecchiaia cresce da 5,78 a 5,96 milioni. Invalidità cala da 0,88 a 0,83 milioni. Indirette in lieve calo da 4,18 a 4,12 milioni.">Trend 2024-2026 pensioni per tipo da bilanci preventivi INPS.</canvas>
    </div>
  </div>

  <div class="insight">
    <strong>Nota metodologica:</strong> i dati di questa sezione sono estratti dai Bilanci Preventivi INPS 2025 e 2026, approvati dal Consiglio di Amministrazione. I valori di importo medio sono al lordo delle ritenute fiscali. Le pensioni di anzianità/anticipate hanno importi medi molto più alti (2.372 €/mese per il FPLD) rispetto alle pensioni di vecchiaia (1.050 €/mese) perché calcolate prevalentemente con il sistema retributivo — quelle erogate a lavoratori con carriere lunghe iniziate prima del 1996. Le gestioni degli autonomi (artigiani, commercianti, coltivatori) sono in deficit strutturale: hanno meno di 100 contribuenti per ogni 100 pensioni e ricevono trasferimenti dalle gestioni in surplus. Per approfondire: <a href="https://www.inps.it/it/it/dati-e-bilanci.html" target="_blank" rel="noopener" style="color:var(--is-ink); text-decoration:underline;">INPS — Dati e bilanci</a>.
  </div>

</section>

<!-- SEZIONE 06: FLUSSI FINANZIARI -->
<section class="section" id="flussi">
  <div class="section-header">
    <span class="section-num">06 /</span>
    <h2 class="section-title">Flussi finanziari INPS — serie storica 2020–2025</h2>
  </div>
  <p class="section-desc">Come si evolve il bilancio di cassa dell'INPS negli ultimi sei anni: entrate contributive, trasferimenti dallo Stato e uscite per prestazioni. La differenza tra ciò che l'INPS incassa dai contributi e ciò che paga è il <strong>deficit strutturale</strong> — il buco che lo Stato copre ogni anno con trasferimenti dalla fiscalità generale.</p>
  <p class="section-desc" style="margin-bottom:2rem;">Fonte: INPS — Note tecniche sui flussi finanziari dicembre 2020, 2021, 2022, 2023, 2024 e 2025. Tutti i valori sono in miliardi di euro, dati annuali consuntivi (dicembre suppletivo per 2020–2022, dicembre per 2023–2025).</p>

  <!-- CARDS CHIAVE -->
  <div class="cards-grid" style="margin-bottom:1.5rem;">
    <div class="stat-card">
      <div class="stat-card-label">Contributi raccolti 2025</div>
      <div class="stat-card-val ok">244 mld €</div>
      <div class="stat-card-sub">+11.2% vs 2024 — fine esonero contributivo</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Pensioni pagate 2025</div>
      <div class="stat-card-val warn">288 mld €</div>
      <div class="stat-card-sub">+1.3% vs 2024 — rallentamento crescita</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Deficit strutturale 2025</div>
      <div class="stat-card-val danger">~160 mld €</div>
      <div class="stat-card-sub">gap contributi → prestazioni, coperto dallo Stato</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Trasferimenti Stato 2025</div>
      <div class="stat-card-val warn">165 mld €</div>
      <div class="stat-card-sub">-8.4% vs 2024 — riduzione misure eccezionali</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Prestazioni temporanee 2025</div>
      <div class="stat-card-val">41 mld €</div>
      <div class="stat-card-sub">NASPI, CIG, Assegno Unico, ADI</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Invalidi civili 2025</div>
      <div class="stat-card-val danger">23,4 mld €</div>
      <div class="stat-card-sub">+23% in 5 anni — crescita più rapida del sistema</div>
    </div>
  </div>

  <!-- GRAFICO 1: ENTRATE VS USCITE -->
  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Entrate contributive vs pagamenti totali — 2020–2025 (mld €)</div>
    <span class="source-tag static"><span class="source-dot"></span>INPS — Note tecniche flussi finanziari dicembre 2020–2025</span>
    <div style="display:flex;flex-wrap:wrap;gap:12px;margin:0.75rem 0;font-size:11px;color:var(--is-ink-3);">
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:16px;height:3px;background:#1d4ed8;display:inline-block;"></span>Entrate contributive totali</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:16px;height:3px;background:#e34948;display:inline-block;"></span>Pagamenti correnti totali</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:16px;height:3px;background:#eda100;display:inline-block;border-top:3px dashed #eda100;height:0;"></span>Trasferimenti dallo Stato</span>
    </div>
    <div class="canvas-wrap" style="height:320px;">
      <canvas id="flussiChart" role="img" aria-label="Entrate contributive vs pagamenti INPS 2020-2025. Il gap tra le due linee è il deficit strutturale coperto dai trasferimenti statali.">Serie storica flussi finanziari INPS 2020-2025.</canvas>
    </div>
  </div>

  <!-- GRAFICO 2: DEFICIT STRUTTURALE -->
  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Deficit strutturale annuo — differenza tra pagamenti e contributi (mld €)</div>
    <span class="source-tag static"><span class="source-dot"></span>INPS — elaborazione su flussi finanziari annuali</span>
    <div class="canvas-wrap" style="height:260px;">
      <canvas id="deficitChart" role="img" aria-label="Deficit strutturale INPS per anno: 2020 circa 160 miliardi, minimo 2021 a 145, poi risalita a 179 nel 2024, discesa a 160 nel 2025.">Deficit strutturale INPS 2020-2025.</canvas>
    </div>
    <div class="insight" style="margin-top:1rem;">
      Il deficit 2020 è gonfiato dalla pandemia (prestazioni Covid straordinarie). Il 2024 tocca il picco a 179 miliardi principalmente per i maggiori trasferimenti verso i pensionati e la crescita delle pensioni pubbliche. Il calo 2025 è quasi interamente dovuto alla fine dell'esonero contributivo del 6–7%, che ha fatto rientrare ~19 miliardi di contributi che negli anni precedenti non venivano versati.
    </div>
  </div>

  <!-- GRAFICO 3: SCOMPOSIZIONE PENSIONI -->
  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Pensioni pagate per componente — 2020–2025 (mld €)</div>
    <span class="source-tag static"><span class="source-dot"></span>INPS — quadri di dettaglio pagamenti, flussi finanziari annuali</span>
    <div style="display:flex;flex-wrap:wrap;gap:12px;margin:0.75rem 0;font-size:11px;color:var(--is-ink-3);">
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#2a78d6;display:inline-block;"></span>Gestioni private (netto IC)</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#4a3aa7;display:inline-block;"></span>Gestioni pubbliche</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#e34948;display:inline-block;"></span>Invalidi civili</span>
    </div>
    <div class="canvas-wrap" style="height:300px;">
      <canvas id="pensioniTrendChart" role="img" aria-label="Scomposizione pensioni pagate 2020-2025. Gestioni private crescono da 168 a 195 miliardi. Gestioni pubbliche da 57 a 70 miliardi. Invalidi civili da 19 a 23 miliardi.">Scomposizione pensioni pagate INPS 2020-2025.</canvas>
    </div>
  </div>

  <!-- GRAFICO 4: PRESTAZIONI TEMPORANEE -->
  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Prestazioni temporanee — evoluzione 2020–2025 (mld €)</div>
    <span class="source-tag static"><span class="source-dot"></span>INPS — quadri di dettaglio pagamenti, flussi finanziari annuali</span>
    <div style="display:flex;flex-wrap:wrap;gap:12px;margin:0.75rem 0;font-size:11px;color:var(--is-ink-3);">
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#2a78d6;display:inline-block;"></span>NASPI</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#008300;display:inline-block;"></span>Assegno Unico</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#e34948;display:inline-block;"></span>RdC / ADI</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#eda100;display:inline-block;"></span>CIG e altre</span>
    </div>
    <div class="canvas-wrap" style="height:300px;">
      <canvas id="temporaneeChart" role="img" aria-label="Prestazioni temporanee 2020-2025. NASPI stabile intorno a 9-10 miliardi. Assegno Unico introdotto nel 2022, raggiunge 20 miliardi nel 2024. RdC cala da 9 miliardi a quasi zero nel 2024, sostituito da ADI.">Prestazioni temporanee INPS 2020-2025.</canvas>
    </div>
    <div class="insight" style="margin-top:1rem;">
      <strong>Tre discontinuità visibili nel grafico:</strong> il picco 2020 delle prestazioni Covid (11 mld straordinari); l'introduzione dell'Assegno Unico nel 2022 (12 mld al primo anno, poi crescita costante); la sostituzione del Reddito di Cittadinanza con l'Assegno di Inclusione nel 2024: il RdC è sceso da 7,4 a 0,1 miliardi, ma l'ADI che lo ha sostituito ha erogato 4,7 miliardi — la spesa complessiva della categoria è calata da 7,4 a 4,8 miliardi (-35%), non azzerata, perché una parte dei beneficiari rientrava nei nuovi criteri più restrittivi.
    </div>
  </div>

  <div class="insight">
    <strong>Nota metodologica:</strong> il "deficit strutturale" in questa sezione è calcolato come differenza tra pagamenti correnti totali e riscossioni dalla produzione (contributi + recupero crediti, esclusi trasferimenti Stato). Non coincide con il deficit di bilancio in senso contabile, che segue regole diverse. È piuttosto la misura di quanto il sistema previdenziale dipende ogni anno dalla fiscalità generale per funzionare — indipendentemente da come viene classificato contabilmente. Il 2020 include un'anticipazione di tesoreria straordinaria di 8 miliardi che non è trasferimento strutturale. Il 2021 include 12 miliardi di anticipazioni a gestioni previdenziali anch'esse straordinarie legate al Covid.
  </div>
</section>

<!-- SEZIONE 07: PENSIONI PER REGIONE — COEFFICIENTE STANDARDIZZATO -->
<section class="section" id="pensioni-regioni">
  <div class="section-header">
    <span class="section-num">07 /</span>
    <h2 class="section-title">Pensioni per regione — coefficiente standardizzato</h2>
  </div>
  <p class="section-desc">Confrontare le regioni sul numero grezzo di pensioni per abitante è fuorviante: una regione con più anziani ha naturalmente più pensionati, a parità di generosità del sistema. Il coefficiente standardizzato corregge per questo effetto demografico.</p>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Coefficiente di pensionamento standardizzato per regione (pensioni per 1.000 residenti, corretto per età) — 1.1.2026</div>
    <span class="source-tag static"><span class="source-dot"></span>Elaborazione propria su dati INPS (Osservatorio statistico sulle pensioni erogate) e ISTAT (popolazione residente 1.1.2026), standardizzazione indiretta</span>
    <div class="canvas-wrap" style="height:520px;">
      <canvas id="regioneChart" role="img" aria-label="Coefficiente di pensionamento standardizzato per regione, dal più basso al più alto: Valle d'Aosta 322,7, Trentino-Alto Adige 326,8, Sicilia 333,5, Liguria 337,6, Lazio 338,3, Toscana 342,3, Veneto 348,6, Sardegna 351,0, Piemonte 352,1, Friuli Venezia Giulia 354,3, Abruzzo 355,2, Campania 355,8, Lombardia 356,5, Molise 361,2, Basilicata 365,5, Emilia Romagna 367,7, Puglia 372,8, Marche 379,0, Umbria 387,7, Calabria 401,5. Media nazionale 360,7.">Coefficiente di pensionamento standardizzato per regione, elaborazione su dati INPS/ISTAT 1.1.2026.</canvas>
    </div>
  </div>

  <div class="insight">
    <strong>Come è calcolato:</strong> non esiste una tavola INPS che incrocia direttamente regione ed età dei pensionati — quell'incrocio è bloccato dalle regole sul segreto statistico (troppe celle piccole a livello regionale). Il coefficiente qui è quindi calcolato con <strong>standardizzazione indiretta</strong> (lo stesso principio dello standardized mortality ratio usato in epidemiologia): si prende il tasso di pensionamento età-specifico a livello nazionale, lo si applica alla struttura anagrafica reale di ciascuna regione (dati ISTAT) per ottenere le pensioni "attese" in quella regione, e si confronta con le pensioni osservate realmente. Una regione con un coefficiente sopra la media ha più pensionati di quanti ce ne aspetteremmo dalla sola sua composizione per età — quindi per ragioni diverse dall'invecchiamento (storia industriale, occupazionale, migratoria).
  </div>
  <div class="insight" style="margin-top:1rem;">
    <strong>Attenzione — Valle d'Aosta e Trentino-Alto Adige:</strong> queste due regioni (le più piccole per popolazione) mostrano uno scarto di circa 15-20 punti rispetto a una stima precedente basata su una tavola PDF trascritta manualmente. Non potendo verificare con un terzo metodo indipendente quale valore sia più accurato, il dato va considerato con più cautela per queste due regioni rispetto alle altre 18.
  </div>
</section>

<!-- SEZIONE: DATI IN ARRIVO -->
<section class="section" id="pens-in-arrivo">
  <div class="section-header">
    <span class="section-num">— /</span>
    <h2 class="section-title">Sezioni ancora da completare</h2>
  </div>
  <p class="section-desc">Coerentemente con il principio di questo Osservatorio di non pubblicare mai dati stimati o inventati, le seguenti sezioni previste per questa pagina restano in attesa delle tavole sorgente e non sono ancora popolate:</p>
  <ul style="margin: 0 0 1rem 1.4rem; color: var(--is-ink-2); line-height: 1.9;">
    <li><strong>Per genere</strong> — scomposizione uomini/donne per numero e importo medio</li>
    <li><strong>Distribuzione per fascia di importo mensile</strong> — quante pensioni sono sotto i 1.000€, tra 1.000 e 2.000€, ecc.</li>
    <li><strong>Rapporto contributi/prestazioni per gestione</strong> — il blocco più complesso, richiede l'incrocio tra tavole INPS e RGS Conto Annuale</li>
  </ul>
</section>

</main>

</div>

<footer class="pens-footer">
  <div style="max-width:980px; margin:0 auto;">
    Fonte: INPS — Osservatorio statistico sulle pensioni erogate dall'INPS (inclusa Gestione Dipendenti Pubblici), dati vigenti al 1° gennaio 2026.<br>
    Dati raccolti ed elaborati manualmente al momento; nessuna automazione di aggiornamento è ancora attiva per questa pagina.
  </div>
</footer>


<style>

@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&display=swap');
  

  .ita-spende *, .ita-spende *::before, .ita-spende *::after { box-sizing: border-box; margin: 0; padding: 0; }

  .ita-spende {
    --is-ink: #0d0d0d;
    --is-ink-2: #3a3a3a;
    --is-ink-3: #7a7a7a;
    --is-paper: #f5f3ee;
    --is-paper-2: #eceae3;
    --is-paper-3: #e0ddd4;
    --is-red: #c0392b;
    --is-red-light: #f9ebe9;
    --is-green: #1a6b3c;
    --is-green-light: #e8f4ed;
    --is-amber: #b45309;
    --is-amber-light: #fef3cd;
    --is-blue: #1d4ed8;
    --is-rule: 1px solid #c8c5bc;
    --is-font-sans: 'IBM Plex Sans', system-ui, sans-serif;
    --is-font-mono: 'IBM Plex Mono', monospace;
  }

  html { scroll-behavior: smooth; }

  .ita-spende {
    font-family: var(--is-font-sans);
    background: var(--is-paper);
    color: var(--is-ink);
    font-size: 15px;
    line-height: 1.6;
  }
  
 .ita-spende nav {
    position: sticky; top: 0; z-index: 100;
    background: var(--is-ink);
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 1.5rem;
    height: 52px;
    border-bottom: 2px solid var(--is-red);
    gap: 1rem;
  }
  .ita-spende .nav-brand {
    font-family: var(--is-font-mono);
    font-size: 14px; font-weight: 500;
    color: #fff; letter-spacing: 0.02em;
    flex-shrink: 0;
  }
  .ita-spende .nav-brand span { color: var(--is-red); }

  .ita-spende .nav-links { display: flex; align-items: center; gap: 1.4rem; }
  .ita-spende .nav-links > a {
    font-size: 12px; font-weight: 500; letter-spacing: 0.08em;
    text-transform: uppercase; color: #aaa;
    text-decoration: none; transition: color 0.15s;
    white-space: nowrap;
  }
  .ita-spende .nav-links > a:hover { color: #fff; }

  .ita-spende .nav-group { position: relative; }
  .ita-spende .nav-group__toggle {
    background: none; border: none; cursor: pointer; padding: 0;
    font-family: var(--is-font-sans);
    font-size: 12px; font-weight: 500; letter-spacing: 0.08em;
    text-transform: uppercase; color: #aaa;
    display: flex; align-items: center; gap: 4px;
    white-space: nowrap;
  }
  .ita-spende .nav-group__toggle:hover,
  .ita-spende .nav-group.open .nav-group__toggle { color: #fff; }
  .ita-spende .nav-caret { font-size: 10px; transition: transform 0.15s; }
  .ita-spende .nav-group.open .nav-caret { transform: rotate(180deg); }

  .ita-spende .nav-group__menu {
    display: none;
    position: absolute; top: 100%; left: 0; margin-top: 10px;
    background: var(--is-ink); border: 1px solid #333; border-top: 2px solid var(--is-red);
    min-width: 170px; padding: 6px 0;
    flex-direction: column;
  }
  .ita-spende .nav-group.open .nav-group__menu { display: flex; }
  .ita-spende .nav-group__menu a {
    padding: 9px 16px; font-size: 12px; font-weight: 500;
    letter-spacing: 0.06em; text-transform: uppercase;
    color: #aaa; text-decoration: none; white-space: nowrap;
  }
  .ita-spende .nav-group__menu a:hover { color: #fff; background: rgba(255,255,255,0.05); }

  .ita-spende .nav-tag {
    font-family: var(--is-font-mono);
    font-size: 11px; color: #555;
    flex-shrink: 0; white-space: nowrap;
  }

  .ita-spende .nav-toggle {
    display: none;
    flex-direction: column; justify-content: center; gap: 4px;
    background: none; border: none; cursor: pointer; padding: 8px;
    flex-shrink: 0;
  }
  .ita-spende .nav-toggle span { width: 20px; height: 2px; background: #fff; display: block; }

    .ita-spende .hero {
    background: var(--is-ink);
    color: #fff;
    padding: 5rem 2rem 4rem;
    border-bottom: var(--is-rule);
  }
  .ita-spende .hero-inner { max-width: 900px; margin: 0 auto; }
  .ita-spende .hero-eyebrow {
    font-family: var(--is-font-mono);
    font-size: 11px; letter-spacing: 0.12em;
    text-transform: uppercase; color: var(--is-red);
    margin-bottom: 1.5rem;
  }
  .ita-spende .hero h1 {
    font-size: clamp(2.2rem, 5vw, 3.8rem);
    font-weight: 300; line-height: 1.1;
    letter-spacing: -0.02em;
    margin-bottom: 1.5rem;
  }
  .ita-spende .hero h1 strong { font-weight: 600; color: #fff; }
  .ita-spende .hero-sub {
    font-size: 16px; font-weight: 300;
    color: #aaa; max-width: 580px; line-height: 1.7;
    margin-bottom: 3rem;
  }
  .ita-spende .hero-numbers {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 0;
    border-top: 1px solid #333;
  }
  .ita-spende .hero-num {
    padding: 1.5rem 1.5rem 1.5rem 0;
    border-right: 1px solid #333;
  }
  .ita-spende .hero-num:last-child { border-right: none; }
  .ita-spende .hero-num-val {
    font-family: var(--is-font-mono);
    font-size: 2rem; font-weight: 500;
    color: #fff; line-height: 1;
    margin-bottom: 0.4rem;
  }
  .ita-spende .hero-num-val.red { color: var(--is-red); }
  .ita-spende .hero-num-label { font-size: 12px; color: #666; font-weight: 300; }

  
  .ita-spende .section {
    max-width: 980px;
    margin: 0 auto;
    padding: 4rem 2rem;
    border-bottom: var(--is-rule);
  }
  .ita-spende .section-header {
    display: flex; align-items: baseline;
    gap: 1rem; margin-bottom: 2.5rem;
  }
  .ita-spende .section-num {
    font-family: var(--is-font-mono);
    font-size: 11px; color: var(--is-red);
    letter-spacing: 0.1em;
  }
  .ita-spende .section-title {
    font-size: 1.5rem; font-weight: 500;
    letter-spacing: -0.01em;
  }
  .ita-spende .section-desc {
    font-size: 14px; color: var(--is-ink-3);
    margin-bottom: 2rem; max-width: 620px;
    line-height: 1.7;
  }

  
  .ita-spende .chart-wrap {
    background: #fff;
    border: var(--is-rule);
    border-radius: 4px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
  }
  .ita-spende .chart-title {
    font-family: var(--is-font-mono);
    font-size: 11px; letter-spacing: 0.08em;
    text-transform: uppercase; color: var(--is-ink-3);
    margin-bottom: 1rem;
  }
  .ita-spende .canvas-wrap { position: relative; width: 100%; }

  
  .ita-spende .selector-row {
    display: flex; flex-wrap: wrap; gap: 0.5rem;
    margin-bottom: 1.5rem;
  }
  .ita-spende .sel-btn {
    font-family: var(--is-font-mono);
    font-size: 11px; letter-spacing: 0.06em;
    padding: 5px 14px;
    border: 1px solid var(--is-paper-3);
    background: #fff; color: var(--is-ink-2);
    border-radius: 2px; cursor: pointer;
    transition: all 0.15s;
  }
  .ita-spende .sel-btn:hover { border-color: var(--is-ink); }
  .ita-spende .sel-btn.active { background: var(--is-ink); color: #fff; border-color: var(--is-ink); }

  
  .ita-spende .cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1px;
    background: var(--is-paper-3);
    border: var(--is-rule);
    margin-bottom: 1.5rem;
  }
  .ita-spende .stat-card {
    background: #fff;
    padding: 1.25rem 1.5rem;
  }
  .ita-spende .stat-card-label {
    font-size: 11px; color: var(--is-ink-3);
    letter-spacing: 0.06em; text-transform: uppercase;
    margin-bottom: 0.5rem;
  }
  .ita-spende .stat-card-val {
    font-family: var(--is-font-mono);
    font-size: 1.6rem; font-weight: 500;
    line-height: 1; margin-bottom: 0.3rem;
  }
  .ita-spende .stat-card-val.danger { color: var(--is-red); }
  .ita-spende .stat-card-val.ok { color: var(--is-green); }
  .ita-spende .stat-card-val.warn { color: var(--is-amber); }
  .ita-spende .stat-card-sub { font-size: 11px; color: var(--is-ink-3); }

  
  .ita-spende .data-table {
    width: 100%; border-collapse: collapse;
    font-size: 13px;
  }
  .ita-spende .data-table th {
    font-family: var(--is-font-mono);
    font-size: 10px; letter-spacing: 0.08em;
    text-transform: uppercase; color: var(--is-ink-3);
    text-align: left; padding: 8px 12px;
    border-bottom: 2px solid var(--is-ink);
    background: var(--is-paper-2);
  }
  .ita-spende .data-table td {
    padding: 9px 12px;
    border-bottom: var(--is-rule);
    color: var(--is-ink-2);
  }
  .ita-spende .data-table tr.ita td {
    background: #fff8f7;
    font-weight: 500; color: var(--is-ink);
  }
  .ita-spende .data-table tr.ita td:first-child::before {
    content: '▶ ';
    color: var(--is-red); font-size: 9px;
  }
  .ita-spende .data-table tr:hover td { background: var(--is-paper-2); }
  .ita-spende .data-table .num {
    font-family: var(--is-font-mono);
    text-align: right;
  }
  .ita-spende .badge {
    display: inline-block;
    font-family: var(--is-font-mono);
    font-size: 10px; padding: 2px 7px;
    border-radius: 2px;
  }
  .ita-spende .badge-red { background: var(--is-red-light); color: var(--is-red); }
  .ita-spende .badge-green { background: var(--is-green-light); color: var(--is-green); }
  .ita-spende .badge-amber { background: var(--is-amber-light); color: var(--is-amber); }

  
  .ita-spende .insight {
    border-left: 3px solid var(--is-red);
    padding: 1rem 1.25rem;
    background: #fff;
    margin-top: 1.5rem;
    font-size: 13px; line-height: 1.7;
    color: var(--is-ink-2);
  }
  .ita-spende .insight strong { color: var(--is-ink); }

  
  .ita-spende footer {
    background: var(--is-ink);
    color: #555;
    padding: 2rem;
    font-family: var(--is-font-mono);
    font-size: 11px;
    line-height: 1.8;
  }
  .ita-spende footer a { color: #777; }

  
  .ita-spende .legend {
    display: flex; flex-wrap: wrap; gap: 1rem;
    margin-bottom: 1rem;
    font-size: 12px; color: var(--is-ink-2);
  }
  .ita-spende .legend-item { display: flex; align-items: center; gap: 6px; }
  .ita-spende .legend-sq { width: 12px; height: 12px; border-radius: 2px; flex-shrink: 0; }

  
  .ita-spende .tab-bar {
    display: flex; border-bottom: 2px solid var(--is-paper-3);
    margin-bottom: 1.5rem; gap: 0;
  }
  .ita-spende .tab {
    font-family: var(--is-font-mono);
    font-size: 11px; letter-spacing: 0.06em;
    text-transform: uppercase;
    padding: 10px 20px;
    border: none; border-bottom: 2px solid transparent;
    background: none; cursor: pointer;
    color: var(--is-ink-3); margin-bottom: -2px;
    transition: all 0.15s;
  }
  .ita-spende .tab.active { color: var(--is-ink); border-bottom-color: var(--is-red); }
  .ita-spende .tab-panel { display: none; }
  .ita-spende .tab-panel.active { display: block; }

  
  .ita-spende #dataStatus {
    font-family: var(--is-font-mono);
    font-size: 11px; color: #777;
    transition: color 0.3s;
    cursor: default;
  }
  .ita-spende #dataStatus.live { color: #5ec98a; }
  .ita-spende #dataStatus.fallback { color: #d9a441; }
  .ita-spende #dataStatus.error { color: #e07a6b; }

  .ita-spende .source-tag {
    display: inline-flex; align-items: center; gap: 5px;
    font-family: var(--is-font-mono);
    font-size: 10px; padding: 3px 8px;
    border-radius: 2px; margin-bottom: 0.75rem;
  }
  .ita-spende .source-tag.live { background: var(--is-green-light); color: var(--is-green); }
  .ita-spende .source-tag.static { background: var(--is-paper-3); color: var(--is-ink-3); }
  .ita-spende .source-dot { width: 6px; height: 6px; border-radius: 50%; background: currentColor; }

  
  .ita-spende .manovra-list { display: flex; flex-direction: column; gap: 0; }
  .ita-spende .manovra-item {
    display: grid;
    grid-template-columns: 90px 1fr;
    gap: 1.5rem;
    padding: 1.5rem 0;
    border-bottom: var(--is-rule);
  }
  .ita-spende .manovra-item:first-child { padding-top: 0; }
  .ita-spende .manovra-year {
    font-family: var(--is-font-mono);
    font-size: 1.4rem; font-weight: 500;
    color: var(--is-red);
    line-height: 1;
  }
  .ita-spende .manovra-title {
    font-size: 15px; font-weight: 500;
    margin-bottom: 0.4rem;
  }
  .ita-spende .manovra-desc {
    font-size: 13px; color: var(--is-ink-2);
    line-height: 1.6; margin-bottom: 0.75rem;
  }
  .ita-spende .manovra-links { display: flex; flex-wrap: wrap; gap: 0.5rem; }
  .ita-spende .manovra-link {
    font-family: var(--is-font-mono);
    font-size: 11px;
    color: var(--is-ink-2);
    text-decoration: none;
    padding: 4px 10px;
    border: 1px solid var(--is-paper-3);
    border-radius: 2px;
    transition: all 0.15s;
  }
  .ita-spende .manovra-link:hover { border-color: var(--is-ink); color: var(--is-ink); background: #fff; }
  .ita-spende .manovra-link::after { content: ' ↗'; opacity: 0.5; }

  @media (max-width: 640px)  {
    .ita-spende .manovra-item { grid-template-columns: 1fr; gap: 0.5rem; }

    .ita-spende .nav-toggle { display: flex; }
    .ita-spende .nav-tag { display: none; }
    .ita-spende .nav-links {
      display: none;
      position: absolute; top: 52px; left: 0; right: 0;
      background: var(--is-ink);
      flex-direction: column; align-items: stretch; gap: 0;
      padding: 6px 0;
      border-bottom: 2px solid var(--is-red);
      max-height: calc(100vh - 52px);
      overflow-y: auto;
    }
    .ita-spende .nav-links.open { display: flex; }
    .ita-spende .nav-links > a { padding: 13px 1.5rem; }

    .ita-spende .nav-group { width: 100%; }
    .ita-spende .nav-group__toggle {
      width: 100%; padding: 13px 1.5rem; justify-content: space-between;
    }
    .ita-spende .nav-group__menu {
      display: none;
      position: static; border: none; margin: 0; padding: 0 0 6px 2.5rem;
      background: none;
    }
    .ita-spende .nav-group.open .nav-group__menu { display: flex; }

    .ita-spende .hero { padding: 3rem 1rem 2.5rem; }
    .ita-spende .section { padding: 2.5rem 1rem; }
    .ita-spende .hero-num { padding: 1rem 1rem 1rem 0; }
  }



  .pens-footer {
    text-align: center;
    padding: 2rem 1.5rem;
    font-size: 12px;
    color: var(--is-ink-3);
    background: var(--is-paper-2);
    border-top: var(--is-rule);
  }
</style>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.js"></script>
<script>
window.addEventListener('DOMContentLoaded', () => {
  // Menu mobile (hamburger) — stessa logica delle altre pagine del sito
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
      const isOpen = navLinks.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen);
    });
    navLinks.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        navLinks.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // ── DATI: Pensioni per regione (fonte: INPS, vedi assets/data/pensioni.json) ──
  (function() {
    const ctx = document.getElementById('pensRegioneChart').getContext('2d');
    const labels = ["Valle d'Aosta","Molise","Basilicata","Trentino-Alto Adige","Umbria","Friuli-Venezia Giulia","Abruzzo","Liguria","Sardegna","Marche","Calabria","Toscana","Puglia","Sicilia","Piemonte","Emilia-Romagna","Veneto","Campania","Lazio","Lombardia"];
    const numero = [41248,112494,200019,330537,363773,468097,470622,596436,597532,600876,718745,1350324,1433938,1513886,1613592,1663593,1712439,1719157,1876594,3488543];
    const importo = [1527.07,1118.12,1093.24,1536.91,1217.19,1401.98,1181.86,1399.42,1186.15,1217.24,1023.29,1348.69,1099.86,1110.51,1410.56,1385.32,1358.80,1107.93,1404.08,1432.94];
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Numero pensioni',
          data: numero,
          backgroundColor: '#1d4ed8',
          borderRadius: 3
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: {
            label: ctx => ` ${ctx.parsed.x.toLocaleString('it-IT')} pensioni`,
            afterLabel: ctx => ` Importo medio: ${importo[ctx.dataIndex].toLocaleString('it-IT', {minimumFractionDigits:2, maximumFractionDigits:2})} €/mese`
          }}
        },
        scales: {
          x: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => (v/1e6).toFixed(1) + 'M' },
            title: { display: true, text: 'Numero pensioni', font: { size: 10 }, color: '#7a7a7a' } },
          y: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#0d0d0d' } }
        }
      }
    });
  })();

  // ── DATI: Pensioni per fascia d'età (fonte: INPS, vedi assets/data/pensioni.json) ──
  (function() {
    const ctx = document.getElementById('pensEtaChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Under 65', '65-74 anni', '75-84 anni', '85 e oltre'],
        datasets: [{
          label: 'Numero pensioni',
          data: [3384417, 6502395, 6781414, 4589765],
          backgroundColor: '#1d4ed8',
          borderRadius: 3
        }]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: {
            label: ctx => ` ${ctx.parsed.y.toLocaleString('it-IT')} pensioni`,
            afterLabel: ctx => {
              const importi = [970.03, 1621.64, 1322.97, 978.44];
              return ` Importo medio: ${importi[ctx.dataIndex].toLocaleString('it-IT', {minimumFractionDigits:2, maximumFractionDigits:2})} €/mese`;
            }
          }}
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 12 }, color: '#0d0d0d' } },
          y: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => (v/1e6).toFixed(1) + 'M' } }
        }
      }
    });
  })();

  // ── DATI: Pensioni per tipologia (fonte: INPS, vedi assets/data/pensioni.json) ──
  (function() {
    const ctx = document.getElementById('pensTipologiaChart').getContext('2d');
    new Chart(ctx, {
      data: {
        labels: ['Vecchiaia/\nAnticipata', 'Invalidità', 'Superstiti', 'Assegno\nsociale', 'Invalidi\ncivili'],
        datasets: [
          { type: 'bar', label: 'Numero (milioni)', data: [11.90, 0.82, 4.12, 0.91, 3.50],
            backgroundColor: '#1d4ed8', borderRadius: 3, yAxisID: 'y' },
          { type: 'line', label: 'Importo medio (€/mese)', data: [1717.51, 1144.40, 878.07, 556.04, 509.32],
            borderColor: '#c0392b', backgroundColor: 'transparent', borderWidth: 2,
            pointRadius: 5, pointBackgroundColor: '#c0392b', yAxisID: 'y2' }
        ]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: {
            label: ctx => ctx.datasetIndex === 0 ? ` ${ctx.parsed.y}M pensioni` : ` ${ctx.parsed.y.toLocaleString('it-IT', {minimumFractionDigits:2})} €/mese`
          }}
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#7a7a7a' } },
          y:  { grid: { color: '#e0ddd4' }, position: 'left',  ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + 'M' } },
          y2: { grid: { display: false },  position: 'right', ticks: { font: { size: 11 }, color: '#c0392b', callback: v => v + ' €' } }
        }
      }
    });
  })();

  // ── Helper condivisi (spostati da spesa-pubblica insieme alle sezioni 05-07) ──
  function setSourceTag(elId, isLive, extra) {
    const el = document.getElementById(elId);
    if (!el) return;
    el.className = 'source-tag ' + (isLive ? 'live' : 'static');
    el.innerHTML = '<span class="source-dot"></span>' +
      (isLive ? `dati ${extra || 'live Eurostat'}` : `dati statici ${extra || 'MEF/ISTAT 2023'}`);
  }

  function fetchWithTimeout(url, ms) {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), ms);
    return fetch(url, { signal: controller.signal })
      .finally(() => clearTimeout(timeout));
  }

  // ── SEZIONE 05: PENSIONI DETTAGLIO ────────────────────────────────────────────

  // Dati statici di fallback per la serie storica (Eurostat GF10 % PIL Italia).
  // Fonte: Eurostat gov_10a_exp, cofog99=GF10, unit=PC_GDP, geo=IT.
  // Aggiornare quando disponibili dati più recenti.
  const storiaStatica = {
    anni:    [1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023],
    gf10:    [21.3,21.7,22.0,21.8,21.9,21.7,21.8,22.2,22.5,22.5,22.7,22.4,22.1,22.5,23.9,24.0,23.9,24.5,24.5,24.5,24.2,24.0,23.8,23.7,23.8,25.4,24.5,23.8,21.0],
    // GF1002 (solo vecchiaia) ha copertura storica più limitata — disponibile da ~2001
    gf1002:  [null,null,null,null,null,null,13.1,13.4,13.6,13.7,13.9,13.7,13.5,13.8,14.7,14.8,14.7,15.1,15.2,15.1,14.9,14.8,14.6,14.5,14.6,15.6,15.1,14.7,null]
  };

  // Dati INPS reali — Bilancio Preventivo 2025 (CA2024_0109) e 2026 (CA2025_0181)
  // Pensioni vigenti al 31.12.2025, gestioni contributive, escluse assistenziali e invalidi civili

  // GRAFICO STORIA — costruito prima con dati statici, poi eventualmente sostituito da Eurostat live
  let storiaChartInstance = null;
  function buildStoriaChart(anni, gf10, gf1002) {
    if (storiaChartInstance) storiaChartInstance.destroy();
    const ctx = document.getElementById('storiaChart').getContext('2d');
    const datasets = [{
      label: 'Protezione sociale (GF10)',
      data: anni.map((a, i) => ({ x: a, y: gf10[i] })),
      borderColor: '#1d4ed8', backgroundColor: 'rgba(29,78,216,0.08)',
      borderWidth: 2, pointRadius: 3, pointHoverRadius: 5, fill: true, tension: 0.3
    }];
    if (gf1002 && gf1002.some(v => v !== null)) {
      datasets.push({
        label: 'Solo vecchiaia (GF1002)',
        data: anni.map((a, i) => ({ x: a, y: gf1002[i] })),
        borderColor: '#c0392b', backgroundColor: 'transparent',
        borderWidth: 2, borderDash: [4, 3], pointRadius: 3, pointHoverRadius: 5,
        fill: false, tension: 0.3, spanGaps: true
      });
    }
    storiaChartInstance = new Chart(ctx, {
      type: 'line', data: { datasets },
      options: {
        responsive: true, maintainAspectRatio: false, animation: { duration: 500 },
        plugins: {
          legend: { display: true, labels: { font: { size: 11, family: "'IBM Plex Mono', monospace" }, color: '#7a7a7a', boxWidth: 20 } },
          tooltip: { callbacks: { label: ctx => ` ${ctx.dataset.label}: ${ctx.parsed.y !== null ? ctx.parsed.y + '% PIL' : 'n.d.'}` } }
        },
        scales: {
          x: { type: 'linear', grid: { color: '#e8e5de' }, ticks: { font: { size: 11 }, color: '#7a7a7a', stepSize: 5, callback: v => String(v) }, min: 1995, max: 2023 },
          y: { grid: { color: '#e8e5de' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + '%' }, min: 0, max: 28,
            title: { display: true, text: '% PIL', font: { size: 10 }, color: '#7a7a7a' } }
        }
      }
    });
  }

  // GRAFICO 1: PER TIPO — barre + linea doppio asse
  (function() {
    const ctx = document.getElementById('tipoChart').getContext('2d');
    new Chart(ctx, {
      data: {
        labels: ['Anzianit\u00e0 /\nAnticipate', 'Vecchiaia', 'Indirette /\nReversibilit\u00e0', 'Invalidit\u00e0 /\nInabilit\u00e0'],
        datasets: [
          { type: 'bar', label: 'Numero (milioni)', data: [6.68, 5.82, 4.16, 0.86],
            backgroundColor: '#2a78d6', borderRadius: 3, yAxisID: 'y' },
          { type: 'line', label: 'Spesa annua (mld \u20ac)', data: [186.6, 73.8, 47.1, 12.8],
            borderColor: '#e34948', backgroundColor: 'transparent', borderWidth: 2,
            pointRadius: 5, pointBackgroundColor: '#e34948', yAxisID: 'y2' }
        ]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: { legend: { display: false },
          tooltip: { callbacks: { label: ctx => ctx.datasetIndex === 0 ? ` ${ctx.parsed.y}M pensioni` : ` ${ctx.parsed.y} mld \u20ac/anno` } }
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#7a7a7a' } },
          y:  { grid: { color: '#e8e5de' }, position: 'left',  ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + 'M' } },
          y2: { grid: { display: false },  position: 'right', ticks: { font: { size: 11 }, color: '#e34948', callback: v => v + ' mld' } }
        }
      }
    });
  })();

  // GRAFICO 2: IMPORTO MEDIO PER GESTIONE — orizzontale, ordinato decrescente
  (function() {
    const ctx = document.getElementById('gestioniChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Ex INPDAI\n(dirigenti)', 'Ferrovie\ndello Stato', 'CTPS\n(dip. statali)', 'FPLD\n(dip. privati)', 'CPDEL\n(enti locali)', 'Commercianti', 'Artigiani', 'Coltivatori\ndiretti'],
        datasets: [{
          label: '\u20ac/mese lordi',
          data: [6203, 2756, 2789, 2372, 2351, 1828, 1696, 1235],
          backgroundColor: ['#e34948','#2a78d6','#2a78d6','#2a78d6','#2a78d6','#eda100','#eda100','#eda100'],
          borderRadius: 3
        }]
      },
      options: {
        indexAxis: 'y', responsive: true, maintainAspectRatio: false,
        plugins: { legend: { display: false },
          tooltip: { callbacks: { label: ctx => ' ' + ctx.parsed.x.toLocaleString('it-IT') + ' \u20ac/mese lordi (pensioni anzianit\u00e0)' } }
        },
        scales: {
          x: { grid: { color: '#e8e5de' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v.toLocaleString('it-IT') + ' \u20ac' } },
          y: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#7a7a7a' } }
        }
      }
    });
  })();

  // GRAFICO 3: RAPPORTO CONTRIBUENTI/PENSIONI
  (function() {
    const ctx = document.getElementById('rapportoChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['FPLD\ndip. privati', 'Parasubord.', 'CTPS\nstatali', 'CPDEL\nenti locali', 'Commercianti', 'Artigiani', 'Coltivatori\ndiretti'],
        datasets: [{
          label: 'Contribuenti per 100 pensioni',
          data: [169, 167, 109, 96, 92, 74, 60],
          backgroundColor: ['#008300','#008300','#2a78d6','#e34948','#e34948','#e34948','#e34948'],
          borderRadius: 3
        }]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: { legend: { display: false },
          tooltip: { callbacks: { label: ctx => ' ' + ctx.parsed.y + ' contribuenti per 100 pensioni' } }
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#7a7a7a' } },
          y: { grid: { color: '#e8e5de' }, min: 0, max: 200,
            ticks: { font: { size: 11 }, color: '#7a7a7a' },
            afterDatasetsDraw(chart) {
              const ctx2 = chart.ctx, yS = chart.scales.y, xS = chart.scales.x;
              const y100 = yS.getPixelForValue(100);
              ctx2.save();
              ctx2.beginPath();
              ctx2.moveTo(xS.left, y100); ctx2.lineTo(xS.right, y100);
              ctx2.strokeStyle = '#e34948'; ctx2.lineWidth = 2;
              ctx2.setLineDash([6, 3]); ctx2.stroke(); ctx2.restore();
            }
          }
        }
      }
    });
  })();

  // GRAFICO 4: TREND 2024-2026 PER TIPO
  (function() {
    const ctx = document.getElementById('trendPensioniChart').getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['2024', '2025', '2026'],
        datasets: [
          { label: 'Vecchiaia',           data: [5.78, 5.82, 5.96], borderColor: '#2a78d6', backgroundColor: 'rgba(42,120,214,0.08)', borderWidth: 2, pointRadius: 4, fill: false, tension: 0.3 },
          { label: 'Anzianit\u00e0/Anticipate', data: [6.68, 6.68, 6.67], borderColor: '#008300', backgroundColor: 'transparent', borderWidth: 2, pointRadius: 4, fill: false, tension: 0.3, borderDash: [5,3] },
          { label: 'Invalidit\u00e0',          data: [0.88, 0.86, 0.83], borderColor: '#e34948', backgroundColor: 'transparent', borderWidth: 2, pointRadius: 4, fill: false, tension: 0.3, borderDash: [2,3] },
          { label: 'Indirette/Rev.',       data: [4.18, 4.16, 4.12], borderColor: '#eda100', backgroundColor: 'transparent', borderWidth: 2, pointRadius: 4, fill: false, tension: 0.3, borderDash: [8,3] }
        ]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: { legend: { display: false },
          tooltip: { callbacks: { label: ctx => ` ${ctx.dataset.label}: ${ctx.parsed.y.toFixed(2)}M pensioni` } }
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 12 }, color: '#7a7a7a' } },
          y: { grid: { color: '#e8e5de' }, min: 0, max: 8,
            ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v.toFixed(1) + 'M' } }
        }
      }
    });
  })();

  // FETCH EUROSTAT SERIE STORICA
  async function loadStoriaEurostat() {
    const anni = [1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023];
    const timeParams = anni.map(a => `time=${a}`).join('&');
    const urlGF10 = `${EUROSTAT_BASE}gov_10a_exp?format=JSON&unit=PC_GDP&sector=S13&cofog99=GF10&na_item=TE&geo=IT&${timeParams}`;
    const res = await fetchWithTimeout(urlGF10, EUROSTAT_TIMEOUT_MS);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const json = await res.json();
    const timeIndex = json.dimension.time.category.index;
    const values = json.value;
    const gf10Live = anni.map(a => {
      const idx = timeIndex[String(a)];
      if (idx === undefined) return null;
      const v = Array.isArray(values) ? values[idx] : values[String(idx)];
      return (v !== undefined && v !== null) ? Number(v) : null;
    });
    let gf1002Live = anni.map(() => null);
    try {
      const urlGF1002 = `${EUROSTAT_BASE}gov_10a_exp?format=JSON&unit=PC_GDP&sector=S13&cofog99=GF1002&na_item=TE&geo=IT&${timeParams}`;
      const res2 = await fetchWithTimeout(urlGF1002, EUROSTAT_TIMEOUT_MS);
      if (res2.ok) {
        const json2 = await res2.json();
        const ti2 = json2.dimension.time.category.index;
        const v2 = json2.value;
        gf1002Live = anni.map(a => {
          const idx = ti2[String(a)];
          if (idx === undefined) return null;
          const val = Array.isArray(v2) ? v2[idx] : v2[String(idx)];
          return (val !== undefined && val !== null) ? Number(val) : null;
        });
      }
    } catch(e) {}
    if (!gf10Live.some(v => v !== null)) throw new Error('Nessun valore GF10');
    return { anni, gf10: gf10Live, gf1002: gf1002Live };
  }

  // AVVIO
  buildStoriaChart(storiaStatica.anni, storiaStatica.gf10, storiaStatica.gf1002);
  setSourceTag('storiaSourceTag', false, '— dati statici Eurostat 2023');

  loadStoriaEurostat()
    .then(({ anni, gf10, gf1002 }) => {
      buildStoriaChart(anni, gf10, gf1002);
      setSourceTag('storiaSourceTag', true, '— Eurostat live');
    })
    .catch(e => {
      console.warn('Serie storica Eurostat non disponibile:', e.message);
      setSourceTag('storiaSourceTag', false, '— dati statici (Eurostat non raggiungibile)');
    });
  // ── SEZIONE 06: FLUSSI FINANZIARI INPS 2020–2025 ─────────────────────────────
  // Fonte: Note tecniche flussi finanziari INPS dicembre di ogni anno (annuale consuntivo)
  // Valori in miliardi di euro

  const flussiAnni = [2020, 2021, 2022, 2023, 2024, 2025];
  const flussiContrib  = [183.4, 194.1, 205.5, 214.6, 219.8, 244.4];
  const flussiProd     = [196.4, 207.8, 218.7, 229.9, 234.9, 262.2];
  const flussiStato    = [139.9, 142.3, 154.7, 160.4, 179.9, 164.8];
  const flussiPag      = [356.3, 352.6, 365.3, 392.6, 414.1, 421.8];
  const flussiDeficit  = flussiAnni.map((_, i) => parseFloat((flussiPag[i] - flussiProd[i]).toFixed(1)));

  const pensPrivate    = [168.6, 165.6, 170.9, 182.9, 192.4, 194.5];
  const pensPubbliche  = [57.4, 58.6, 62.2, 65.4, 68.8, 69.7];
  const pensIC         = [19.0, 19.9, 20.4, 21.4, 22.6, 23.4];

  const tempNaspi    = [9.5, 7.5, 7.9, 8.8, 9.6, 10.1];
  const tempAunico   = [0, 0, 12.3, 17.4, 20.0, 19.8];
  const tempRdcAdi   = [7.2, 9.1, 9.0, 7.4, 4.8, 6.1];
  const tempTotArr   = [34.5, 30.9, 35.1, 38.7, 39.3, 41.1];
  const tempCigAltre = flussiAnni.map((_, i) => parseFloat((tempTotArr[i] - tempNaspi[i] - tempAunico[i] - tempRdcAdi[i]).toFixed(1)));

  const gridC = '#e8e5de';
  const tickC = '#7a7a7a';
  const baseOpts = { responsive: true, maintainAspectRatio: false };

  (function() {
    const ctx = document.getElementById('flussiChart').getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: flussiAnni,
        datasets: [
          { label: 'Entrate contributive', data: flussiContrib,
            borderColor: '#1d4ed8', backgroundColor: 'rgba(29,78,216,0.07)',
            borderWidth: 2.5, pointRadius: 4, fill: true, tension: 0.3 },
          { label: 'Pagamenti correnti', data: flussiPag,
            borderColor: '#e34948', backgroundColor: 'rgba(227,73,72,0.07)',
            borderWidth: 2.5, pointRadius: 4, fill: true, tension: 0.3 },
          { label: 'Trasferimenti Stato', data: flussiStato,
            borderColor: '#eda100', backgroundColor: 'transparent',
            borderWidth: 2, borderDash: [6,3], pointRadius: 4, fill: false, tension: 0.3 }
        ]
      },
      options: {
        ...baseOpts,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: { label: ctx => ` ${ctx.dataset.label}: ${ctx.parsed.y} mld \u20ac` } }
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 12 }, color: tickC } },
          y: { grid: { color: gridC }, min: 0, max: 480,
            ticks: { font: { size: 11 }, color: tickC, callback: v => v + ' mld' } }
        }
      }
    });
  })();

  (function() {
    const ctx = document.getElementById('deficitChart').getContext('2d');
    const noteDeficit = [
      'Anno Covid — prestazioni straordinarie', 'Minimo — recupero post-Covid',
      'Stabilizzazione post-Covid', 'Perequazione +7% e Assegno Unico',
      'Picco — trasf. Stato eccezionali', 'Calo — fine esonero contributivo'
    ];
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: flussiAnni,
        datasets: [{
          label: 'Deficit strutturale',
          data: flussiDeficit,
          borderColor: '#e34948', backgroundColor: 'rgba(227,73,72,0.12)',
          borderWidth: 2.5, pointRadius: 5,
          pointBackgroundColor: ['#e34948','#008300','#e34948','#e34948','#e34948','#008300'],
          fill: true, tension: 0.3
        }]
      },
      options: {
        ...baseOpts,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: {
            label: ctx => ` Deficit strutturale: ${ctx.parsed.y} mld \u20ac`,
            afterLabel: ctx => ' ' + (noteDeficit[ctx.dataIndex] || '')
          }}
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 12 }, color: tickC } },
          y: { grid: { color: gridC }, min: 100, max: 220,
            ticks: { font: { size: 11 }, color: tickC, callback: v => v + ' mld' } }
        }
      }
    });
  })();

  (function() {
    const ctx = document.getElementById('pensioniTrendChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: flussiAnni,
        datasets: [
          { label: 'Gestioni private (netto IC)', data: pensPrivate,   backgroundColor: '#2a78d6', borderRadius: 2, stack: 'p' },
          { label: 'Gestioni pubbliche',          data: pensPubbliche, backgroundColor: '#4a3aa7', borderRadius: 2, stack: 'p' },
          { label: 'Invalidi civili',             data: pensIC,        backgroundColor: '#e34948', borderRadius: 2, stack: 'p' }
        ]
      },
      options: {
        ...baseOpts,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: {
            label: ctx => ` ${ctx.dataset.label}: ${ctx.parsed.y} mld \u20ac`,
            footer: items => ` Totale: ${items.reduce((s,i) => s+i.parsed.y, 0).toFixed(1)} mld \u20ac`
          }}
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 12 }, color: tickC }, stacked: true },
          y: { grid: { color: gridC }, stacked: true, min: 0, max: 330,
            ticks: { font: { size: 11 }, color: tickC, callback: v => v + ' mld' } }
        }
      }
    });
  })();

  (function() {
    const ctx = document.getElementById('temporaneeChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: flussiAnni,
        datasets: [
          { label: 'NASPI',         data: tempNaspi,    backgroundColor: '#2a78d6', borderRadius: 2, stack: 't' },
          { label: 'Assegno Unico', data: tempAunico,   backgroundColor: '#008300', borderRadius: 2, stack: 't' },
          { label: 'RdC / ADI',     data: tempRdcAdi,   backgroundColor: '#e34948', borderRadius: 2, stack: 't' },
          { label: 'CIG e altre',   data: tempCigAltre, backgroundColor: '#eda100', borderRadius: 2, stack: 't' }
        ]
      },
      options: {
        ...baseOpts,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: {
            label: ctx => ` ${ctx.dataset.label}: ${ctx.parsed.y.toFixed(1)} mld \u20ac`,
            footer: items => ` Totale: ${items.reduce((s,i) => s+i.parsed.y, 0).toFixed(1)} mld \u20ac`
          }}
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 12 }, color: tickC }, stacked: true },
          y: { grid: { color: gridC }, stacked: true, min: 0, max: 50,
            ticks: { font: { size: 11 }, color: tickC, callback: v => v + ' mld' } }
        }
      }
    });
  })();

  // ── SEZIONE 07: PENSIONI PER REGIONE — COEFFICIENTE STANDARDIZZATO ───────────
  // Elaborazione propria: standardizzazione indiretta su dati INPS (Osservatorio
  // statistico sulle pensioni erogate, stock regionale + distribuzione nazionale
  // per età) e ISTAT (popolazione residente per regione ed età, 1.1.2026).
  // Vedi nota metodologica nella sezione per il dettaglio del calcolo.
  (function() {
    const ctx = document.getElementById('regioneChart').getContext('2d');
    const regioni = ["Valle d'Aosta", 'Trentino-Alto Adige', 'Sicilia', 'Liguria', 'Lazio', 'Toscana', 'Veneto', 'Sardegna', 'Piemonte', 'Friuli V.G.', 'Abruzzo', 'Campania', 'Lombardia', 'Molise', 'Basilicata', 'Emilia Romagna', 'Puglia', 'Marche', 'Umbria', 'Calabria'];
    const coeff = [322.7, 326.8, 333.5, 337.6, 338.3, 342.3, 348.6, 351.0, 352.1, 354.3, 355.2, 355.8, 356.5, 361.2, 365.5, 367.7, 372.8, 379.0, 387.7, 401.5];
    const media = 360.7;
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: regioni,
        datasets: [{
          label: 'Pensioni per 1.000 residenti (standardizzato)',
          data: coeff,
          backgroundColor: coeff.map(v => v < media ? '#2a78d6' : '#e34948'),
          borderRadius: 3
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: { label: ctx => ` ${ctx.parsed.x.toFixed(1)} per 1.000 residenti (standardizzato)` } },
          annotation: undefined
        },
        scales: {
          x: { grid: { color: '#e8e5de' }, ticks: { font: { size: 11 }, color: '#7a7a7a' },
            title: { display: true, text: 'Pensioni per 1.000 residenti', font: { size: 10 }, color: '#7a7a7a' } },
          y: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#3a3a3a' } }
        }
      }
    });
  })();
});
</script>
