---
layout: default
title: "Istruzione — spesa, alunni, classi e organico docente"
description: "Approfondimento sulla scuola statale italiana: spesa per Missione e Programma dal bilancio MIM, alunni, classi e organico docente per regione, con fonti sempre citate."
---
<div class="prose">
<span class="prose__kicker">Approfondimento</span>
<h1>Istruzione — spesa, alunni, classi e organico</h1>
<p>
  Quarta voce di spesa pubblica dopo pensioni, sanità e Pubblica Amministrazione:
  qui la scuola statale italiana vista da due angolazioni — quanto costa e come si
  scompone il bilancio del Ministero dell'Istruzione e del Merito (MIM), e quante
  sono le persone coinvolte (alunni, classi, organico docente) e come si
  distribuiscono sul territorio.
  Alcune dimensioni previste per questa pagina (confronto europeo, spesa per
  regione) sono ancora in fase di raccolta dati e sono segnalate esplicitamente
  più sotto, senza valori inventati nel frattempo.
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
    <a href="#ist-missione">Spesa per Missione</a>
    <div class="nav-group" id="approfondimentiGroup">
      <button class="nav-group__toggle" aria-haspopup="true" aria-expanded="false">Altre sezioni <span class="nav-caret">▾</span></button>
      <div class="nav-group__menu">
        <a href="#ist-alunni-classi">Alunni e classi</a>
        <a href="#ist-organico">Organico e sostegno</a>
        <a href="#ist-indirizzi">Indirizzi II grado</a>
      </div>
    </div>
    <a href="{{ '/spesa-pubblica/' | relative_url }}">← Panoramica generale</a>
  </div>
  <div class="nav-tag">Dati fermi al 2024/2025</div>
</nav>

<main class="ita-spende__main">

<!-- SEZIONE 1: SPESA PER MISSIONE E PROGRAMMA -->
<section class="section" id="ist-missione">
  <div class="section-header">
    <span class="section-num">01 /</span>
    <h2 class="section-title">Spesa per Missione e Programma — bilancio MIM</h2>
  </div>
  <p class="section-desc">Il bilancio del Ministero dell'Istruzione e del Merito si articola in Missioni e Programmi. La <strong>Missione 1 "Istruzione scolastica"</strong> è quella che riguarda direttamente scuole, alunni e personale docente (la Missione 4 "Servizi generali", qui esclusa, riguarda funzionamento e affari generali del Ministero stesso).</p>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Missione 1 "Istruzione scolastica" per Programma — Competenza 2025 (mld €)</div>
    <span class="source-tag static"><span class="source-dot"></span>MIM — Nota Integrativa al disegno di Legge di Bilancio 2025-2027</span>
    <div class="canvas-wrap" style="height:400px;">
      <canvas id="istMissioneChart" role="img" aria-label="Spesa Missione 1 Istruzione scolastica per programma, competenza 2025: Istruzione del primo ciclo 34,00 miliardi, Istruzione del secondo ciclo 18,27 miliardi, Programmazione e coordinamento 1,67 miliardi, Edilizia scolastica e sicurezza 1,20 miliardi, Istituzioni scolastiche non statali e paritarie 0,70 miliardi, Reclutamento e aggiornamento personale 0,43 miliardi, Politiche territoriali e USR 0,22 miliardi, Sviluppo del sistema e diritto allo studio 0,21 miliardi, Istruzione terziaria non universitaria e ITS 0,05 miliardi.">Spesa Missione 1 per programma, competenza 2025.</canvas>
    </div>
  </div>

  <div style="overflow-x:auto; margin-bottom:1.5rem;">
    <table class="data-table">
      <thead>
        <tr>
          <th>Programma</th>
          <th class="num">CP 2025 (€)</th>
          <th class="num">% Missione 1</th>
        </tr>
      </thead>
      <tbody>
        <tr class="ita">
          <td>1.6 — Istruzione del primo ciclo <span style="font-size:11px;color:var(--is-ink-3);">(infanzia, primaria, secondaria I grado)</span></td>
          <td class="num">34.003.998.510</td>
          <td class="num">59,9%</td>
        </tr>
        <tr>
          <td>1.7 — Istruzione del secondo ciclo <span style="font-size:11px;color:var(--is-ink-3);">(scuole superiori)</span></td>
          <td class="num">18.270.873.958</td>
          <td class="num">32,2%</td>
        </tr>
        <tr>
          <td>1.1 — Programmazione e coordinamento</td>
          <td class="num">1.672.014.345</td>
          <td class="num">2,9%</td>
        </tr>
        <tr>
          <td>1.9 — Edilizia scolastica e sicurezza</td>
          <td class="num">1.200.988.736</td>
          <td class="num">2,1%</td>
        </tr>
        <tr>
          <td>1.3 — Istituzioni scolastiche non statali / paritarie</td>
          <td class="num">703.994.522</td>
          <td class="num">1,2%</td>
        </tr>
        <tr>
          <td>1.8 — Reclutamento e aggiornamento personale</td>
          <td class="num">431.502.449</td>
          <td class="num">0,8%</td>
        </tr>
        <tr>
          <td>1.5 — Politiche territoriali / USR <span style="font-size:11px;color:var(--is-ink-3);">(aggregato nazionale)</span></td>
          <td class="num">217.147.660</td>
          <td class="num">0,4%</td>
        </tr>
        <tr>
          <td>1.2 — Sviluppo del sistema e diritto allo studio</td>
          <td class="num">214.285.455</td>
          <td class="num">0,4%</td>
        </tr>
        <tr>
          <td>1.4 — Istruzione terziaria non universitaria / ITS</td>
          <td class="num">51.032.659</td>
          <td class="num">0,1%</td>
        </tr>
        <tr>
          <td><strong>Totale Missione 1</strong></td>
          <td class="num"><strong>56.765.838.294</strong></td>
          <td class="num"><strong>100%</strong></td>
        </tr>
        <tr>
          <td>Totale Ministero <span style="font-size:11px;color:var(--is-ink-3);">(incl. Missione 4 — servizi generali)</span></td>
          <td class="num">56.901.553.611</td>
          <td class="num">—</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="insight">
    <strong>Quasi due terzi del bilancio scuola è il primo ciclo:</strong> infanzia, primaria e secondaria di primo grado insieme (Programma 1.6) assorbono il 59,9% della Missione 1 — coerente con il fatto che sono anche il segmento con più alunni e più sezioni/classi (vedi sezione 02). Primo e secondo ciclo insieme fanno il 92,1% del bilancio: tutto il resto — coordinamento, edilizia, paritarie, reclutamento, diritto allo studio, ITS — si divide il restante 7,9%.
  </div>

  <div class="chart-wrap" style="margin-top:2rem; margin-bottom:1.5rem;">
    <div class="chart-title">Dentro il primo e il secondo ciclo — scomposizione per natura della spesa (CP 2025)</div>
    <span class="source-tag static"><span class="source-dot"></span>MIM — Nota Integrativa al disegno di Legge di Bilancio 2025-2027</span>
    <div style="display:flex;flex-wrap:wrap;gap:12px;margin:0.75rem 0;font-size:11px;color:var(--is-ink-3);">
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#2a78d6;display:inline-block;"></span>Primo ciclo</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#c0392b;display:inline-block;"></span>Secondo ciclo</span>
    </div>
    <div class="canvas-wrap" style="height:340px;">
      <canvas id="istScomposizioneChart" role="img" aria-label="Scomposizione spesa primo ciclo (64,8% docenti, 12,5% dirigenti e ATA, 18,8% sostegno, 1,1% funzionamento istituti, 2,8% supplenze) e secondo ciclo (66,5% docenti, 16,3% dirigenti e ATA, 12,5% sostegno, 1,1% funzionamento istituti, 2,6% supplenze, 0,9% miglioramento offerta formativa), percentuali sul relativo totale.">Scomposizione spesa primo e secondo ciclo per natura, 2025.</canvas>
    </div>
  </div>

  <div class="insight">
    <strong>Il sostegno pesa quasi il doppio nel primo ciclo:</strong> la voce "sostegno BES / docenti di sostegno" assorbe il 18,8% del budget del primo ciclo contro il 12,5% del secondo — coerente con i dati sulla disabilità della sezione 02, dove l'incidenza degli alunni con disabilità è più alta in primaria (5,7%) e secondaria di I grado (6,0%) che alla secondaria di II grado (3,6%). In entrambi i cicli, personale docente e dirigenti/ATA insieme superano il 77% della spesa: la scuola statale italiana è, in bilancio, prima di tutto costo del personale.
  </div>
  <div class="insight" style="margin-top:1rem; border-color: var(--is-ink-3);">
    <strong>Nota metodologica:</strong> "CP" indica gli stanziamenti di competenza (gli importi impegnabili nell'anno, non necessariamente le uscite di cassa effettive). Il Programma 1.5 è riportato come aggregato nazionale: la Nota Integrativa non lo scompone per singolo Ufficio Scolastico Regionale. Il totale "Ministero" incluso in tabella (Missione 1 + Missione 4) non coincide con la sola spesa scolastica: la Missione 4 copre funzionamento e affari generali del Ministero stesso, non prestazioni dirette alle scuole.
  </div>
</section>

<!-- SEZIONE 2: ALUNNI E CLASSI -->
<section class="section" id="ist-alunni-classi">
  <div class="section-header">
    <span class="section-num">02 /</span>
    <h2 class="section-title">Alunni, classi e rapporto alunni/classe</h2>
  </div>
  <p class="section-desc">Dati di Organico di Fatto per l'A.S. 2024/2025, riferiti al 6 settembre 2024 (in corso di ulteriore aggiornamento da parte degli Uffici periferici al momento della rilevazione). Le istituzioni scolastiche statali sono <strong>7.600</strong> (7.473 istituzioni scolastiche + 127 Centri Provinciali per l'Istruzione degli Adulti), distribuite su <strong>40.076 sedi</strong> — il 69% delle quali dedicato a infanzia e primaria.</p>

  <div class="cards-grid" style="margin-bottom:1.5rem;">
    <div class="stat-card">
      <div class="stat-card-label">Alunni totali</div>
      <div class="stat-card-val">7.073.587</div>
      <div class="stat-card-sub">di cui 331.124 con disabilità (4,7%)</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Classi totali</div>
      <div class="stat-card-val">362.115</div>
      <div class="stat-card-sub">tutti gli ordini di scuola</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Rapporto alunni/classe</div>
      <div class="stat-card-val">19,5</div>
      <div class="stat-card-sub">media nazionale, tutti gli ordini</div>
    </div>
  </div>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Rapporto alunni (bambini/studenti)/classe per ordine di scuola — A.S. 2024/2025</div>
    <span class="source-tag static"><span class="source-dot"></span>MIM — Ufficio di Statistica, Focus "Principali dati della scuola", settembre 2024</span>
    <div class="canvas-wrap" style="height:280px;">
      <canvas id="istRapportoOrdineChart" role="img" aria-label="Rapporto alunni per classe per ordine di scuola: infanzia 19,7 bambini per sezione, primaria 18,0 alunni per classe, secondaria di primo grado 19,7, secondaria di secondo grado 20,9.">Rapporto alunni/classe per ordine di scuola.</canvas>
    </div>
  </div>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Rapporto alunni/classe per regione — A.S. 2024/2025 (tutti gli ordini)</div>
    <span class="source-tag static"><span class="source-dot"></span>MIM — Ufficio di Statistica, Focus "Principali dati della scuola", settembre 2024 (Tab. 4)</span>
    <div class="canvas-wrap" style="height:480px;">
      <canvas id="istRapportoRegioneChart" role="img" aria-label="Rapporto alunni/classe per regione, dal più basso al più alto: Molise 16,6, Basilicata 16,7, Sardegna 16,8, Campania 18,4, Sicilia 18,6, Friuli Venezia Giulia 18,5, Calabria 17,2, Abruzzo 19,2, Puglia 19,2, Umbria 19,4, Piemonte 19,5, Marche 20,0, Lazio 20,2, Veneto 20,2, Toscana 20,4, Liguria 20,4, Lombardia 20,7, Emilia Romagna 21,5. Media Italia 19,5.">Rapporto alunni/classe per regione, 2024/2025.</canvas>
    </div>
  </div>

  <div class="insight">
    <strong>Un divario Nord-Sud rovesciato rispetto alle aspettative:</strong> le regioni con il rapporto alunni/classe più basso (classi più piccole) sono in gran parte meridionali e insulari — Molise (16,6), Basilicata (16,7), Sardegna (16,8), Calabria (17,2) — mentre Emilia Romagna (21,5) e Lombardia (20,7) hanno le classi più numerose. Questo non significa necessariamente "più risorse per alunno" al Sud: è in larga parte un effetto della dispersione demografica e della rete di piccole scuole di montagna o a bassa densità abitativa, dove le classi restano sotto la soglia dimensionale media anche a fronte di un numero di alunni in calo (vedi serie storica più sotto), non di scelte di investimento aggiuntivo.
  </div>

  <div style="overflow-x:auto; margin-bottom:1.5rem;">
    <table class="data-table">
      <thead>
        <tr>
          <th>Regione</th>
          <th class="num">Alunni</th>
          <th class="num">Classi</th>
          <th class="num">Alunni/classe</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Piemonte</td><td class="num">493.904</td><td class="num">25.382</td><td class="num">19,5</td></tr>
        <tr><td>Lombardia</td><td class="num">1.116.821</td><td class="num">53.993</td><td class="num">20,7</td></tr>
        <tr><td>Veneto</td><td class="num">549.314</td><td class="num">27.212</td><td class="num">20,2</td></tr>
        <tr><td>Friuli Venezia Giulia</td><td class="num">132.950</td><td class="num">7.185</td><td class="num">18,5</td></tr>
        <tr><td>Liguria</td><td class="num">163.052</td><td class="num">7.984</td><td class="num">20,4</td></tr>
        <tr><td>Emilia Romagna</td><td class="num">531.037</td><td class="num">24.691</td><td class="num">21,5</td></tr>
        <tr><td>Toscana</td><td class="num">445.044</td><td class="num">21.770</td><td class="num">20,4</td></tr>
        <tr><td>Umbria</td><td class="num">108.344</td><td class="num">5.596</td><td class="num">19,4</td></tr>
        <tr><td>Marche</td><td class="num">194.269</td><td class="num">9.729</td><td class="num">20,0</td></tr>
        <tr><td>Lazio</td><td class="num">684.030</td><td class="num">33.848</td><td class="num">20,2</td></tr>
        <tr><td>Abruzzo</td><td class="num">160.852</td><td class="num">8.401</td><td class="num">19,2</td></tr>
        <tr><td>Molise</td><td class="num">33.689</td><td class="num">2.031</td><td class="num">16,6</td></tr>
        <tr><td>Campania</td><td class="num">787.901</td><td class="num">42.789</td><td class="num">18,4</td></tr>
        <tr><td>Puglia</td><td class="num">517.033</td><td class="num">26.997</td><td class="num">19,2</td></tr>
        <tr><td>Basilicata</td><td class="num">67.462</td><td class="num">4.034</td><td class="num">16,7</td></tr>
        <tr><td>Calabria</td><td class="num">250.595</td><td class="num">14.536</td><td class="num">17,2</td></tr>
        <tr><td>Sicilia</td><td class="num">660.629</td><td class="num">35.441</td><td class="num">18,6</td></tr>
        <tr><td>Sardegna</td><td class="num">176.661</td><td class="num">10.496</td><td class="num">16,8</td></tr>
        <tr class="ita"><td><strong>Italia</strong></td><td class="num"><strong>7.073.587</strong></td><td class="num"><strong>362.115</strong></td><td class="num"><strong>19,5</strong></td></tr>
      </tbody>
    </table>
  </div>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Serie storica alunni, classi e posti comuni — AA.SS. 2018/2019-2024/2025 (variazione % vs 2017/2018)</div>
    <span class="source-tag static"><span class="source-dot"></span>MIM — Ufficio di Statistica, Focus "Principali dati della scuola", settembre 2024 (Graf. 4)</span>
    <div class="canvas-wrap" style="height:300px;">
      <canvas id="istSerieStoricaChart" role="img" aria-label="Variazione percentuale rispetto al 2017/2018: alunni in calo costante, da -1,0% nel 2018/19 a -8,9% nel 2024/25. Classi in calo dal 2022/23, da +0,5% a -2,6% nel 2024/25. Posti comuni in leggero aumento, tra +0,2% e +1,7%, con picco a +1,7% nel 2022/23.">Serie storica alunni, classi e posti comuni, 2018/19-2024/25.</canvas>
    </div>
  </div>

  <div class="insight">
    <strong>Meno alunni, ma non proporzionalmente meno classi né meno posti:</strong> tra il 2017/18 e il 2024/25 gli alunni sono calati dell'8,9%, ma le classi solo del 2,6% (e con ritardo, a partire dal 2022/23) e i posti comuni sono addirittura leggermente aumentati. È l'effetto combinato del calo demografico strutturale italiano e di una rete scolastica che si adatta più lentamente — chiudere una sezione o una sede richiede tempi amministrativi più lunghi della semplice contrazione del numero di iscritti, specie nei territori a bassa densità.
  </div>
</section>

<!-- SEZIONE 3: ORGANICO E SOSTEGNO -->
<section class="section" id="ist-organico">
  <div class="section-header">
    <span class="section-num">03 /</span>
    <h2 class="section-title">Organico docente e sostegno per disabilità</h2>
  </div>
  <p class="section-desc">I posti istituiti per l'A.S. 2024/2025 sono complessivamente <strong>684.583 posti comuni</strong> (di cui 14.142 "per l'adeguamento dell'organico") e <strong>205.253 posti di sostegno</strong> (di cui 79.083 "in deroga"). Il dato sul sostegno in deroga, alla data della rilevazione, era riferito ancora al 5 settembre 2023 ed era segnalato dal MIM come "in via di aggiornamento" — va quindi letto con cautela, soprattutto nel confronto anno su anno più sotto.</p>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Alunni con disabilità per posto di sostegno, per regione — A.S. 2024/2025</div>
    <span class="source-tag static"><span class="source-dot"></span>MIM — Ufficio di Statistica, Focus "Principali dati della scuola", settembre 2024 (Tab. 4 e Tab. 13)</span>
    <div class="canvas-wrap" style="height:480px;">
      <canvas id="istSostegnoRegioneChart" role="img" aria-label="Alunni con disabilità per posto di sostegno per regione, dal più basso (migliore) al più alto (peggiore): Piemonte 1,24, Umbria 1,20, Marche 1,27, Molise 1,27, Abruzzo 1,31, Calabria 1,30, Sicilia 1,32, Basilicata 1,35, Toscana 1,38, Lazio 1,56, Veneto 1,73, Friuli Venezia Giulia 1,84, Puglia 1,81, Emilia Romagna 1,64, Campania 2,00, Liguria 2,27, Lombardia 2,22. Media Italia 1,61.">Alunni con disabilità per posto di sostegno, per regione.</canvas>
    </div>
  </div>

  <div class="insight">
    <strong>La copertura del sostegno varia moltissimo da regione a regione:</strong> in Lombardia ci sono in media 2,22 alunni con disabilità per ogni posto di sostegno, quasi il doppio che in Piemonte o Umbria (1,20-1,24). Non è possibile stabilire da questo solo dato se la differenza rifletta bisogni diversi (gravità/tipologia delle disabilità), organizzazione didattica diversa (compresenza, gruppi di lavoro) o effettiva minore disponibilità di risorse — ma il divario, quasi 2 a 1 tra le regioni agli estremi, è ampio abbastanza da meritare un approfondimento dedicato in futuro, incrociando questo dato con la gravità delle certificazioni (L. 104/92, commi 1 e 3).
  </div>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Alunni con disabilità e posti di sostegno — serie storica AA.SS. 2018/2019-2024/2025</div>
    <span class="source-tag static"><span class="source-dot"></span>MIM — Ufficio di Statistica, Focus "Principali dati della scuola", settembre 2024 (Graf. 5)</span>
    <div style="display:flex;flex-wrap:wrap;gap:12px;margin:0.75rem 0;font-size:11px;color:var(--is-ink-3);">
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#c0392b;display:inline-block;"></span>Alunni con disabilità</span>
      <span style="display:flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;border-radius:2px;background:#1baf7a;display:inline-block;"></span>Posti di sostegno</span>
    </div>
    <div class="canvas-wrap" style="height:300px;">
      <canvas id="istDisabilitaSostegnoChart" role="img" aria-label="Alunni con disabilità in aumento costante: da 256.296 nel 2018/19 a 331.124 nel 2024/25. Posti di sostegno in aumento fino al 2023/24 (234.460), poi in calo apparente a 205.253 nel 2024/25.">Serie storica alunni con disabilità e posti di sostegno.</canvas>
    </div>
  </div>

  <div class="insight" style="border-color: var(--is-ink-3);">
    <strong>Attenzione a leggere il calo 2024/25 come un vero calo di risorse:</strong> il grafico mostra i posti di sostegno scendere da 234.460 (2023/24) a 205.253 (2024/25), mentre gli alunni con disabilità continuano a salire (331.124). Ma, come segnalato dal MIM stesso, la componente "posti in deroga" (79.083 dei 205.253 totali) era alla data della rilevazione ancora riferita al 5 settembre 2023 e in fase di aggiornamento da parte degli Uffici periferici — i posti in deroga vengono tipicamente assegnati più avanti nell'anno scolastico, in base alle certificazioni effettive. Il calo apparente potrebbe quindi essere, almeno in parte, un artefatto della data di rilevazione (a chiusura organico "di fatto" iniziale) piuttosto che un vero disinvestimento — un punto che richiederebbe un dato più aggiornato per essere confermato o escluso.
  </div>
</section>

<!-- SEZIONE 4: INDIRIZZI SECONDARIA II GRADO -->
<section class="section" id="ist-indirizzi">
  <div class="section-header">
    <span class="section-num">04 /</span>
    <h2 class="section-title">Indirizzi di studio nella secondaria di II grado</h2>
  </div>
  <p class="section-desc">Dei 2.619.287 studenti della secondaria di II grado statale, la ripartizione per macro-percorso di studio (A.S. 2024/2025):</p>

  <div class="chart-wrap" style="margin-bottom:1.5rem;">
    <div class="chart-title">Studenti per percorso di studio — Secondaria di II grado, A.S. 2024/2025</div>
    <span class="source-tag static"><span class="source-dot"></span>MIM — Ufficio di Statistica, Focus "Principali dati della scuola", settembre 2024 (Tab. 7)</span>
    <div class="canvas-wrap" style="height:320px;">
      <canvas id="istIndirizziChart" role="img" aria-label="Ripartizione studenti secondaria di II grado per percorso: Licei 51,4% (1.346.023 studenti), Tecnici 31,8% (832.365), Professionali 16,8% (440.899).">Studenti per percorso di studio, secondaria di II grado.</canvas>
    </div>
  </div>

  <div class="insight">
    <strong>Più della metà degli studenti delle superiori italiane sceglie un liceo:</strong> il percorso liceale (51,4%) supera da solo la somma di tecnici e professionali insieme in molte singole regioni — anche se, come mostrano i bilanci regionali (Tab. 10 della fonte), la proporzione varia: Lazio e Campania hanno una quota di liceali sopra il 60%, mentre in Veneto e Friuli Venezia Giulia tecnici e professionali insieme superano il 55% degli studenti.
  </div>
</section>

<!-- SEZIONI ANCORA DA COMPLETARE -->
<section class="section" id="ist-limiti" style="border-bottom:none;">
  <div class="section-header">
    <span class="section-num">— /</span>
    <h2 class="section-title">Dimensioni ancora da completare</h2>
  </div>
  <p class="section-desc">Per completezza, le due dimensioni previste per questa pagina ma non ancora popolate con dati verificati:</p>
  <div class="insight" style="border-color: var(--is-ink-3);">
    <strong>Confronto europeo:</strong> serve un confronto Eurostat GF09 (spesa istruzione in % PIL, per paese e serie storica Italia) più OCSE "Education at a Glance" (spesa per studente comparata a livello internazionale), costruito con la stessa architettura già usata per la pagina <a href="{{ '/pubblica-amministrazione/' | relative_url }}">Pubblica Amministrazione</a> — non ancora realizzato per l'istruzione in modo dedicato (il dato che compare nella <a href="{{ '/spesa-pubblica/' | relative_url }}#confronto">panoramica generale</a> è un riferimento statico 2023, non aggiornato via Eurostat).
  </div>
  <div class="insight" style="margin-top:1rem; border-color: var(--is-ink-3);">
    <strong>Spesa per regione:</strong> la scuola statale è competenza dello Stato centrale in Italia (a differenza della sanità), quindi non esiste una voce di "spesa regionale per istruzione" a sé stante nei bilanci regionali. Un proxy possibile è il costo del personale scolastico per regione dal Conto Annuale RGS (già usato per la pagina Pubblica Amministrazione) — non ancora costruito per questa pagina.
  </div>
</section>

</main>

</div>

<footer class="pens-footer">
  <div style="max-width:980px; margin:0 auto;">
    Fonti: MIM — Nota Integrativa al disegno di Legge di Bilancio 2025-2027 (spesa); MIM — Ufficio di Statistica, Focus "Principali dati della scuola — Avvio Anno Scolastico 2024/2025", settembre 2024 (alunni, classi, organico).<br>
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

  // ── GRAFICO: Missione 1 per Programma, CP 2025 ──
  (function() {
    const ctx = document.getElementById('istMissioneChart').getContext('2d');
    const dati = [
      {p:'1.4 — ITS / terziaria non universitaria', v:0.05},
      {p:'1.2 — Sviluppo sistema / diritto studio', v:0.21},
      {p:'1.5 — Politiche territoriali / USR', v:0.22},
      {p:'1.8 — Reclutamento e aggiornamento', v:0.43},
      {p:'1.3 — Scuole non statali / paritarie', v:0.70},
      {p:'1.9 — Edilizia scolastica e sicurezza', v:1.20},
      {p:'1.1 — Programmazione e coordinamento', v:1.67},
      {p:'1.7 — Secondo ciclo', v:18.27},
      {p:'1.6 — Primo ciclo', v:34.00}
    ];
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: dati.map(d => d.p),
        datasets: [{
          label: 'Miliardi €',
          data: dati.map(d => d.v),
          backgroundColor: dati.map(d => d.v >= 10 ? '#c0392b' : '#2a78d6'),
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

  // ── GRAFICO: Scomposizione primo/secondo ciclo per natura spesa ──
  (function() {
    const ctx = document.getElementById('istScomposizioneChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Personale docenti', 'Dirigenti e ATA', 'Sostegno BES', 'Funzionamento istituti', 'Continuità/supplenze', 'Miglioramento offerta'],
        datasets: [
          { label: 'Primo ciclo', data: [64.8, 12.5, 18.8, 1.1, 2.8, null], backgroundColor: '#2a78d6', borderRadius: 3 },
          { label: 'Secondo ciclo', data: [66.5, 16.3, 12.5, 1.1, 2.6, 0.9], backgroundColor: '#c0392b', borderRadius: 3 }
        ]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: true, labels: { font: { size: 11, family: "'IBM Plex Mono', monospace" }, color: '#7a7a7a', boxWidth: 20 } },
          tooltip: { callbacks: { label: ctx => ` ${ctx.dataset.label}: ${ctx.parsed.y}%` } }
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 10 }, color: '#7a7a7a' } },
          y: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + '%' } }
        }
      }
    });
  })();

  // ── GRAFICO: Rapporto alunni/classe per ordine ──
  (function() {
    const ctx = document.getElementById('istRapportoOrdineChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Infanzia\n(bambini/sezione)', 'Primaria', 'Secondaria\ndi I grado', 'Secondaria\ndi II grado'],
        datasets: [{
          label: 'Alunni/classe',
          data: [19.7, 18.0, 19.7, 20.9],
          backgroundColor: '#2a78d6',
          borderRadius: 3
        }]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: { label: ctx => ` ${ctx.parsed.y} alunni per classe` } }
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#7a7a7a' } },
          y: { grid: { color: '#e0ddd4' }, min: 0, max: 24, ticks: { font: { size: 11 }, color: '#7a7a7a' } }
        }
      }
    });
  })();

  // ── GRAFICO: Rapporto alunni/classe per regione ──
  (function() {
    const ctx = document.getElementById('istRapportoRegioneChart').getContext('2d');
    const dati = [
      {r:'Molise', v:16.6}, {r:'Basilicata', v:16.7}, {r:'Sardegna', v:16.8}, {r:'Calabria', v:17.2},
      {r:'Friuli Venezia Giulia', v:18.5}, {r:'Campania', v:18.4}, {r:'Sicilia', v:18.6}, {r:'Abruzzo', v:19.2},
      {r:'Puglia', v:19.2}, {r:'Umbria', v:19.4}, {r:'Piemonte', v:19.5}, {r:'Marche', v:20.0},
      {r:'Veneto', v:20.2}, {r:'Lazio', v:20.2}, {r:'Toscana', v:20.4}, {r:'Liguria', v:20.4},
      {r:'Lombardia', v:20.7}, {r:'Emilia Romagna', v:21.5}
    ].sort((a,b) => a.v - b.v);
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: dati.map(d => d.r),
        datasets: [{
          label: 'Alunni/classe',
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
          tooltip: { callbacks: { label: ctx => ` ${ctx.parsed.x} alunni per classe` } }
        },
        scales: {
          x: { grid: { color: '#e0ddd4' }, min: 14, ticks: { font: { size: 11 }, color: '#7a7a7a' },
            title: { display: true, text: 'Alunni per classe', font: { size: 10 }, color: '#7a7a7a' } },
          y: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#0d0d0d' } }
        }
      }
    });
  })();

  // ── GRAFICO: Serie storica alunni/classi/posti comuni ──
  (function() {
    const ctx = document.getElementById('istSerieStoricaChart').getContext('2d');
    const anni = ['2018/19','2019/20','2020/21','2021/22','2022/23','2023/24','2024/25'];
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: anni,
        datasets: [
          { label: 'Alunni', data: [-1.0,-1.5,-3.1,-4.7,-5.1,-7.1,-8.9], borderColor: '#c0392b', backgroundColor: 'transparent', borderWidth: 2.5, pointRadius: 4, tension: 0.2 },
          { label: 'Classi', data: [null,0.8,0.7,0.7,1.4,-1.4,-2.6], borderColor: '#2a78d6', backgroundColor: 'transparent', borderWidth: 2.5, pointRadius: 4, tension: 0.2, spanGaps: true },
          { label: 'Posti comuni', data: [0.4,0.8,0.7,0.7,1.7,0.8,0.8], borderColor: '#1baf7a', backgroundColor: 'transparent', borderWidth: 2.5, pointRadius: 4, tension: 0.2 }
        ]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: true, labels: { font: { size: 11, family: "'IBM Plex Mono', monospace" }, color: '#7a7a7a', boxWidth: 20 } },
          tooltip: { callbacks: { label: ctx => ` ${ctx.dataset.label}: ${ctx.parsed.y}%` } }
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#7a7a7a' } },
          y: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => v + '%' } }
        }
      }
    });
  })();

  // ── GRAFICO: Alunni con disabilità per posto sostegno, per regione ──
  (function() {
    const ctx = document.getElementById('istSostegnoRegioneChart').getContext('2d');
    const dati = [
      {r:'Umbria', v:1.20}, {r:'Piemonte', v:1.24}, {r:'Marche', v:1.27}, {r:'Molise', v:1.27},
      {r:'Abruzzo', v:1.31}, {r:'Calabria', v:1.30}, {r:'Sicilia', v:1.32}, {r:'Basilicata', v:1.35},
      {r:'Toscana', v:1.38}, {r:'Lazio', v:1.56}, {r:'Veneto', v:1.73}, {r:'Puglia', v:1.81},
      {r:'Friuli Venezia Giulia', v:1.84}, {r:'Emilia Romagna', v:1.64}, {r:'Campania', v:2.00},
      {r:'Liguria', v:2.27}, {r:'Lombardia', v:2.22}
    ].sort((a,b) => a.v - b.v);
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: dati.map(d => d.r),
        datasets: [{
          label: 'Alunni con disabilità / posto sostegno',
          data: dati.map(d => d.v),
          backgroundColor: dati.map(d => d.v > 2 ? '#c0392b' : '#2a78d6'),
          borderRadius: 3
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: { label: ctx => ` ${ctx.parsed.x.toFixed(2)} alunni con disabilità per posto` } }
        },
        scales: {
          x: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a' },
            title: { display: true, text: 'Alunni con disabilità per posto di sostegno', font: { size: 10 }, color: '#7a7a7a' } },
          y: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#0d0d0d' } }
        }
      }
    });
  })();

  // ── GRAFICO: Alunni con disabilità vs posti sostegno, serie storica ──
  (function() {
    const ctx = document.getElementById('istDisabilitaSostegnoChart').getContext('2d');
    const anni = ['2018/19','2019/20','2020/21','2021/22','2022/23','2023/24','2024/25'];
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: anni,
        datasets: [
          { label: 'Alunni con disabilità', data: [256296,269684,277414,287039,312235,321185,331124], borderColor: '#c0392b', backgroundColor: 'rgba(192,57,43,0.06)', borderWidth: 2.5, pointRadius: 4, fill: true, tension: 0.2 },
          { label: 'Posti di sostegno', data: [165970,177750,184834,217503,220728,234460,205253], borderColor: '#1baf7a', backgroundColor: 'rgba(27,175,122,0.06)', borderWidth: 2.5, pointRadius: 4, fill: true, tension: 0.2 }
        ]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: true, labels: { font: { size: 11, family: "'IBM Plex Mono', monospace" }, color: '#7a7a7a', boxWidth: 20 } },
          tooltip: { callbacks: { label: ctx => ` ${ctx.dataset.label}: ${ctx.parsed.y.toLocaleString('it-IT')}` } }
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 11 }, color: '#7a7a7a' } },
          y: { grid: { color: '#e0ddd4' }, ticks: { font: { size: 11 }, color: '#7a7a7a', callback: v => (v/1000) + 'k' } }
        }
      }
    });
  })();

  // ── GRAFICO: Indirizzi secondaria II grado ──
  (function() {
    const ctx = document.getElementById('istIndirizziChart').getContext('2d');
    new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: ['Licei', 'Tecnici', 'Professionali'],
        datasets: [{
          data: [51.4, 31.8, 16.8],
          backgroundColor: ['#2a78d6', '#e0a638', '#c0392b'],
          borderWidth: 0
        }]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: {
          legend: { display: true, position: 'bottom', labels: { font: { size: 12, family: "'IBM Plex Mono', monospace" }, color: '#3a3a3a', boxWidth: 14 } },
          tooltip: { callbacks: { label: ctx => ` ${ctx.label}: ${ctx.parsed}%` } }
        }
      }
    });
  })();
});
</script>
