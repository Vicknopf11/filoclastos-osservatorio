---
layout: default
title: "Sanità — spesa pubblica e privata per regione"
description: "Approfondimento sulla spesa sanitaria italiana: confronto regionale tra spesa pubblica e spesa privata/out-of-pocket dei cittadini, con fonti RGS sempre citate."
---
<div class="prose">
<span class="prose__kicker">Approfondimento</span>
<h1>Sanità — spesa per regione</h1>
<p>
  Seconda voce di spesa pubblica dopo le pensioni: qui la spesa sanitaria italiana
  scomposta per regione, con il confronto tra quanto viene speso dal Servizio Sanitario
  Nazionale e quanto pagano direttamente i cittadini di tasca propria (out-of-pocket).
  Fonte principale: Ministero dell'Economia e delle Finanze — Ragioneria Generale dello
  Stato, "Il monitoraggio della spesa sanitaria", Roma, novembre 2025.
  Alcune sezioni previste dallo schema di questa pagina sono ancora in fase di raccolta
  dati e sono segnalate esplicitamente più sotto, senza valori inventati nel frattempo.
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
    <a href="#sanita-pubblica">Spesa pubblica</a>
    <a href="#sanita-privata">Spesa privata</a>
    <a href="{{ '/spesa-pubblica/' | relative_url }}">← Panoramica generale</a>
  </div>
</nav>

<main class="ita-spende__main">

<!-- SEZIONE 1: SPESA PUBBLICA PER REGIONE -->
<section class="section" id="sanita-pubblica">
  <div class="section-header">
    <span class="section-num">01 /</span>
    <h2 class="section-title">Spesa sanitaria pubblica per regione</h2>
  </div>
  <p class="section-desc">Spesa sanitaria corrente di Conto Economico (CE) — cioè la spesa effettiva sostenuta dagli enti del Servizio Sanitario Nazionale (SSN), al netto di ammortamenti e rivalutazioni. Il confronto tra regioni grezzo è fuorviante: una regione con più anziani o più patologie croniche spende naturalmente di più. Qui sotto il dato è mostrato sia in valore assoluto sia pro capite.</p>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Spesa sanitaria pubblica pro capite per regione — Anno 2024 (€)</div>
    <span class="source-tag static"><span class="source-dot"></span>MEF-RGS — "Il monitoraggio della spesa sanitaria", nov. 2025 (Tab. 1.3); popolazione INPS/ISTAT 1.1.2026</span>
    <div style="display:flex;flex-wrap:wrap;gap:12px;margin:0.75rem 0;font-size:11px;color:var(--is-ink-3);">
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#2a78d6;display:inline-block;"></span>Nessun piano di rientro</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#e34948;display:inline-block;"></span>Piano di rientro</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#eda100;display:inline-block;"></span>Autonomia speciale</span>
    </div>
    <div class="canvas-wrap" style="height:520px;">
      <canvas id="sanitaPubRegioneChart" role="img" aria-label="Spesa sanitaria pubblica pro capite per regione, dalla più bassa (Lazio, 2.229 euro) alla più alta (Trentino-Alto Adige, 2.979 euro). Media nazionale 2.366 euro.">Spesa sanitaria pubblica pro capite per regione, 2024.</canvas>
    </div>
  </div>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Spesa sanitaria pubblica corrente — Italia, serie storica 2015–2024 (mld €)</div>
    <span class="source-tag static"><span class="source-dot"></span>MEF-RGS — "Il monitoraggio della spesa sanitaria", nov. 2025 (Tab. 1.3, totale ITALIA)</span>
    <div class="canvas-wrap" style="height:280px;">
      <canvas id="sanitaStoriaChart" role="img" aria-label="Spesa sanitaria pubblica italiana da 111,1 miliardi nel 2015 a 139,4 miliardi nel 2024, con impennata nel 2020 per la pandemia.">Serie storica spesa sanitaria pubblica italiana 2015-2024.</canvas>
    </div>
  </div>

  <div class="insight">
    <strong>Nord/Sud non è la chiave di lettura più esatta:</strong> il divario segue soprattutto la distinzione amministrativa. Le quattro regioni con la spesa pubblica pro capite più bassa (Lazio, Campania, Calabria, Sicilia) sono tutte sotto <strong>piano di rientro</strong> — un regime di commissariamento e vincoli di spesa imposto quando i conti sanitari regionali sono in disavanzo strutturale. All'estremo opposto, le <strong>autonomie speciali</strong> (Trentino-Alto Adige, Valle d'Aosta, Friuli Venezia Giulia, Sardegna) — che finanziano la sanità con risorse proprie e non con il fondo sanitario nazionale — spendono sistematicamente di più: Trentino-Alto Adige tocca 2.979 €/persona, il 26% sopra la media nazionale di 2.366 €.
  </div>
  <div class="insight" style="margin-top:1rem; border-color: var(--is-ink-3);">
    <strong>Limite dichiarato:</strong> il dato pro capite usa la popolazione regionale al 1° gennaio 2026 (stessa fonte già usata per le pensioni), confrontata con la spesa sanitaria dell'anno 2024 — un disallineamento di circa due anni. Le variazioni di popolazione regionale in questo arco sono generalmente contenute, ma il dato andrebbe aggiornato con la popolazione 2024 non appena reperita.
  </div>
</section>

<!-- SEZIONE 2: SPESA PRIVATA / OUT-OF-POCKET -->
<section class="section" id="sanita-privata">
  <div class="section-header">
    <span class="section-num">02 /</span>
    <h2 class="section-title">Spesa sanitaria privata (out-of-pocket) per regione</h2>
  </div>
  <p class="section-desc">Quanto pagano i cittadini direttamente di tasca propria per prestazioni sanitarie — visite specialistiche, farmaci, odontoiatria, dispositivi medici — al netto di quanto rimborsato dal SSN. Fonte: Sistema Tessera Sanitaria, che raccoglie questi dati per la dichiarazione dei redditi precompilata; include anche il ticket sanitario pagato dai cittadini.</p>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Spesa sanitaria privata pro capite per regione — Anno 2024 (€)</div>
    <span class="source-tag static"><span class="source-dot"></span>MEF-RGS — "Il monitoraggio della spesa sanitaria", nov. 2025 (Tab. 4.13); popolazione INPS/ISTAT 1.1.2026</span>
    <div class="canvas-wrap" style="height:520px;">
      <canvas id="sanitaPrivRegioneChart" role="img" aria-label="Spesa sanitaria privata pro capite per regione, dalla più bassa (Basilicata, 438 euro) alla più alta (Lombardia, 1.099 euro).">Spesa sanitaria privata pro capite per regione, 2024.</canvas>
    </div>
  </div>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Spesa sanitaria privata — Italia, serie storica 2016–2024 (mld €)</div>
    <span class="source-tag static"><span class="source-dot"></span>MEF-RGS — "Il monitoraggio della spesa sanitaria", nov. 2025 (Tab. 4.12, totale ITALIA)</span>
    <div class="canvas-wrap" style="height:280px;">
      <canvas id="sanitaPrivStoriaChart" role="img" aria-label="Spesa sanitaria privata italiana da 28,1 miliardi nel 2016 a 46,4 miliardi nel 2024, con calo nel 2020 per la pandemia (-11,6%) e crescita sostenuta dopo.">Serie storica spesa sanitaria privata italiana 2016-2024.</canvas>
    </div>
  </div>

  <div class="insight">
    <strong>Chi spende di più di tasca propria non è chi ha il SSN più debole:</strong> Lombardia (1.099 €/persona) e Trentino-Alto Adige (880 €) hanno la spesa privata pro capite più alta, nonostante abbiano anche una spesa pubblica pro capite sopra la media — segno che la spesa privata qui è complementare (per tempi di attesa o scelta) più che sostitutiva. All'opposto, le regioni con la spesa pubblica pro capite più bassa (Calabria, Campania, Sicilia) hanno anche tra le spese private più basse: chi ha meno reddito disponibile spesso rinuncia del tutto, invece di rivolgersi al privato — un dato che da solo non distingue le due situazioni, ma che segnala un'area da approfondire con i dati di rinuncia alle cure (vedi sezioni ancora da completare).
  </div>
</section>

<!-- SEZIONE: DATI IN ARRIVO -->
<section class="section" id="sanita-in-arrivo">
  <div class="section-header">
    <span class="section-num">— /</span>
    <h2 class="section-title">Sezioni ancora da completare</h2>
  </div>
  <p class="section-desc">Coerentemente con il principio di questo Osservatorio di non pubblicare mai dati stimati o inventati, le seguenti sezioni previste per questa pagina restano in attesa delle tavole sorgente e non sono ancora popolate:</p>
  <ul style="margin: 0 0 1rem 1.4rem; color: var(--is-ink-2); line-height: 1.9;">
    <li><strong>Confronto europeo</strong> — spesa sanitaria in percentuale del PIL, Italia vs altri paesi UE (dataset Eurostat gov_10a_exp, cofog99=GF07, e hlth_sha11_hf per pubblico/privato), stessa architettura statica già usata per le pensioni</li>
    <li><strong>Liste d'attesa e rinuncia alle cure</strong> — quota di popolazione che rinuncia a prestazioni sanitarie per motivi economici o per tempi di attesa troppo lunghi (fonte probabile: ISTAT, indagine "Aspetti della vita quotidiana")</li>
  </ul>
</section>

</main>

</div>

<footer class="pens-footer">
  <div style="max-width:980px; margin:0 auto;">
    Fonte: Ministero dell'Economia e delle Finanze — Ragioneria Generale dello Stato, "Il monitoraggio della spesa sanitaria", Roma, novembre 2025. Popolazione regionale: INPS/ISTAT, dati al 1° gennaio 2026 (vedi nota metodologica sul disallineamento temporale).<br>
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

const sanitaRegioni = ["Lazio", "Campania", "Calabria", "Sicilia", "Marche", "Basilicata", "Abruzzo", "Puglia", "Lombardia", "Piemonte", "Veneto", "Umbria", "Toscana", "Liguria", "Emilia-Romagna", "Molise", "Sardegna", "Friuli-Venezia Giulia", "Valle d'Aosta", "Trentino-Alto Adige"];
const sanitaPubPC = [2229, 2236, 2242, 2247, 2258, 2283, 2297, 2302, 2352, 2373, 2393, 2415, 2424, 2496, 2537, 2565, 2623, 2704, 2872, 2979];
const sanitaPrivPC = [923, 470, 449, 471, 723, 438, 568, 548, 1099, 874, 902, 694, 847, 866, 909, 525, 605, 788, 734, 880];
const sanitaPubMln = [12725.6, 12452.2, 4098.2, 10729.4, 3342.1, 1199.2, 2911.0, 8896.9, 23671.6, 10098.9, 11622.1, 2054.6, 8870.8, 3773.3, 11359.1, 733.5, 4077.5, 3227.7, 352.0, 3249.8];
const sanitaPrivMln = [5270.0, 2620.0, 820.0, 2250.0, 1070.0, 230.0, 720.0, 2120.0, 11060.0, 3720.0, 4380.0, 590.0, 3100.0, 1310.0, 4070.0, 150.0, 940.0, 940.0, 90.0, 960.0];
const sanitaColori = ["#e34948", "#e34948", "#e34948", "#e34948", "#2a78d6", "#2a78d6", "#e34948", "#e34948", "#2a78d6", "#2a78d6", "#2a78d6", "#2a78d6", "#2a78d6", "#2a78d6", "#2a78d6", "#e34948", "#eda100", "#eda100", "#eda100", "#eda100"];

  // ── GRAFICO: Spesa pubblica pro capite per regione ──
  (function() {
    const ctx = document.getElementById('sanitaPubRegioneChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: sanitaRegioni,
        datasets: [{
          label: 'Spesa pubblica pro capite',
          data: sanitaPubPC,
          backgroundColor: sanitaColori,
          borderRadius: 3
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: {
            label: ctx => ` ${ctx.parsed.x.toLocaleString('it-IT')} €/persona`,
            afterLabel: ctx => ` Spesa totale: ${sanitaPubMln[ctx.dataIndex].toLocaleString('it-IT')} mln €`
          }}
        },
        scales: {
          x: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + ' €' },
            title: { display: true, text: 'Spesa pro capite (€)', font: { size: 10 }, color: '#7a7a7a' } },
          y: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#0d0d0d' } }
        }
      }
    });
  })();

  // ── GRAFICO: Serie storica spesa pubblica nazionale ──
  (function() {
    const ctx = document.getElementById('sanitaStoriaChart').getContext('2d');
    const anni = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024];
    const valori = [111.1,112.5,114.3,115.7,116.9,123.3,126.9,130.3,132.9,139.4];
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: anni,
        datasets: [{
          label: 'Spesa sanitaria pubblica',
          data: valori,
          borderColor: '#1d4ed8', backgroundColor: 'rgba(29,78,216,0.08)',
          borderWidth: 2.5, pointRadius: 4, fill: true, tension: 0.3
        }]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: { label: ctx => ` ${ctx.parsed.y} mld €` } }
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#7a7a7a' } },
          y: { grid: { color: '#e0ddd4' }, min: 100, max: 150,
            ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + ' mld' } }
        }
      }
    });
  })();

  // ── GRAFICO: Spesa privata pro capite per regione ──
  (function() {
    const ctx = document.getElementById('sanitaPrivRegioneChart').getContext('2d');
    const ordinePriv = sanitaRegioni.map((r,i) => ({r, v: sanitaPrivPC[i], mln: sanitaPrivMln[i]})).sort((a,b) => a.v - b.v);
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ordinePriv.map(o => o.r),
        datasets: [{
          label: 'Spesa privata pro capite',
          data: ordinePriv.map(o => o.v),
          backgroundColor: '#c0392b',
          borderRadius: 3
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: {
            label: ctx => ` ${ctx.parsed.x.toLocaleString('it-IT')} €/persona`,
            afterLabel: ctx => ` Spesa totale: ${ordinePriv[ctx.dataIndex].mln.toLocaleString('it-IT')} mln €`
          }}
        },
        scales: {
          x: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + ' €' },
            title: { display: true, text: 'Spesa pro capite (€)', font: { size: 10 }, color: '#7a7a7a' } },
          y: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#0d0d0d' } }
        }
      }
    });
  })();

  // ── GRAFICO: Serie storica spesa privata nazionale ──
  (function() {
    const ctx = document.getElementById('sanitaPrivStoriaChart').getContext('2d');
    const anni = [2016,2017,2018,2019,2020,2021,2022,2023,2024];
    const valori = [28.13,30.48,32.29,34.85,30.79,37.16,40.26,43.10,46.41];
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: anni,
        datasets: [{
          label: 'Spesa sanitaria privata',
          data: valori,
          borderColor: '#c0392b', backgroundColor: 'rgba(192,57,43,0.08)',
          borderWidth: 2.5, pointRadius: 4, fill: true, tension: 0.3
        }]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: { label: ctx => ` ${ctx.parsed.y} mld €` } }
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#7a7a7a' } },
          y: { grid: { color: '#e0ddd4' }, min: 20, max: 50,
            ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + ' mld' } }
        }
      }
    });
  })();
});
</script>
