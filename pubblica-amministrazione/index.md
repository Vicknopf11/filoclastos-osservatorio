---
layout: default
title: "Pubblica Amministrazione — entrate, uscite e saldo per livello di governo"
description: "Approfondimento sulla Pubblica Amministrazione italiana: confronto tra Amministrazioni centrali, locali ed Enti di previdenza su entrate, uscite e saldo di bilancio, con fonti ISTAT sempre citate."
---
<div class="prose">
<span class="prose__kicker">Approfondimento</span>
<h1>Pubblica Amministrazione — per livello di governo</h1>
<p>
  Terza voce di spesa pubblica dopo pensioni e sanità: qui la Pubblica Amministrazione
  italiana scomposta nei tre sottosettori SEC 2010 — Amministrazioni centrali (Stato),
  Amministrazioni locali (Regioni, Comuni, Città metropolitane) ed Enti di previdenza —
  con entrate, uscite e saldo di bilancio per ciascuno.
  Fonte: ISTAT — Conto economico delle Amministrazioni pubbliche per sottosettore,
  edizione aprile 2026.
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
    <a href="#pa-sottosettori">Per livello di governo</a>
    <a href="#pa-saldo">Saldo nazionale</a>
    <a href="#pa-dipendenti">Dipendenti per comparto</a>
    <a href="{{ '/spesa-pubblica/' | relative_url }}">← Panoramica generale</a>
  </div>
</nav>

<main class="ita-spende__main">

<!-- SEZIONE 1: PER LIVELLO DI GOVERNO -->
<section class="section" id="pa-sottosettori">
  <div class="section-header">
    <span class="section-num">01 /</span>
    <h2 class="section-title">Entrate, uscite e saldo per livello di governo</h2>
  </div>
  <p class="section-desc">Il Conto economico delle Amministrazioni pubbliche secondo il SEC 2010 (Sistema Europeo dei Conti) scompone la PA in tre sottosettori: <strong>Amministrazioni centrali</strong> (Stato, ministeri, agenzie fiscali, enti centrali), <strong>Amministrazioni locali</strong> (Regioni, Comuni, Città metropolitane, Camere di Commercio, Università pubbliche) ed <strong>Enti di previdenza</strong> (INPS e altri enti nazionali di previdenza e assistenza).</p>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Entrate e uscite per sottosettore — Anno 2025 (mld €)</div>
    <span class="source-tag static"><span class="source-dot"></span>ISTAT — Conto economico delle AP per sottosettore, ed. aprile 2026</span>
    <div style="display:flex;flex-wrap:wrap;gap:12px;margin:0.75rem 0;font-size:11px;color:var(--is-ink-3);">
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#2a78d6;display:inline-block;"></span>Entrate totali</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#e34948;display:inline-block;"></span>Uscite totali</span>
    </div>
    <div class="canvas-wrap" style="height:320px;">
      <canvas id="paSottosettoriChart" role="img" aria-label="Entrate e uscite 2025 per sottosettore: Amministrazioni centrali 651,6 miliardi di entrate contro 731,1 di uscite; Amministrazioni locali 330,5 contro 330,3; Enti di previdenza 466,9 contro 456,9.">Entrate e uscite per sottosettore PA, 2025.</canvas>
    </div>
  </div>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Saldo (Accreditamento/indebitamento netto) per sottosettore — 2023-2025 (mld €)</div>
    <span class="source-tag static"><span class="source-dot"></span>ISTAT — Conto economico delle AP per sottosettore, ed. aprile 2026</span>
    <div class="canvas-wrap" style="height:280px;">
      <canvas id="paSaldoSottosettoriChart" role="img" aria-label="Saldo per sottosettore 2023-2025. Amministrazioni centrali sempre in deficit: -163,5, -85,0, -79,5 miliardi. Amministrazioni locali quasi in pareggio: +6,0, +2,2, +0,2. Enti di previdenza in surplus crescente: +4,7, +9,1, +9,9.">Saldo per sottosettore PA, 2023-2025.</canvas>
    </div>
  </div>

  <div style="overflow-x:auto; margin-bottom:1.5rem;">
    <table class="data-table">
      <thead>
        <tr>
          <th>Sottosettore</th>
          <th class="num">Entrate 2025 (mld €)</th>
          <th class="num">Uscite 2025 (mld €)</th>
          <th class="num">Saldo 2025 (mld €)</th>
          <th class="num">Saldo 2024 (mld €)</th>
          <th class="num">Saldo 2023 (mld €)</th>
        </tr>
      </thead>
      <tbody>
        <tr class="ita">
          <td>Amministrazioni centrali</td>
          <td class="num">651,6</td>
          <td class="num">731,1</td>
          <td class="num" style="color:var(--red)">-79,5</td>
          <td class="num" style="color:var(--red)">-85,0</td>
          <td class="num" style="color:var(--red)">-163,5</td>
        </tr>
        <tr>
          <td>Amministrazioni locali</td>
          <td class="num">330,5</td>
          <td class="num">330,3</td>
          <td class="num">+0,2</td>
          <td class="num">+2,2</td>
          <td class="num">+6,0</td>
        </tr>
        <tr>
          <td>Enti di previdenza</td>
          <td class="num">466,9</td>
          <td class="num">456,9</td>
          <td class="num">+9,9</td>
          <td class="num">+9,1</td>
          <td class="num">+4,7</td>
        </tr>
        <tr>
          <td><strong>Totale PA (consolidato)</strong></td>
          <td class="num"><strong>1.085,9</strong></td>
          <td class="num"><strong>1.155,3</strong></td>
          <td class="num" style="color:var(--red)"><strong>-69,4</strong></td>
          <td class="num" style="color:var(--red)"><strong>-73,8</strong></td>
          <td class="num" style="color:var(--red)"><strong>-152,9</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="insight">
    <strong>Il deficit pubblico italiano è quasi tutto Stato centrale:</strong> le Amministrazioni centrali sono l'unico sottosettore strutturalmente in deficit, e per importi molto ampi (-79,5 miliardi nel 2025). Le Amministrazioni locali (Regioni, Comuni) sono da anni vicine al pareggio di bilancio — un vincolo di fatto imposto dalle regole di finanza pubblica sugli enti territoriali. Gli Enti di previdenza (INPS) sono addirittura in <strong>surplus crescente</strong> (+9,9 miliardi nel 2025): le entrate contributive superano le uscite per prestazioni, un dato che sorprende rispetto alla narrazione comune sul sistema pensionistico "in perdita" — il deficit previdenziale di cui si parla di solito riguarda la GIAS (finanziata da fiscalità generale, quindi contabilizzata tra le Amministrazioni centrali), non la gestione contributiva pura qui rappresentata.
  </div>
  <div class="insight" style="margin-top:1rem; border-color: var(--is-ink-3);">
    <strong>Nota metodologica:</strong> il totale consolidato della PA non è la somma dei tre sottosettori, perché elimina i trasferimenti tra un livello di governo e l'altro (es. i trasferimenti dello Stato a Regioni/Comuni o agli Enti di previdenza) — altrimenti questi flussi verrebbero contati due volte. Il dato consolidato è quello ufficiale fornito direttamente da ISTAT per "Amministrazioni pubbliche", non un calcolo derivato.
  </div>
</section>

<!-- SEZIONE 2: SALDO NAZIONALE -->
<section class="section" id="pa-saldo">
  <div class="section-header">
    <span class="section-num">02 /</span>
    <h2 class="section-title">Saldo nazionale e saldo primario</h2>
  </div>
  <p class="section-desc">Il saldo complessivo delle Amministrazioni pubbliche (l'"indebitamento netto" che compare nelle notifiche EDP europee) confrontato con il <strong>saldo primario</strong> — lo stesso saldo calcolato escludendo la spesa per interessi sul debito pubblico. La differenza tra i due mostra quanto del deficit italiano sia dovuto al costo del debito accumulato in passato, piuttosto che allo squilibrio tra entrate e spesa corrente di oggi.</p>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Saldo complessivo vs saldo primario — Italia, 2023-2025 (mld €)</div>
    <span class="source-tag static"><span class="source-dot"></span>ISTAT — Conto economico delle AP, ed. aprile 2026</span>
    <div style="display:flex;flex-wrap:wrap;gap:12px;margin:0.75rem 0;font-size:11px;color:var(--is-ink-3);">
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#e34948;display:inline-block;"></span>Accreditamento/indebitamento netto</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#2a78d6;display:inline-block;"></span>Saldo primario (netto interessi)</span>
    </div>
    <div class="canvas-wrap" style="height:300px;">
      <canvas id="paSaldoNazionaleChart" role="img" aria-label="Saldo pubblico italiano 2023-2025: indebitamento netto -152,9, -73,8, -69,4 miliardi. Saldo primario -75,1 miliardi nel 2023, poi in surplus: +11,7 nel 2024 e +17,8 nel 2025.">Saldo nazionale e saldo primario, 2023-2025.</canvas>
    </div>
  </div>

  <div class="insight">
    <strong>Il saldo primario è già positivo:</strong> dal 2024 l'Italia incassa più di quanto spende, se si escludono gli interessi sul debito pregresso (+11,7 miliardi nel 2024, +17,8 nel 2025). È l'onere del debito accumulato — non lo squilibrio tra entrate e spesa corrente — a mantenere il saldo complessivo in rosso. Il miglioramento tra 2023 e 2024 (da -75,1 a +11,7 miliardi di saldo primario, quasi 87 miliardi di differenza in un solo anno) è in parte dovuto al venir meno di misure straordinarie (superbonus, sostegni energia) che avevano gonfiato la spesa 2023.
  </div>
</section>

<!-- SEZIONE 3: DIPENDENTI PUBBLICI PER COMPARTO -->
<section class="section" id="pa-dipendenti">
  <div class="section-header">
    <span class="section-num">03 /</span>
    <h2 class="section-title">Numero e costo dei dipendenti pubblici per comparto</h2>
  </div>
  <p class="section-desc">Personale a tempo indeterminato e dirigenti in servizio al 31 dicembre 2024, per comparto di contrattazione. Esclude personale con contratti flessibili/a termine (rilevati separatamente dal Conto Annuale) e non è espresso in equivalenti a tempo pieno — chi lavora part-time è conteggiato come una unità di personale, non come frazione.</p>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Dipendenti pubblici per comparto — Anno 2024</div>
    <span class="source-tag static"><span class="source-dot"></span>RGS — Conto Annuale 2024, dati aperti (tabella OCCUPAZIONE)</span>
    <div class="canvas-wrap" style="height:340px;">
      <canvas id="paDipendentiChart" role="img" aria-label="Dipendenti pubblici 2024 per comparto: Scuola 1,25 milioni, Sanità 714 mila, Altro (forze dell'ordine, magistratura, ricerca) 606 mila, Enti locali 499 mila, Stato 211 mila, Università 104 mila.">Dipendenti pubblici per comparto, 2024.</canvas>
    </div>
  </div>

  <div style="overflow-x:auto; margin-bottom:1.5rem;">
    <table class="data-table">
      <thead>
        <tr>
          <th>Comparto</th>
          <th class="num">Dipendenti</th>
          <th class="num">Costo del lavoro (mld €)</th>
          <th class="num">Costo medio annuo (€)</th>
        </tr>
      </thead>
      <tbody>
        <tr class="ita">
          <td>Scuola</td>
          <td class="num">1.254.459</td>
          <td class="num">51,12</td>
          <td class="num">40.751</td>
        </tr>
        <tr>
          <td>Sanità</td>
          <td class="num">713.976</td>
          <td class="num">46,67</td>
          <td class="num">65.366</td>
        </tr>
        <tr>
          <td>Altro (forze dell'ordine, magistratura, ricerca, ecc.)</td>
          <td class="num">605.579</td>
          <td class="num">41,83</td>
          <td class="num">69.074</td>
        </tr>
        <tr>
          <td>Enti locali (Regioni, Comuni)</td>
          <td class="num">499.429</td>
          <td class="num">24,60</td>
          <td class="num">49.256</td>
        </tr>
        <tr>
          <td>Stato (Ministeri, agenzie fiscali)</td>
          <td class="num">211.236</td>
          <td class="num">13,27</td>
          <td class="num">62.821</td>
        </tr>
        <tr>
          <td>Università (docenti, ricercatori, amministrativo)</td>
          <td class="num">104.115</td>
          <td class="num">8,59</td>
          <td class="num">82.505</td>
        </tr>
        <tr>
          <td><strong>Totale</strong></td>
          <td class="num"><strong>3.388.794</strong></td>
          <td class="num"><strong>186,08</strong></td>
          <td class="num"><strong>54.911</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Dentro la voce "Altro" — scomposizione (Anno 2024)</div>
    <span class="source-tag static"><span class="source-dot"></span>RGS — Conto Annuale 2024, dati aperti (tabella OCCUPAZIONE)</span>
    <div class="canvas-wrap" style="height:280px;">
      <canvas id="paAltroChart" role="img" aria-label="Scomposizione della voce Altro: Corpi di polizia 302.695, Forze armate 173.747, Vigili del fuoco 36.299, Enti Lista S13 ISTAT 32.974, Enti di ricerca 24.604, Magistratura 11.224, altri enti e carriere minori 24.036.">Scomposizione della voce Altro, 2024.</canvas>
    </div>
  </div>

  <div style="overflow-x:auto; margin-bottom:1.5rem;">
    <table class="data-table">
      <thead>
        <tr>
          <th>Dentro "Altro"</th>
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
          <td>Enti Lista S13 ISTAT</td>
          <td class="num">32.974</td>
          <td class="num">2,62</td>
          <td class="num">79.327</td>
        </tr>
        <tr>
          <td>Enti di ricerca</td>
          <td class="num">24.604</td>
          <td class="num">2,08</td>
          <td class="num">84.733</td>
        </tr>
        <tr>
          <td>Magistratura</td>
          <td class="num">11.224</td>
          <td class="num">2,46</td>
          <td class="num">218.748</td>
        </tr>
        <tr>
          <td>Altri enti e carriere minori <span style="font-size:11px;color:var(--is-ink-3);">(AFAM, carriera diplomatica/prefettizia/penitenziaria, Autorità indipendenti, Presidenza Consiglio, enti art. 60, Unioncamere)</span></td>
          <td class="num">24.036</td>
          <td class="num">2,39</td>
          <td class="num">99.458</td>
        </tr>
        <tr>
          <td><strong>Totale "Altro"</strong></td>
          <td class="num"><strong>605.579</strong></td>
          <td class="num"><strong>41,83</strong></td>
          <td class="num"><strong>69.074</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="insight">
    <strong>Le forze dell'ordine sono la componente più grande:</strong> Corpi di polizia e Forze armate insieme (476.442 persone) rappresentano quasi l'80% della voce "Altro" — più della somma di Stato e Università messe insieme. La Magistratura è la categoria più piccola per numero (11.224 persone) ma con il costo medio annuo più alto di qualsiasi comparto in questa pagina (218.748 €), riflettendo una struttura salariale specifica per la carriera giudiziaria.
  </div>

  <div class="insight">
    <strong>La scuola è di gran lunga il comparto più numeroso</strong> (1,25 milioni di dipendenti, oltre un terzo del totale) ma con il costo medio annuo più basso (40.751 €) tra tutte le categorie — riflette una struttura di carriera piatta e un corpo docente numericamente enorme rispetto agli altri comparti. All'estremo opposto, l'università ha il costo medio più alto tra le cinque categorie richieste (82.505 €), spiegato dalla componente di docenti e ricercatori. La voce "Altro" (605 mila persone, che include forze dell'ordine, forze armate, magistratura e enti di ricerca) ha in realtà il costo medio più alto in assoluto tra tutte le sotto-categorie del Conto Annuale — la magistratura da sola supera 218.000 €/anno medio, ma pesa solo su 11 mila persone.
  </div>
  <div class="insight" style="margin-top:1rem; border-color: var(--is-ink-3);">
    <strong>Nota metodologica:</strong> "Università" qui aggrega due categorie contrattuali distinte nel Conto Annuale — il personale amministrativo (comparto "Istruzione e Ricerca") e i professori/ricercatori universitari (comparto "Personale in regime di diritto pubblico", stesso regime normativo di magistrati e militari) — perché dal punto di vista del lettore sono entrambi "l'università". "Stato" corrisponde al comparto ufficiale "Funzioni centrali" (Ministeri, agenzie fiscali, enti pubblici non economici centrali). Il dato non include il personale con contratti flessibili o a tempo determinato, rilevato a parte dal Conto Annuale.
  </div>
</section>

<!-- SEZIONE: DATI IN ARRIVO -->
<section class="section" id="pa-in-arrivo">
  <div class="section-header">
    <span class="section-num">— /</span>
    <h2 class="section-title">Sezioni ancora da completare</h2>
  </div>
  <p class="section-desc">Coerentemente con il principio di questo Osservatorio di non pubblicare mai dati stimati o inventati, le seguenti sezioni previste per questa pagina restano in attesa delle tavole sorgente e non sono ancora popolate:</p>
  <ul style="margin: 0 0 1rem 1.4rem; color: var(--is-ink-2); line-height: 1.9;">
    <li><strong>Confronto europeo</strong> — spesa per servizi generali della PA in percentuale del PIL (Eurostat gov_10a_exp, cofog99=GF01) e numero di dipendenti pubblici su popolazione attiva (OCSE "Government at a Glance")</li>
    <li><strong>Debito per livello di governo</strong> — scomposizione dello stock di debito pubblico (non solo il saldo annuale) tra Stato, enti locali ed enti di previdenza, fonte probabile: Banca d'Italia</li>
  </ul>
</section>

</main>

</div>

<footer class="pens-footer">
  <div style="max-width:980px; margin:0 auto;">
    Fonte: ISTAT — Conto economico delle Amministrazioni pubbliche per sottosettore (SEC 2010), edizione aprile 2026.<br>
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

  // ── GRAFICO: Entrate/uscite per sottosettore 2025 ──
  (function() {
    const ctx = document.getElementById('paSottosettoriChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Amministrazioni\ncentrali', 'Amministrazioni\nlocali', 'Enti di\nprevidenza'],
        datasets: [
          { label: 'Entrate', data: [651.6, 330.5, 466.9], backgroundColor: '#2a78d6', borderRadius: 3 },
          { label: 'Uscite', data: [731.1, 330.3, 456.9], backgroundColor: '#e34948', borderRadius: 3 }
        ]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: { label: ctx => ` ${ctx.dataset.label}: ${ctx.parsed.y} mld €` } }
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#7a7a7a' } },
          y: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + ' mld' } }
        }
      }
    });
  })();

  // ── GRAFICO: Saldo per sottosettore 2023-2025 ──
  (function() {
    const ctx = document.getElementById('paSaldoSottosettoriChart').getContext('2d');
    const anni = [2023, 2024, 2025];
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: anni,
        datasets: [
          { label: 'Amministrazioni centrali', data: [-163.5, -85.0, -79.5],
            borderColor: '#e34948', backgroundColor: 'transparent', borderWidth: 2.5, pointRadius: 4, tension: 0.2 },
          { label: 'Amministrazioni locali', data: [6.0, 2.2, 0.2],
            borderColor: '#2a78d6', backgroundColor: 'transparent', borderWidth: 2.5, pointRadius: 4, tension: 0.2 },
          { label: 'Enti di previdenza', data: [4.7, 9.1, 9.9],
            borderColor: '#008300', backgroundColor: 'transparent', borderWidth: 2.5, pointRadius: 4, tension: 0.2 }
        ]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: true, labels: { font: { size: 11, family: "'IBM Plex Mono', monospace" }, color: '#7a7a7a', boxWidth: 20 } },
          tooltip: { callbacks: { label: ctx => ` ${ctx.dataset.label}: ${ctx.parsed.y} mld €` } }
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 12 }, color: '#7a7a7a' } },
          y: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + ' mld' } }
        }
      }
    });
  })();

  // ── GRAFICO: Saldo nazionale vs saldo primario ──
  (function() {
    const ctx = document.getElementById('paSaldoNazionaleChart').getContext('2d');
    const anni = [2023, 2024, 2025];
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: anni,
        datasets: [
          { label: 'Indebitamento netto', data: [-152.9, -73.8, -69.4], backgroundColor: '#e34948', borderRadius: 3 },
          { label: 'Saldo primario', data: [-75.1, 11.7, 17.8], backgroundColor: '#2a78d6', borderRadius: 3 }
        ]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: true, labels: { font: { size: 11, family: "'IBM Plex Mono', monospace" }, color: '#7a7a7a', boxWidth: 20 } },
          tooltip: { callbacks: { label: ctx => ` ${ctx.dataset.label}: ${ctx.parsed.y} mld €` } }
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 12 }, color: '#7a7a7a' } },
          y: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + ' mld' } }
        }
      }
    });
  })();
  // ── GRAFICO: Scomposizione della voce Altro ──
  (function() {
    const ctx = document.getElementById('paAltroChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Corpi di\\npolizia', 'Forze\\narmate', 'Vigili del\\nfuoco', 'Enti Lista\\nS13 ISTAT', 'Enti di\\nricerca', 'Magistratura', 'Altri enti\\nminori'],
        datasets: [{
          label: 'Dipendenti',
          data: [302695, 173747, 36299, 32974, 24604, 11224, 24036],
          backgroundColor: '#c0392b',
          borderRadius: 3
        }]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: { label: ctx => ` ${ctx.parsed.y.toLocaleString('it-IT')} dipendenti` } }
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 10 }, color: '#7a7a7a' } },
          y: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => (v/1000) + 'k' } }
        }
      }
    });
  })();

  // ── GRAFICO: Dipendenti pubblici per comparto ──
  (function() {
    const ctx = document.getElementById('paDipendentiChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Scuola', 'Sanità', 'Altro', 'Enti locali', 'Stato', 'Università'],
        datasets: [{
          label: 'Dipendenti',
          data: [1254459, 713976, 605579, 499429, 211236, 104115],
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
          x: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => (v/1e6).toFixed(1) + 'M' },
            title: { display: true, text: 'Dipendenti', font: { size: 10 }, color: '#7a7a7a' } },
          y: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#0d0d0d' } }
        }
      }
    });
  })();
});
</script>
