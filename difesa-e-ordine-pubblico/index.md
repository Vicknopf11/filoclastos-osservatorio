---
layout: default
title: "Difesa e ordine pubblico — spesa per Missione e personale per corpo"
description: "Approfondimento sulla spesa italiana per difesa, forze dell'ordine e soccorso pubblico: bilanci di Ministero della Difesa e Ministero dell'Interno, personale per corpo, con fonti sempre citate."
---
<div class="prose">
<span class="prose__kicker">Approfondimento</span>
<h1>Difesa e ordine pubblico</h1>
<p>
  Quinta voce di spesa pubblica dopo pensioni, sanità, Pubblica Amministrazione e
  istruzione: qui la spesa italiana per difesa, forze dell'ordine e soccorso
  pubblico, scomposta dai bilanci di due ministeri — Difesa e Interno — che
  insieme coprono la gran parte, ma non la totalità, di questa voce. Il
  confronto europeo e altre dimensioni previste per questa pagina sono ancora
  in fase di raccolta dati e sono segnalate esplicitamente più sotto, senza
  valori inventati nel frattempo.
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
    <a href="#dop-missione">Spesa per Missione</a>
    <div class="nav-group" id="approfondimentiGroup">
      <button class="nav-group__toggle" aria-haspopup="true" aria-expanded="false">Altre sezioni <span class="nav-caret">▾</span></button>
      <div class="nav-group__menu">
        <a href="#dop-personale">Personale per corpo</a>
        <a href="#dop-limiti">Dimensioni da completare</a>
      </div>
    </div>
    <a href="{{ '/spesa-pubblica/' | relative_url }}">← Panoramica generale</a>
  </div>
  <div class="nav-tag">Dati fermi al bilancio 2025-2027</div>
</nav>

<main class="ita-spende__main">

<!-- SEZIONE 1: SPESA PER MISSIONE -->
<section class="section" id="dop-missione">
  <div class="section-header">
    <span class="section-num">01 /</span>
    <h2 class="section-title">Spesa per Missione e Programma</h2>
  </div>
  <p class="section-desc">La spesa per difesa, ordine pubblico e soccorso pubblico non sta in un solo bilancio: il <strong>Ministero della Difesa</strong> copre le Forze Armate e l'Arma dei Carabinieri come corpo, il <strong>Ministero dell'Interno</strong> copre la Polizia di Stato, il Corpo Nazionale dei Vigili del Fuoco e un contributo aggiuntivo ai Carabinieri, e il <strong>Ministero dell'Economia e delle Finanze</strong> copre la Guardia di Finanza — oltre a una voce meno ovvia, i servizi di intelligence.</p>

  <div class="insight" style="margin-top:0; margin-bottom:1.5rem; border-color: var(--is-ink-3);">
    <strong>Attenzione alla numerazione delle Missioni:</strong> ciascun ministero ha una propria numerazione interna delle Missioni, indipendente dagli altri — non è la stessa sequenza continuata, e lo stesso numero può significare cose diverse. Qui sotto vedrai la <strong>Missione 1</strong> della Difesa, le <strong>Missioni 3 e 4</strong> dell'Interno, e la <strong>Missione 5</strong> del MEF — che non ha nulla a che fare con la Missione 5 dell'Interno ("Immigrazione, accoglienza e garanzia dei diritti"), pur avendo lo stesso numero. Le Missioni 2 di Difesa e Interno esistono ma sono state escluse perché fuori tema (per la Difesa è "Sviluppo sostenibile e tutela del territorio", i Carabinieri forestali; per l'Interno è "Relazioni finanziarie con le autonomie territoriali", i trasferimenti a Comuni e Regioni). Non è un dato mancante: è stata una scelta editoriale.
  </div>

  <div class="cards-grid" style="margin-bottom:1.5rem;">
    <div class="stat-card">
      <div class="stat-card-label">Difesa (Min. Difesa, Missione 1)</div>
      <div class="stat-card-val">29,50 mld €</div>
      <div class="stat-card-sub">Forze Armate + Carabinieri</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Ordine pubblico (Min. Interno, Missione 3)</div>
      <div class="stat-card-val">9,00 mld €</div>
      <div class="stat-card-sub">Polizia di Stato + coordinamento</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Soccorso pubblico (Min. Interno, Missione 4)</div>
      <div class="stat-card-val">2,99 mld €</div>
      <div class="stat-card-sub">quasi tutto Vigili del Fuoco</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Ordine pubblico (MEF, Missione 5)</div>
      <div class="stat-card-val">3,12 mld €</div>
      <div class="stat-card-sub">Guardia di Finanza + intelligence</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Totale nei tre bilanci</div>
      <div class="stat-card-val">44,60 mld €</div>
      <div class="stat-card-sub">CP 2025, esclude Polizia Penitenziaria (v. limiti)</div>
    </div>
  </div>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Ministero della Difesa — Missione "Difesa e sicurezza del territorio" per Programma, CP 2025 (mld €)</div>
    <span class="source-tag static"><span class="source-dot"></span>Ministero della Difesa — Nota Integrativa al disegno di Legge di Bilancio 2025-2027</span>
    <div class="canvas-wrap" style="height:340px;">
      <canvas id="dopDifesaChart" role="img" aria-label="Spesa Missione Difesa per programma, competenza 2025: Approntamento e impiego Carabinieri 7,35 miliardi, Pianificazione generale delle Forze Armate e approvvigionamenti 7,11 miliardi, Approntamento e impiego forze terrestri (Esercito) 5,95 miliardi, Approntamento e impiego forze aeree (Aeronautica) 2,87 miliardi, Pianificazione ammodernamento armamenti e ricerca 2,60 miliardi, Approntamento e impiego forze marittime (Marina) 2,31 miliardi, Approntamento e impiego Comandi ed Enti interforze 1,31 miliardi.">Spesa Difesa per programma, competenza 2025.</canvas>
    </div>
  </div>

  <div style="overflow-x:auto; margin-bottom:1.5rem;">
    <table class="data-table">
      <thead>
        <tr>
          <th>Programma (Ministero della Difesa)</th>
          <th class="num">CP 2025 (€)</th>
          <th class="num">% Missione</th>
        </tr>
      </thead>
      <tbody>
        <tr class="ita">
          <td>1.1 — Approntamento e impiego Carabinieri</td>
          <td class="num">7.349.170.827</td>
          <td class="num">24,9%</td>
        </tr>
        <tr>
          <td>1.5 — Pianificazione generale Forze Armate e approvvigionamenti</td>
          <td class="num">7.108.886.746</td>
          <td class="num">24,1%</td>
        </tr>
        <tr>
          <td>1.2 — Approntamento e impiego forze terrestri (Esercito)</td>
          <td class="num">5.950.803.516</td>
          <td class="num">20,2%</td>
        </tr>
        <tr>
          <td>1.4 — Approntamento e impiego forze aeree (Aeronautica)</td>
          <td class="num">2.873.841.012</td>
          <td class="num">9,7%</td>
        </tr>
        <tr>
          <td>1.10 — Pianificazione ammodernamento armamenti e ricerca</td>
          <td class="num">2.602.910.887</td>
          <td class="num">8,8%</td>
        </tr>
        <tr>
          <td>1.3 — Approntamento e impiego forze marittime (Marina)</td>
          <td class="num">2.306.490.471</td>
          <td class="num">7,8%</td>
        </tr>
        <tr>
          <td>1.9 — Approntamento e impiego Comandi ed Enti interforze</td>
          <td class="num">1.305.922.599</td>
          <td class="num">4,4%</td>
        </tr>
        <tr>
          <td><strong>Totale Missione 1 — Difesa e sicurezza del territorio</strong></td>
          <td class="num"><strong>29.498.026.058</strong></td>
          <td class="num"><strong>100%</strong></td>
        </tr>
        <tr>
          <td>Totale Ministero della Difesa <span style="font-size:11px;color:var(--is-ink-3);">(incl. tutela ambientale e servizi generali)</span></td>
          <td class="num">31.298.400.926</td>
          <td class="num">—</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="insight">
    <strong>Carabinieri ed Esercito, non l'aeronautica o la marina, sono le voci più grandi:</strong> il solo "Approntamento e impiego Carabinieri" (24,9%) supera ogni singola Forza Armata, incluso l'Esercito (20,2%). La voce "Pianificazione generale e approvvigionamenti" (24,1%) è quasi altrettanto grande, ma è una voce trasversale — copre logistica, personale comune e approvvigionamenti non attribuiti a una singola Forza — quindi non è possibile, con questo solo dato, calcolare un "costo totale" pulito per Esercito, Marina o Aeronautica: la spesa realmente attribuibile a ciascuna Forza è più alta di quanto mostrato nella sola voce di "approntamento e impiego" dedicata.
  </div>

  <div class="chart-wrap" style="margin-top:2rem; margin-bottom:1.5rem;">
    <div class="chart-title">Ministero dell'Interno — Ordine pubblico e soccorso pubblico per Programma, CP 2025 (mln €)</div>
    <span class="source-tag static"><span class="source-dot"></span>Ministero dell'Interno — Nota Integrativa al disegno di Legge di Bilancio 2025-2027</span>
    <div class="canvas-wrap" style="height:300px;">
      <canvas id="dopInternoChart" role="img" aria-label="Spesa Interno per programma, competenza 2025: Contrasto al crimine e Polizia di Stato 7.753 milioni, Prevenzione dal rischio e soccorso pubblico (Vigili del Fuoco) 2.978 milioni, Pianificazione e coordinamento Forze di polizia 753 milioni, Servizio Arma dei Carabinieri per ordine pubblico 490 milioni.">Spesa Interno per programma, competenza 2025.</canvas>
    </div>
  </div>

  <div style="overflow-x:auto; margin-bottom:1.5rem;">
    <table class="data-table">
      <thead>
        <tr>
          <th>Programma (Ministero dell'Interno)</th>
          <th class="num">CP 2025 (€)</th>
          <th class="num">Missione</th>
        </tr>
      </thead>
      <tbody>
        <tr class="ita">
          <td>3.1 — Contrasto al crimine, tutela dell'ordine e sicurezza pubblica (Polizia di Stato)</td>
          <td class="num">7.752.941.692</td>
          <td class="num">Ordine pubblico</td>
        </tr>
        <tr>
          <td>4.2 — Prevenzione dal rischio e soccorso pubblico (Vigili del Fuoco)</td>
          <td class="num">2.977.997.080</td>
          <td class="num">Soccorso civile</td>
        </tr>
        <tr>
          <td>3.3 — Pianificazione e coordinamento Forze di polizia</td>
          <td class="num">752.802.304</td>
          <td class="num">Ordine pubblico</td>
        </tr>
        <tr>
          <td>3.2 — Servizio permanente Arma dei Carabinieri per l'ordine pubblico</td>
          <td class="num">490.076.124</td>
          <td class="num">Ordine pubblico</td>
        </tr>
        <tr>
          <td>4.1 — Gestione del sistema nazionale di difesa civile</td>
          <td class="num">7.574.878</td>
          <td class="num">Soccorso civile</td>
        </tr>
        <tr>
          <td><strong>Totale Missione 3 — Ordine pubblico e sicurezza</strong></td>
          <td class="num"><strong>8.995.820.120</strong></td>
          <td class="num">—</td>
        </tr>
        <tr>
          <td><strong>Totale Missione 4 — Soccorso civile</strong></td>
          <td class="num"><strong>2.985.571.958</strong></td>
          <td class="num">—</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="insight">
    <strong>L'Arma dei Carabinieri è finanziata da due bilanci diversi, per due funzioni diverse:</strong> il grosso del suo bilancio (7,35 mld €) sta nella Missione Difesa come corpo militare a tutti gli effetti (organicamente è la quarta Forza Armata). Ma il Ministero dell'Interno versa un contributo aggiuntivo (490 milioni, Programma 3.2) specificamente per il "servizio permanente" di ordine pubblico che i Carabinieri svolgono sul territorio — riconoscendo che il loro lavoro quotidiano è in gran parte sovrapponibile a quello della Polizia di Stato. Il Corpo Nazionale dei Vigili del Fuoco, da solo, assorbe il 99,7% della Missione "Soccorso civile" — la voce "difesa civile" (coordinamento, pianificazione) pesa appena lo 0,25%.
  </div>

  <div class="chart-wrap" style="margin-top:2rem; margin-bottom:1.5rem;">
    <div class="chart-title">Ministero dell'Economia e delle Finanze — Missione "Ordine pubblico e sicurezza" per Programma, CP 2025 (mln €)</div>
    <span class="source-tag static"><span class="source-dot"></span>MEF — Nota Integrativa a Legge di Bilancio 2025-2027</span>
    <div class="canvas-wrap" style="height:240px;">
      <canvas id="dopMefChart" role="img" aria-label="Spesa MEF Missione Ordine pubblico per programma, competenza 2025: Guardia di Finanza 1.734 milioni, Sicurezza democratica (servizi di intelligence) 1.385 milioni.">Spesa MEF per programma, competenza 2025.</canvas>
    </div>
  </div>

  <div style="overflow-x:auto; margin-bottom:1.5rem;">
    <table class="data-table">
      <thead>
        <tr>
          <th>Programma (Ministero dell'Economia e delle Finanze)</th>
          <th class="num">CP 2025 (€)</th>
          <th class="num">% Missione</th>
        </tr>
      </thead>
      <tbody>
        <tr class="ita">
          <td>5.1 — Concorso della Guardia di Finanza alla sicurezza interna ed esterna</td>
          <td class="num">1.734.284.767</td>
          <td class="num">55,6%</td>
        </tr>
        <tr>
          <td>5.2 — Sicurezza democratica <span style="font-size:11px;color:var(--is-ink-3);">(sistema di informazione per la sicurezza della Repubblica)</span></td>
          <td class="num">1.384.944.299</td>
          <td class="num">44,4%</td>
        </tr>
        <tr>
          <td><strong>Totale Missione 5 — Ordine pubblico e sicurezza (MEF)</strong></td>
          <td class="num"><strong>3.119.229.066</strong></td>
          <td class="num"><strong>100%</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="insight">
    <strong>Il bilancio dei servizi segreti italiani sta, contabilmente, dentro "Ordine pubblico e sicurezza" del MEF, non dentro un bilancio dedicato all'intelligence.</strong> Il Programma 5.2 "Sicurezza democratica" — che copre il "sistema di informazione per la sicurezza della Repubblica" (AISE, AISI e il coordinamento del DIS) — vale 1,38 miliardi di euro, quasi tanto quanto la Guardia di Finanza (1,73 miliardi) nella stessa Missione. È una collocazione poco intuitiva ma spiegabile: il finanziamento dei servizi segreti passa storicamente dalla Presidenza del Consiglio tramite il MEF, non da un dicastero della sicurezza in senso stretto.
  </div>
  <div class="insight" style="margin-top:1rem; border-color: var(--is-ink-3);">
    <strong>Nota metodologica e limite dichiarato:</strong> questa pagina copre Ministero della Difesa, Ministero dell'Interno e Ministero dell'Economia e delle Finanze. Resta fuori un solo corpo con funzioni di ordine pubblico: la <strong>Polizia Penitenziaria</strong> (Ministero della Giustizia), non ancora coperta da una Nota Integrativa caricata in questa sessione. Il totale di 44,60 miliardi € qui presentato è quindi ancora un sottoinsieme, non il totale della funzione COFOG "Difesa e ordine pubblico" nella sua interezza (il riferimento statico usato nella <a href="{{ '/spesa-pubblica/' | relative_url }}">panoramica generale</a>, circa 55 miliardi, include probabilmente anche la Polizia Penitenziaria e altre voci minori).
  </div>
</section>

<!-- SEZIONE 2: PERSONALE PER CORPO -->
<section class="section" id="dop-personale">
  <div class="section-header">
    <span class="section-num">02 /</span>
    <h2 class="section-title">Personale per corpo</h2>
  </div>
  <p class="section-desc">Dati sul personale a tempo indeterminato al 31 dicembre 2024, dallo stesso Conto Annuale RGS già usato per la pagina <a href="{{ '/pubblica-amministrazione/' | relative_url }}">Pubblica Amministrazione</a>. A questo livello di aggregazione i tre corpi non sono ulteriormente scomposti per singola Forza Armata o singolo corpo di polizia — la scomposizione fine (Esercito/Marina/Aeronautica separati, Polizia di Stato/Carabinieri/Guardia di Finanza separati) richiede una tabella più granulare del Conto Annuale, non ancora caricata.</p>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Personale per corpo — Anno 2024</div>
    <span class="source-tag static"><span class="source-dot"></span>RGS — Conto Annuale 2024, dati aperti (tabella OCCUPAZIONE)</span>
    <div class="canvas-wrap" style="height:280px;">
      <canvas id="dopPersonaleChart" role="img" aria-label="Personale 2024 per corpo: Corpi di polizia 302.695 dipendenti, Forze armate 173.747, Vigili del fuoco 36.299.">Personale per corpo, 2024.</canvas>
    </div>
  </div>

  <div style="overflow-x:auto; margin-bottom:1.5rem;">
    <table class="data-table">
      <thead>
        <tr>
          <th>Corpo</th>
          <th class="num">Dipendenti</th>
          <th class="num">Costo del lavoro (mld €)</th>
          <th class="num">Costo medio annuo (€)</th>
        </tr>
      </thead>
      <tbody>
        <tr class="ita">
          <td>Corpi di polizia</td>
          <td class="num">302.695</td>
          <td class="num">19,17</td>
          <td class="num">63.343</td>
        </tr>
        <tr>
          <td>Forze armate</td>
          <td class="num">173.747</td>
          <td class="num">10,98</td>
          <td class="num">63.173</td>
        </tr>
        <tr>
          <td>Vigili del fuoco</td>
          <td class="num">36.299</td>
          <td class="num">2,14</td>
          <td class="num">58.925</td>
        </tr>
        <tr>
          <td><strong>Totale</strong></td>
          <td class="num"><strong>512.741</strong></td>
          <td class="num"><strong>32,29</strong></td>
          <td class="num"><strong>62.984</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="insight">
    <strong>Il costo del lavoro dei "Corpi di polizia" (19,17 mld €) è più del doppio dell'intera Missione "Ordine pubblico" del Ministero dell'Interno (9,0 mld €, sezione 01).</strong> Non è un errore: la categoria "Corpi di polizia" del Conto Annuale RGS è più ampia di quanto coperto dal solo bilancio dell'Interno — include verosimilmente anche il personale della Guardia di Finanza e della Polizia Penitenziaria, i due corpi segnalati come mancanti nella sezione 01. È un promemoria concreto di quanto la spesa "sicurezza" sia distribuita su più ministeri: guardare un solo bilancio sottostima sistematicamente il costo complessivo delle forze dell'ordine.
  </div>
</section>

<!-- SEZIONE: DIMENSIONI DA COMPLETARE -->
<section class="section" id="dop-limiti" style="border-bottom:none;">
  <div class="section-header">
    <span class="section-num">— /</span>
    <h2 class="section-title">Dimensioni ancora da completare</h2>
  </div>
  <p class="section-desc">Per completezza, quanto previsto per questa pagina ma non ancora popolato con dati verificati:</p>
  <div class="insight" style="border-color: var(--is-ink-3);">
    <strong>Confronto europeo:</strong> serve estendere <code>scripts/fetch_eurostat.py</code> con le categorie COFOG GF02 (Difesa) e GF03 (Ordine pubblico e sicurezza) — stessa architettura già usata per l'istruzione (GF09) — più un confronto con il target NATO del 2% del PIL, che richiederebbe il report ufficiale NATO "Defence Expenditure of NATO Countries" (non raggiungibile dalla rete di questo ambiente: va caricato).
  </div>
  <div class="insight" style="border-color: var(--is-ink-3);">
    <strong>Polizia Penitenziaria:</strong> serve la Nota Integrativa del Ministero della Giustizia per completare il quadro dei corpi con funzioni di ordine pubblico.
  </div>
  <div class="insight" style="margin-top:1rem; border-color: var(--is-ink-3);">
    <strong>Personale per singola Forza/corpo:</strong> la sezione 02 mostra solo gli aggregati "Forze armate" e "Corpi di polizia" — una tabella più granulare del Conto Annuale RGS permetterebbe di scomporre in Esercito/Marina/Aeronautica/Carabinieri e Polizia di Stato/Guardia di Finanza separatamente.
  </div>
</section>

</main>

</div>

<footer class="pens-footer">
  <div style="max-width:980px; margin:0 auto;">
    Fonti: Ministero della Difesa — Nota Integrativa al disegno di Legge di Bilancio 2025-2027; Ministero dell'Interno — Nota Integrativa al disegno di Legge di Bilancio 2025-2027; Ministero dell'Economia e delle Finanze — Nota Integrativa a Legge di Bilancio 2025-2027; RGS — Conto Annuale 2024.<br>
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

  .ita-spende .insight {
    border-left: 3px solid var(--is-red);
    padding: 1rem 1.25rem;
    background: #fff;
    margin-top: 1.5rem;
    font-size: 13px; line-height: 1.7;
    color: var(--is-ink-2);
  }
  .ita-spende .insight strong { color: var(--is-ink); }


  .ita-spende .source-tag {
    display: inline-flex; align-items: center; gap: 5px;
    font-family: var(--is-font-mono);
    font-size: 10px; padding: 3px 8px;
    border-radius: 2px; margin-bottom: 0.75rem;
  }
  .ita-spende .source-tag.static { background: var(--is-paper-3); color: var(--is-ink-3); }
  .ita-spende .source-dot { width: 6px; height: 6px; border-radius: 50%; background: currentColor; }

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

  // Dropdown "Altre sezioni"
  document.querySelectorAll('.nav-group__toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const group = btn.closest('.nav-group');
      const isOpen = group.classList.toggle('open');
      btn.setAttribute('aria-expanded', isOpen);
    });
  });
  document.addEventListener('click', (e) => {
    document.querySelectorAll('.nav-group.open').forEach(g => {
      if (!g.contains(e.target)) g.classList.remove('open');
    });
  });

  // ── GRAFICO: Ministero della Difesa per Programma ──
  (function() {
    const ctx = document.getElementById('dopDifesaChart').getContext('2d');
    const dati = [
      {p:'1.9 — Comandi ed Enti interforze', v:1.31},
      {p:'1.3 — Forze marittime (Marina)', v:2.31},
      {p:'1.10 — Ammodernamento armamenti e ricerca', v:2.60},
      {p:'1.4 — Forze aeree (Aeronautica)', v:2.87},
      {p:'1.2 — Forze terrestri (Esercito)', v:5.95},
      {p:'1.5 — Pianificazione generale e approvvigionamenti', v:7.11},
      {p:'1.1 — Carabinieri', v:7.35}
    ];
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: dati.map(d => d.p),
        datasets: [{
          label: 'Miliardi €',
          data: dati.map(d => d.v),
          backgroundColor: '#2a78d6',
          borderRadius: 3
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: { label: ctx => ` ${ctx.parsed.x.toFixed(2)} mld €` } }
        },
        scales: {
          x: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + ' mld' },
            title: { display: true, text: 'Miliardi €', font: { size: 10 }, color: '#7a7a7a' } },
          y: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#0d0d0d' } }
        }
      }
    });
  })();

  // ── GRAFICO: Ministero dell'Interno per Programma (ordine pubblico + soccorso) ──
  (function() {
    const ctx = document.getElementById('dopInternoChart').getContext('2d');
    const dati = [
      {p:'3.2 — Carabinieri (contributo ordine pubblico)', v:490.1},
      {p:'3.3 — Pianificazione/coordinamento forze polizia', v:752.8},
      {p:'4.2 — Vigili del Fuoco', v:2978.0},
      {p:'3.1 — Polizia di Stato', v:7752.9}
    ];
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: dati.map(d => d.p),
        datasets: [{
          label: 'Milioni €',
          data: dati.map(d => d.v),
          backgroundColor: dati.map(d => d.p.startsWith('3') ? '#c0392b' : '#1baf7a'),
          borderRadius: 3
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: { label: ctx => ` ${ctx.parsed.x.toLocaleString('it-IT')} mln €` } }
        },
        scales: {
          x: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v.toLocaleString('it-IT') + ' mln' },
            title: { display: true, text: 'Milioni €', font: { size: 10 }, color: '#7a7a7a' } },
          y: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#0d0d0d' } }
        }
      }
    });
  })();

  // ── GRAFICO: MEF per Programma (ordine pubblico) ──
  (function() {
    const ctx = document.getElementById('dopMefChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['5.2 — Sicurezza democratica\n(intelligence)', '5.1 — Guardia di Finanza'],
        datasets: [{
          label: 'Milioni €',
          data: [1384.9, 1734.3],
          backgroundColor: '#2a78d6',
          borderRadius: 3
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: { label: ctx => ` ${ctx.parsed.x.toLocaleString('it-IT')} mln €` } }
        },
        scales: {
          x: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v.toLocaleString('it-IT') + ' mln' },
            title: { display: true, text: 'Milioni €', font: { size: 10 }, color: '#7a7a7a' } },
          y: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#0d0d0d' } }
        }
      }
    });
  })();

  // ── GRAFICO: Personale per corpo ──
  (function() {
    const ctx = document.getElementById('dopPersonaleChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Corpi di polizia', 'Forze armate', 'Vigili del fuoco'],
        datasets: [{
          label: 'Dipendenti',
          data: [302695, 173747, 36299],
          backgroundColor: '#2a78d6',
          borderRadius: 3
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: { label: ctx => ` ${ctx.parsed.x.toLocaleString('it-IT')} dipendenti` } }
        },
        scales: {
          x: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => (v/1000) + 'k' },
            title: { display: true, text: 'Dipendenti', font: { size: 10 }, color: '#7a7a7a' } },
          y: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#0d0d0d' } }
        }
      }
    });
  })();
});
</script>
