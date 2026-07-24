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
  <p class="section-desc">Numero di pensioni vigenti e importo medio mensile lordo per regione di residenza del titolare. Per il confronto corretto per struttura anagrafica (che tiene conto del fatto che le regioni più anziane hanno naturalmente più pensionati), vedi il <a href="{{ '/spesa-pubblica/#pensioni-regioni' | relative_url }}">coefficiente standardizzato</a> nella panoramica generale.</p>

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

<!-- SEZIONE: DATI IN ARRIVO -->
<section class="section" id="pens-in-arrivo">
  <div class="section-header">
    <span class="section-num">— /</span>
    <h2 class="section-title">Sezioni ancora da completare</h2>
  </div>
  <p class="section-desc">Coerentemente con il principio di questo Osservatorio di non pubblicare mai dati stimati o inventati, le seguenti sezioni previste per questa pagina restano in attesa delle tavole sorgente e non sono ancora popolate:</p>
  <ul style="margin: 0 0 1rem 1.4rem; color: var(--is-ink-2); line-height: 1.9;">
    <li><strong>Scomposizione IVS / GIAS</strong> — separazione tra spesa previdenziale (contributiva) e assistenziale (fiscalità generale), necessaria per non gonfiare il dato di spesa pensionistica sul PIL nei confronti europei</li>
    <li><strong>Per gestione</strong> — confronto tra FPLD (privato), Gestione Dipendenti Pubblici, autonomi e gestione separata</li>
    <li><strong>Per genere</strong> — scomposizione uomini/donne per numero e importo medio</li>
    <li><strong>Distribuzione per fascia di importo mensile</strong> — quante pensioni sono sotto i 1.000€, tra 1.000 e 2.000€, ecc.</li>
    <li><strong>Serie storiche</strong> — evoluzione 2019-2024 di numero pensionati, spesa totale e incidenza sul PIL</li>
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
});
</script>
