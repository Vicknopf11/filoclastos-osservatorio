---
layout: default
title: "Titolo I — Della spesa pubblica"
---
<div class="prose">
<span class="prose__kicker">Titolo I</span>
<h1>Della spesa pubblica</h1>
<p>
  Bilanci, flussi e destinazione della finanza pubblica italiana, a confronto
  con i principali paesi dell'area euro. Il confronto europeo qui sotto legge
  dati scaricati da Eurostat periodicamente (una volta a settimana, via
  GitHub Actions) e pubblicati come file statico — non calcolati al momento
  della visita. Le altre voci (composizione della spesa italiana, sistema
  pensionistico, leggi di bilancio) sono dati di riferimento MEF/ISTAT/INPS,
  aggiornati manualmente. Metodo descritto per esteso nella
  <a href="{{ '/metodologia/' | relative_url }}">nota metodologica</a>.
</p>
</div>

<div class="ita-spende">

<nav>
  <div class="nav-brand">ITALIA<span>SPENDE</span></div>
  <div class="nav-links">
    <a href="#spesa">Spesa</a>
    <a href="#pensioni">Pensioni</a>
    <a href="#confronto">Europa</a>
    <a href="#debito">Debito</a>
    <a href="#aggiornamenti">Manovre</a>
  </div>
  <div class="nav-tag" id="dataStatus">⏺ carico dati…</div>
</nav>

<div class="hero">
  <div class="hero-inner">
    <div class="hero-eyebrow">// finanza pubblica italiana — dati aggiornati 2023–2024</div>
    <h1>Lo stato italiano<br><strong>come spende i tuoi soldi</strong></h1>
    <p class="hero-sub">Ogni anno il governo italiano raccoglie circa 900 miliardi di euro in tasse e contributi, e ne spende circa 1.040. Questa è la mappa di dove finiscono.</p>
    <div class="hero-numbers">
      <div class="hero-num">
        <div class="hero-num-val">~900</div>
        <div class="hero-num-label">mld € entrate fiscali</div>
      </div>
      <div class="hero-num">
        <div class="hero-num-val red">~1.040</div>
        <div class="hero-num-label">mld € spese totali</div>
      </div>
      <div class="hero-num">
        <div class="hero-num-val red">56,1%</div>
        <div class="hero-num-label">del PIL in spesa pubblica</div>
      </div>
      <div class="hero-num">
        <div class="hero-num-val red">137%</div>
        <div class="hero-num-label">del PIL in debito pubblico</div>
      </div>
      <div class="hero-num">
        <div class="hero-num-val red">~85 mld</div>
        <div class="hero-num-label">€/anno solo in interessi</div>
      </div>
    </div>
  </div>
</div>

<!-- SEZIONE 1: SPESA -->
<section class="section" id="spesa">
  <div class="section-header">
    <span class="section-num">01 /</span>
    <h2 class="section-title">Come viene speso il bilancio pubblico</h2>
  </div>
  <p class="section-desc">La spesa pubblica italiana ammonta a circa 1.040 miliardi di euro nel 2023–24. Ecco la composizione per categoria principale, in miliardi di euro e in percentuale sul totale.</p>

  <div class="tab-bar">
    <button class="tab active" onclick="switchTab('spesa','mld')">Miliardi €</button>
    <button class="tab" onclick="switchTab('spesa','pct')">% del PIL</button>
  </div>

  <div class="chart-wrap">
    <div class="chart-title">Spesa pubblica per categoria — Italia 2023</div>
    <span class="source-tag static" id="spesaSourceTag"><span class="source-dot"></span>dati statici MEF/ISTAT 2023</span>
    <div class="legend">
      <div class="legend-item"><div class="legend-sq" style="background:#c0392b"></div>Spesa rigida (difficile da tagliare)</div>
      <div class="legend-item"><div class="legend-sq" style="background:#2a78d6"></div>Servizi pubblici</div>
      <div class="legend-item"><div class="legend-sq" style="background:#888"></div>Altro</div>
    </div>
    <div class="canvas-wrap" style="height:360px">
      <canvas id="spesaChart" role="img" aria-label="Grafico a barre della spesa pubblica italiana per categoria">Dati spesa pubblica Italia 2023.</canvas>
    </div>
  </div>

  <div class="insight">
    <strong>Il dato che colpisce:</strong> sommando pensioni (350 mld) e interessi sul debito (85–90 mld), si arriva a circa 435 miliardi — oltre il 40% di tutta la spesa pubblica — che escono dal bilancio senza produrre servizi diretti ai cittadini oggi. Per confronto, sanità e istruzione insieme fanno circa 210 miliardi.
  </div>
</section>

<!-- SEZIONE 2: PENSIONI -->
<section class="section" id="pensioni">
  <div class="section-header">
    <span class="section-num">02 /</span>
    <h2 class="section-title">Il sistema pensionistico</h2>
  </div>
  <p class="section-desc">Con 340 miliardi di euro e il 16,2% del PIL, le pensioni rappresentano di gran lunga la voce più pesante del bilancio italiano — e una delle più alte d'Europa.</p>

  <div class="cards-grid">
    <div class="stat-card">
      <div class="stat-card-label">Pensionati totali</div>
      <div class="stat-card-val">16,2M</div>
      <div class="stat-card-sub">persone — 2023</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Pensione media</div>
      <div class="stat-card-val warn">~1.150 €</div>
      <div class="stat-card-sub">lordi/mese</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Pensione mediana</div>
      <div class="stat-card-val warn">~870 €</div>
      <div class="stat-card-sub">metà dei pensionati prende meno</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Età effettiva uscita</div>
      <div class="stat-card-val danger">61,5</div>
      <div class="stat-card-sub">anni — tra le più basse UE</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Spesa / PIL</div>
      <div class="stat-card-val danger">16,2%</div>
      <div class="stat-card-sub">vs 12,5% media UE</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Pensioni oltre 5.000 €</div>
      <div class="stat-card-val">480K</div>
      <div class="stat-card-sub">persone — 3% del totale</div>
    </div>
  </div>

  <div class="chart-wrap">
    <div class="chart-title">Distribuzione pensionati per fascia di importo mensile lordo</div>
    <div class="canvas-wrap" style="height:300px">
      <canvas id="pensioniChart" role="img" aria-label="Distribuzione pensionati per fascia importo">Distribuzione pensioni italiane per fascia.</canvas>
    </div>
  </div>

  <div class="chart-wrap" style="margin-top:1rem">
    <div class="chart-title">Spesa pensionistica % PIL — confronto europeo</div>
    <div class="canvas-wrap" style="height:380px">
      <canvas id="pensioniEuropaChart" role="img" aria-label="Confronto spesa pensionistica europea">Spesa pensionistica per paese europeo in % PIL.</canvas>
    </div>
  </div>
</section>

<!-- SEZIONE 3: CONFRONTO EUROPA -->
<section class="section" id="confronto">
  <div class="section-header">
    <span class="section-num">03 /</span>
    <h2 class="section-title">Il confronto europeo</h2>
  </div>
  <p class="section-desc">Seleziona una categoria di spesa per vedere dove si posiziona l'Italia rispetto ai principali paesi europei.</p>

  <div class="selector-row" id="catSelector">
    <button class="sel-btn active" onclick="selectCat('totale')">Spesa totale</button>
    <button class="sel-btn" onclick="selectCat('pensioni')">Protezione sociale</button>
    <button class="sel-btn" onclick="selectCat('sanita')">Sanità</button>
    <button class="sel-btn" onclick="selectCat('istruzione')">Istruzione</button>
    <button class="sel-btn" onclick="selectCat('interessi')">Interessi debito</button>
    <button class="sel-btn" onclick="selectCat('investimenti')">Investimenti</button>
  </div>

  <div class="chart-wrap">
    <div class="chart-title" id="europaChartTitle">Spesa pubblica totale in % PIL — 2023</div>
    <span class="source-tag static" id="europaSourceTag"><span class="source-dot"></span>dati statici Eurostat 2022–23</span>
    <div class="canvas-wrap" style="height:400px">
      <canvas id="europaChart" role="img" aria-label="Confronto spesa europea per categoria">Confronto europeo spesa pubblica.</canvas>
    </div>
  </div>

  <div class="insight" id="europaInsight">
    L'Italia è quinta in Europa per spesa totale sul PIL (56,1%), in compagnia di Francia, Austria, Belgio e Finlandia. Ma la composizione è molto diversa: l'Italia spende di più in pensioni e interessi, meno in istruzione e investimenti.
  </div>

  <h3 style="font-size:1rem; font-weight:500; margin: 2rem 0 1rem;">Tabella comparativa per categoria — % PIL</h3>
  <div style="overflow-x:auto">
  <table class="data-table">
    <thead>
      <tr>
        <th>Paese</th>
        <th class="num">Spesa tot.</th>
        <th class="num">Protezione sociale</th>
        <th class="num">Sanità</th>
        <th class="num">Istruzione</th>
        <th class="num">Interessi</th>
        <th class="num">Investimenti</th>
        <th>Debito/PIL</th>
      </tr>
    </thead>
    <tbody>
      <tr class="ita">
        <td>🇮🇹 Italia</td>
        <td class="num">56,1%</td>
        <td class="num" style="color:var(--red)">16,2%</td>
        <td class="num">6,7%</td>
        <td class="num" style="color:var(--red)">4,0%</td>
        <td class="num" style="color:var(--red)">4,3%</td>
        <td class="num" style="color:var(--red)">2,5%</td>
        <td><span class="badge badge-red">137%</span></td>
      </tr>
      <tr>
        <td>🇫🇷 Francia</td>
        <td class="num">57,3%</td>
        <td class="num">14,4%</td>
        <td class="num">8,5%</td>
        <td class="num">5,1%</td>
        <td class="num">2,0%</td>
        <td class="num">3,4%</td>
        <td><span class="badge badge-red">111%</span></td>
      </tr>
      <tr>
        <td>🇦🇹 Austria</td>
        <td class="num">56,7%</td>
        <td class="num">13,2%</td>
        <td class="num">7,8%</td>
        <td class="num">5,0%</td>
        <td class="num">1,7%</td>
        <td class="num">3,0%</td>
        <td><span class="badge badge-amber">82%</span></td>
      </tr>
      <tr>
        <td>🇩🇪 Germania</td>
        <td class="num">48,5%</td>
        <td class="num">11,9%</td>
        <td class="num">7,7%</td>
        <td class="num">4,6%</td>
        <td class="num">1,1%</td>
        <td class="num">2,7%</td>
        <td><span class="badge badge-green">66%</span></td>
      </tr>
      <tr>
        <td>🇪🇸 Spagna</td>
        <td class="num">43,8%</td>
        <td class="num">11,4%</td>
        <td class="num">7,4%</td>
        <td class="num">4,5%</td>
        <td class="num">2,3%</td>
        <td class="num">3,0%</td>
        <td><span class="badge badge-red">108%</span></td>
      </tr>
      <tr>
        <td>🇳🇱 Olanda</td>
        <td class="num">44,9%</td>
        <td class="num">9,1%</td>
        <td class="num">7,5%</td>
        <td class="num">5,3%</td>
        <td class="num">0,8%</td>
        <td class="num">3,3%</td>
        <td><span class="badge badge-green">48%</span></td>
      </tr>
      <tr>
        <td>🇸🇪 Svezia</td>
        <td class="num">52,6%</td>
        <td class="num">8,8%</td>
        <td class="num">8,9%</td>
        <td class="num">6,8%</td>
        <td class="num">0,4%</td>
        <td class="num">4,2%</td>
        <td><span class="badge badge-green">33%</span></td>
      </tr>
      <tr>
        <td>🇩🇰 Danimarca</td>
        <td class="num">54,3%</td>
        <td class="num">8,3%</td>
        <td class="num">9,2%</td>
        <td class="num">6,5%</td>
        <td class="num">0,5%</td>
        <td class="num">3,8%</td>
        <td><span class="badge badge-green">29%</span></td>
      </tr>
      <tr>
        <td>🇬🇷 Grecia</td>
        <td class="num">54,8%</td>
        <td class="num">16,8%</td>
        <td class="num">5,9%</td>
        <td class="num">3,8%</td>
        <td class="num">3,1%</td>
        <td class="num">2,2%</td>
        <td><span class="badge badge-red">161%</span></td>
      </tr>
      <tr style="background:var(--paper-2); font-style:italic">
        <td>🇪🇺 Media UE-27</td>
        <td class="num">50,0%</td>
        <td class="num">12,5%</td>
        <td class="num">7,2%</td>
        <td class="num">4,9%</td>
        <td class="num">1,9%</td>
        <td class="num">3,1%</td>
        <td><span class="badge badge-amber">~87%</span></td>
      </tr>
    </tbody>
  </table>
  </div>
</section>

<!-- SEZIONE 4: DEBITO -->
<section class="section" id="debito">
  <div class="section-header">
    <span class="section-num">04 /</span>
    <h2 class="section-title">Il debito pubblico</h2>
  </div>
  <p class="section-desc">Il debito pubblico italiano supera i 2.870 miliardi di euro — circa 137% del PIL. Ogni italiano, neonati inclusi, porta sulle spalle circa 48.000 euro di debito pubblico.</p>

  <div class="cards-grid">
    <div class="stat-card">
      <div class="stat-card-label">Debito totale 2024</div>
      <div class="stat-card-val danger">2.870 mld</div>
      <div class="stat-card-sub">euro</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">% del PIL</div>
      <div class="stat-card-val danger">137%</div>
      <div class="stat-card-sub">2° più alto UE dopo Grecia</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Interessi annui</div>
      <div class="stat-card-val danger">~87 mld</div>
      <div class="stat-card-sub">euro — in crescita con i tassi</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Debito pro capite</div>
      <div class="stat-card-val danger">~48.000 €</div>
      <div class="stat-card-sub">per ogni italiano</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Deficit 2023</div>
      <div class="stat-card-val danger">7,4%</div>
      <div class="stat-card-sub">del PIL (superbonus incluso)</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Obiettivo 2026</div>
      <div class="stat-card-val warn">3,0%</div>
      <div class="stat-card-sub">limite Patto Stabilità UE</div>
    </div>
  </div>

  <div class="chart-wrap">
    <div class="chart-title">Debito pubblico % PIL — confronto europeo 2023</div>
    <div class="canvas-wrap" style="height:340px">
      <canvas id="debitoChart" role="img" aria-label="Confronto debito pubblico europeo in percentuale PIL">Debito pubblico per paese europeo.</canvas>
    </div>
  </div>

  <div class="insight">
    <strong>Il circolo vizioso:</strong> più debito → più interessi da pagare → meno risorse per investimenti → crescita lenta → più difficile ridurre il debito. L'Italia paga oggi ~87 miliardi solo di interessi — il doppio della spesa per l'istruzione. Ogni punto percentuale di aumento dei tassi di interesse costa circa 28 miliardi in più all'anno sul medio termine, man mano che i titoli esistenti vanno a scadenza.
  </div>
</section>

<!-- SEZIONE 5: AGGIORNAMENTI -->
<section class="section" id="aggiornamenti">
  <div class="section-header">
    <span class="section-num">05 /</span>
    <h2 class="section-title">Le ultime leggi di bilancio</h2>
  </div>
  <p class="section-desc">La legge di bilancio (manovra finanziaria) viene approvata ogni anno entro il 31 dicembre. Qui i link alle fonti ufficiali — testo di legge, dossier parlamentari e relazioni tecniche — per ogni manovra recente.</p>

  <div class="manovra-list">

    <div class="manovra-item">
      <div class="manovra-year">2025</div>
      <div>
        <div class="manovra-title">Legge di Bilancio 2025 (L. 30 dicembre 2024, n. 207)</div>
        <div class="manovra-desc">Manovra da circa 30 miliardi di euro. Proroga del cuneo fiscale, riforma IRPEF a tre aliquote, taglio del bonus elettrodomestici, interventi su pensioni e sanità.</div>
        <div class="manovra-links">
          <a class="manovra-link" href="https://www.gazzettaufficiale.it/eli/id/2024/12/30/24G00237/sg" target="_blank" rel="noopener">Testo in Gazzetta Ufficiale</a>
          <a class="manovra-link" href="https://www.senato.it/leg/19/BGT/Schede/Ddliter/57954.htm" target="_blank" rel="noopener">Dossier Senato</a>
          <a class="manovra-link" href="https://www.mef.gov.it/" target="_blank" rel="noopener">MEF</a>
        </div>
      </div>
    </div>

    <div class="manovra-item">
      <div class="manovra-year">2024</div>
      <div>
        <div class="manovra-title">Legge di Bilancio 2024 (L. 30 dicembre 2023, n. 213)</div>
        <div class="manovra-desc">Manovra da circa 24 miliardi. Conferma del taglio del cuneo fiscale, riforma IRPEF a quattro aliquote (poi sostituita), stop a Superbonus al 110%.</div>
        <div class="manovra-links">
          <a class="manovra-link" href="https://www.gazzettaufficiale.it/eli/id/2023/12/30/23G00220/sg" target="_blank" rel="noopener">Testo in Gazzetta Ufficiale</a>
          <a class="manovra-link" href="https://www.camera.it/leg19/126?leg=19&idDocumento=1627" target="_blank" rel="noopener">Dossier Camera</a>
        </div>
      </div>
    </div>

    <div class="manovra-item">
      <div class="manovra-year">2023</div>
      <div>
        <div class="manovra-title">Legge di Bilancio 2023 (L. 29 dicembre 2022, n. 197)</div>
        <div class="manovra-desc">Prima manovra del governo Meloni, circa 35 miliardi, in gran parte assorbiti dal caro energia. Tetto al contante, flat tax incrementale per autonomi, riforma pensioni con Quota 103.</div>
        <div class="manovra-links">
          <a class="manovra-link" href="https://www.gazzettaufficiale.it/eli/id/2022/12/29/22G00211/sg" target="_blank" rel="noopener">Testo in Gazzetta Ufficiale</a>
          <a class="manovra-link" href="https://www.senato.it/leg/19/BGT/Schede/Ddliter/56625.htm" target="_blank" rel="noopener">Dossier Senato</a>
        </div>
      </div>
    </div>

    <div class="manovra-item">
      <div class="manovra-year">2022</div>
      <div>
        <div class="manovra-title">Legge di Bilancio 2022 (L. 30 dicembre 2021, n. 234)</div>
        <div class="manovra-desc">Governo Draghi. Riforma IRPEF a quattro aliquote, taglio cuneo fiscale, proroga Superbonus 110% con nuove regole, fondo complementare al PNRR.</div>
        <div class="manovra-links">
          <a class="manovra-link" href="https://www.gazzettaufficiale.it/eli/id/2021/12/30/21G00208/sg" target="_blank" rel="noopener">Testo in Gazzetta Ufficiale</a>
          <a class="manovra-link" href="https://www.camera.it/leg18/126?leg=18&idDocumento=3424" target="_blank" rel="noopener">Dossier Camera</a>
        </div>
      </div>
    </div>

  </div>

  <div class="insight" style="margin-top: 2rem;">
    <strong>Dove trovare i documenti ufficiali:</strong> il <a href="https://www.mef.gov.it/documenti-pubblicazioni/doc-finanza-pubblica/" target="_blank" rel="noopener" style="color:var(--ink); text-decoration:underline;">MEF</a> pubblica il Documento di Economia e Finanza (DEF) e la Nota di Aggiornamento (NADEF) ogni anno in primavera e autunno. Il testo definitivo delle leggi è sempre su <a href="https://www.gazzettaufficiale.it" target="_blank" rel="noopener" style="color:var(--ink); text-decoration:underline;">Gazzetta Ufficiale</a>, mentre i dossier tecnici di accompagnamento (più leggibili del testo di legge) sono su <a href="https://www.senato.it" target="_blank" rel="noopener" style="color:var(--ink); text-decoration:underline;">Senato</a> e <a href="https://www.camera.it" target="_blank" rel="noopener" style="color:var(--ink); text-decoration:underline;">Camera</a>.
  </div>
</section>

<footer>
  <div style="max-width:980px; margin:0 auto;">
    ITALIA<span style="color:var(--red)">SPENDE</span> — prototipo dimostrativo &nbsp;|&nbsp;
    Fonti: Eurostat COFOG · MEF Conto Consolidato PA · ISTAT · INPS Rapporto Annuale · OCSE Pensions at a Glance 2023 · Banca d'Italia<br>
    I dati si riferiscono al 2022–2024. Alcune voci sono stime basate su fonti ufficiali. Questo sito non è affiliato ad alcun ente governativo.
  </div>
</footer>

</div>

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
    padding: 0 2rem;
    height: 52px;
    border-bottom: 2px solid var(--is-red);
  }
  .ita-spende .nav-brand {
    font-family: var(--is-font-mono);
    font-size: 14px; font-weight: 500;
    color: #fff; letter-spacing: 0.02em;
  }
  .ita-spende .nav-brand span { color: var(--is-red); }
  .ita-spende .nav-links { display: flex; gap: 2rem; }
  .ita-spende .nav-links a {
    font-size: 12px; font-weight: 500; letter-spacing: 0.08em;
    text-transform: uppercase; color: #aaa;
    text-decoration: none; transition: color 0.15s;
  }
  .ita-spende .nav-links a:hover { color: #fff; }
  .ita-spende .nav-tag {
    font-family: var(--is-font-mono);
    font-size: 11px; color: #555;
  }

  
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
    .ita-spende .nav-links { display: none; }
    .ita-spende .hero { padding: 3rem 1rem 2.5rem; }
    .ita-spende .section { padding: 2.5rem 1rem; }
    .ita-spende .hero-num { padding: 1rem 1rem 1rem 0; }
  }
</style>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.js"></script>
<script>
const spesaData = {
  labels: ['Pensioni e\nprevidenza','Sanità','PA generale','Istruzione','Difesa e\nordine pub.','Welfare /\nassistenza','Interessi\ndebito','Infrastrutture\ne investimenti','Altro'],
  mld: [350, 130, 115, 80, 55, 90, 87, 50, 83],
  pct: [16.2, 6.7, 6.1, 4.0, 2.8, 4.8, 4.3, 2.5, 4.3],
  colors: ['#c0392b','#2a78d6','#4a3aa7','#2a78d6','#888','#1baf7a','#c0392b','#1baf7a','#aaa']
};

const pensioniDistrib = {
  labels: ['< 500 €','500–1.000 €','1.000–1.500 €','1.500–2.000 €','2.000–3.000 €','3.000–5.000 €','> 5.000 €'],
  count: [1.1, 4.5, 4.0, 2.6, 2.3, 1.1, 0.48]
};

const europaData = {
  paesi: ['🇬🇷 Grecia','🇫🇷 Francia','🇦🇹 Austria','🇧🇪 Belgio','🇫🇮 Finlandia','🇮🇹 Italia','🇩🇰 Danimarca','🇸🇪 Svezia','🇵🇹 Portogallo','🇩🇪 Germania','🇳🇱 Olanda','🇪🇸 Spagna'],
  totale:      [54.8,57.3,56.7,56.4,56.2,56.1,54.3,52.6,51.0,48.5,44.9,43.8],
  pensioni:    [18.5,23.3,21.2,20.1,25.6,21.0,19.7,18.9,16.4,19.5,16.4,18.5],
  sanita:      [5.9,8.5,7.8,8.2,7.5,6.7,9.2,8.9,6.4,7.7,7.5,7.4],
  istruzione:  [3.8,5.1,5.0,5.9,5.5,4.0,6.5,6.8,4.8,4.6,5.3,4.5],
  interessi:   [3.1,2.0,1.7,2.5,0.8,4.3,0.5,0.4,2.8,1.1,0.8,2.3],
  investimenti:[2.2,3.4,3.0,2.8,3.5,2.5,3.8,4.2,3.1,2.7,3.3,3.0]
};

const debitoData = {
  paesi: ['🇬🇷 Grecia','🇮🇹 Italia','🇫🇷 Francia','🇧🇪 Belgio','🇪🇸 Spagna','🇵🇹 Portogallo','🇦🇹 Austria','🇩🇪 Germania','🇫🇮 Finlandia','🇮🇪 Irlanda','🇸🇪 Svezia','🇳🇱 Olanda','🇩🇰 Danimarca'],
  valori:[161,137,111,105,108,99,82,66,73,43,33,48,29]
};

const europaInsights = {
  totale: "L'Italia è quinta in Europa per spesa totale sul PIL (56,1%), in compagnia di Francia, Austria, Belgio e Finlandia. Ma la composizione è molto diversa: l'Italia spende di più in pensioni e interessi, meno in istruzione e investimenti.",
  pensioni: "Attenzione: questa voce Eurostat (\"Social protection\", GF10) è più ampia delle sole pensioni — include anche disoccupazione, famiglia, invalidità e altri sussidi. L'Italia è qui al 21% del PIL, terza dopo Svezia e Francia. Le pensioni vere e proprie (sezione dedicata sopra) pesano circa 16,2% — il resto sono altri trasferimenti sociali.",
  sanita: "La sanità italiana (6,7% PIL) è sotto la media UE (7,2%) e molto al di sotto di Danimarca e Svezia (~9%). Il sistema sanitario italiano è comunque considerato efficiente in termini di output per euro speso.",
  istruzione: "L'Italia spende il 4,0% del PIL in istruzione, contro il 4,9% di media UE e il 6,8% della Svezia. È una delle voci in cui il divario è più preoccupante per la crescita futura.",
  interessi: "Il costo degli interessi sul debito (4,3% PIL) è più del doppio della media europea (1,9%). La Svezia paga appena lo 0,4%. Questi soldi non producono alcun servizio: sono il costo del debito accumulato nel passato.",
  investimenti: "L'Italia investe il 2,5% del PIL in infrastrutture e investimenti pubblici — sotto la media UE (3,1%) e molto al di sotto di Svezia (4,2%) e Danimarca (3,8%). Il PNRR sta cercando di colmare parte di questo gap."
};

// ── CHARTS ────────────────────────────────────────────────────────────────────

let spesaChart, europaChart, debitoChart;
let currentEuropaChart = null;
let currentSelectedCat = 'totale';
let debitoChartInstance = null;

function wrapLabels(labels) {
  return labels.map(l => l.includes('\n') ? l.split('\n') : l);
}

// Spesa chart
(function() {
  const ctx = document.getElementById('spesaChart').getContext('2d');
  spesaChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: wrapLabels(spesaData.labels),
      datasets: [{
        label: 'Miliardi €',
        data: spesaData.mld,
        backgroundColor: spesaData.colors,
        borderRadius: 3,
        borderSkipped: false
      }]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: ctx => ` ${ctx.parsed.y} miliardi € — ${((ctx.parsed.y/1040)*100).toFixed(1)}% del totale`
          }
        }
      },
      scales: {
        x: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#7a7a7a' } },
        y: {
          grid: { color: '#e8e5de' },
          ticks: {
            font: { size: 11 }, color: '#7a7a7a',
            callback: v => v + ' mld'
          }
        }
      }
    }
  });
})();

// Pensioni distribuzione
(function() {
  const ctx = document.getElementById('pensioniChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: pensioniDistrib.labels,
      datasets: [{
        label: 'Pensionati (milioni)',
        data: pensioniDistrib.count,
        backgroundColor: ['#b5d4f4','#85b7eb','#378add','#185fa5','#0c447c','#042C53','#c0392b'],
        borderRadius: 3
      }]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: { callbacks: { label: ctx => ` ${ctx.parsed.y}M pensionati` } }
      },
      scales: {
        x: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#7a7a7a' } },
        y: { grid: { color: '#e8e5de' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + 'M' } }
      }
    }
  });
})();

// Pensioni Europa
let pensioniEuropaChartInstance = null;
function rebuildPensioniEuropaChart() {
  if (pensioniEuropaChartInstance) pensioniEuropaChartInstance.destroy();
  const sorted = europaData.paesi.map((p,i) => ({ p, v: europaData.pensioni[i] }))
    .sort((a,b) => b.v - a.v);
  const ctx = document.getElementById('pensioniEuropaChart').getContext('2d');
  pensioniEuropaChartInstance = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: sorted.map(d => d.p),
      datasets: [{
        label: '% PIL',
        data: sorted.map(d => d.v),
        backgroundColor: sorted.map(d => d.p.includes('🇮🇹') ? '#c0392b' : '#b5d4f4'),
        borderRadius: 3
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true, maintainAspectRatio: false,
      animation: { duration: 400 },
      plugins: {
        legend: { display: false },
        tooltip: { callbacks: { label: ctx => ` ${ctx.parsed.x}% del PIL` } }
      },
      scales: {
        x: {
          grid: { color: '#e8e5de' },
          ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + '%' },
          min: 0, max: 18
        },
        y: { grid: { display: false }, ticks: { font: { size: 12 }, color: '#3a3a3a' } }
      }
    }
  });
}
rebuildPensioniEuropaChart();

// Europa confronto
(function() {
  renderEuropaChart('totale');
})();

// Debito
rebuildDebitoChart();

// ── INTERACTIONS ──────────────────────────────────────────────────────────────

function switchTab(section, mode) {
  const btns = document.querySelectorAll('.tab');
  btns.forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');

  if (section === 'spesa') {
    const isM = mode === 'mld';
    spesaChart.data.datasets[0].data = isM ? spesaData.mld : spesaData.pct;
    spesaChart.data.datasets[0].label = isM ? 'Miliardi €' : '% PIL';
    spesaChart.options.scales.y.ticks.callback = v => isM ? v + ' mld' : v + '%';
    spesaChart.options.plugins.tooltip.callbacks.label = ctx =>
      isM ? ` ${ctx.parsed.y} miliardi €` : ` ${ctx.parsed.y}% del PIL`;
    spesaChart.update();
  }
}

function renderEuropaChart(cat) {
  const raw = europaData[cat];
  const sorted = europaData.paesi.map((p,i) => ({ p, v: raw[i] })).sort((a,b) => b.v - a.v);

  const titles = {
    totale: 'Spesa pubblica totale in % PIL — 2023',
    pensioni: 'Spesa per protezione sociale in % PIL — 2023',
    sanita: 'Spesa sanitaria pubblica in % PIL — 2023',
    istruzione: 'Spesa per istruzione in % PIL — 2023',
    interessi: 'Costo interessi sul debito in % PIL — 2023',
    investimenti: 'Investimenti pubblici in % PIL — 2023'
  };
  document.getElementById('europaChartTitle').textContent = titles[cat];
  document.getElementById('europaInsight').textContent = europaInsights[cat];

  if (currentEuropaChart) currentEuropaChart.destroy();

  const ctx = document.getElementById('europaChart').getContext('2d');
  currentEuropaChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: sorted.map(d => d.p),
      datasets: [{
        label: '% PIL',
        data: sorted.map(d => d.v),
        backgroundColor: sorted.map(d => d.p.includes('🇮🇹') ? '#c0392b' : '#b5d4f4'),
        borderRadius: 3
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true, maintainAspectRatio: false,
      animation: { duration: 400 },
      plugins: {
        legend: { display: false },
        tooltip: { callbacks: { label: ctx => ` ${ctx.parsed.x}% del PIL` } }
      },
      scales: {
        x: {
          grid: { color: '#e8e5de' },
          ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + '%' }
        },
        y: { grid: { display: false }, ticks: { font: { size: 12 }, color: '#3a3a3a' } }
      }
    }
  });
}
function rebuildDebitoChart() {
  if (debitoChartInstance) debitoChartInstance.destroy();
  const sorted = debitoData.paesi.map((p,i) => ({ p, v: debitoData.valori[i] })).sort((a,b) => b.v - a.v);
  const ctx = document.getElementById('debitoChart').getContext('2d');
  debitoChartInstance = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: sorted.map(d => d.p),
      datasets: [{
        label: '% PIL',
        data: sorted.map(d => d.v),
        backgroundColor: sorted.map(d => {
          if (d.p.includes('🇮🇹')) return '#c0392b';
          if (d.v > 100) return '#f09595';
          if (d.v > 70) return '#fab219';
          return '#9FE1CB';
        }),
        borderRadius: 3
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true, maintainAspectRatio: false,
      animation: { duration: 400 },
      plugins: {
        legend: { display: false },
        tooltip: { callbacks: { label: ctx => ` ${ctx.parsed.x}% del PIL` } }
      },
      scales: {
        x: { grid: { color: '#e8e5de' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + '%' }, min: 0, max: 175 },
        y: { grid: { display: false }, ticks: { font: { size: 12 }, color: '#3a3a3a' } }
      }
    }
  });
}

function setStatus(state, label) {
  const el = document.getElementById('dataStatus');
  if (!el) return;
  el.className = state;
  el.textContent = label;
}

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


// ── DATI STATICI PERIODICI ──────────────────────────────────────────────────
//
// Il file assets/data/eurostat.json viene rigenerato una volta a settimana da
// una GitHub Action (scripts/fetch_eurostat.py), che interroga l'API Eurostat
// dal proprio ambiente e scrive un JSON datato e con fonte dichiarata.
// Questa pagina legge quel file statico — non chiama mai Eurostat dal browser
// di chi visita il sito. Se il file non è raggiungibile, restano visibili i
// valori di riferimento incorporati qui sopra (anno 2023).

const CODE_TO_LABEL = {
  IT: '🇮🇹 Italia', FR: '🇫🇷 Francia', AT: '🇦🇹 Austria', BE: '🇧🇪 Belgio',
  FI: '🇫🇮 Finlandia', DK: '🇩🇰 Danimarca', SE: '🇸🇪 Svezia', PT: '🇵🇹 Portogallo',
  DE: '🇩🇪 Germania', NL: '🇳🇱 Olanda', ES: '🇪🇸 Spagna', EL: '🇬🇷 Grecia',
  IE: '🇮🇪 Irlanda'
};

function applyStaticData(data) {
  const CATEGORIE_EUROPA = ['totale', 'pensioni', 'sanita', 'istruzione', 'interessi'];
  let updatedAny = false;

  CATEGORIE_EUROPA.forEach(cat => {
    const values = data[cat];
    if (!values) return;
    europaData.paesi.forEach((label, i) => {
      const code = Object.keys(CODE_TO_LABEL).find(c => CODE_TO_LABEL[c] === label);
      if (code && values[code] !== undefined) {
        europaData[cat][i] = Number(values[code]);
        updatedAny = true;
      }
    });
  });

  if (data.debito) {
    debitoData.paesi.forEach((label, i) => {
      const code = Object.keys(CODE_TO_LABEL).find(c => CODE_TO_LABEL[c] === label);
      if (code && data.debito[code] !== undefined) {
        debitoData.valori[i] = Number(data.debito[code]);
        updatedAny = true;
      }
    });
  }

  return updatedAny;
}

async function loadStaticData() {
  try {
    const res = await fetchWithTimeout("{{ '/assets/data/eurostat.json' | relative_url }}", 8000);
    if (!res.ok) throw new Error('HTTP ' + res.status);
    const data = await res.json();
    const aggiornato = applyStaticData(data);

    rebuildDebitoChart();
    rebuildPensioniEuropaChart();
    renderEuropaChart(currentSelectedCat || 'totale');

    const d = new Date(data.generated_at);
    const dataFmt = d.toLocaleDateString('it-IT', { year: 'numeric', month: 'long', day: 'numeric' });

    if (aggiornato) {
      setStatus('live', `⏺ dati aggiornati il ${dataFmt}`);
      setSourceTag('europaSourceTag', true, `Eurostat — aggiornato il ${dataFmt}`);
    } else {
      setStatus('fallback', '⏺ dati di riferimento 2023 (file statico vuoto o incompleto)');
    }
  } catch (e) {
    console.warn('Dati statici non disponibili, uso i valori di riferimento incorporati:', e.message);
    setStatus('fallback', '⏺ dati di riferimento 2023 — file non raggiungibile');
  }
}

window.addEventListener('DOMContentLoaded', () => {
  setTimeout(loadStaticData, 200);
});

function selectCat(cat) {
  currentSelectedCat = cat;
  document.querySelectorAll('.sel-btn').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
  renderEuropaChart(cat);
}
</script>
