---
layout: default
title: "Titolo I — Della spesa pubblica"
---
<div class="prose">
<span class="prose__kicker">Titolo I</span>
<h1>Della spesa pubblica</h1>
<p>
  Bilanci, flussi e destinazione della finanza pubblica italiana, a confronto
  con i principali paesi dell'area euro. I dati sono scaricati da Eurostat
  periodicamente (una volta a settimana, via GitHub Actions) e pubblicati
  come file statico — non calcolati al momento della visita. Metodo descritto
  per esteso nella <a href="{{ '/metodologia/' | relative_url }}">nota metodologica</a>.
</p>

<p id="sp-stato" class="fonti">Caricamento dati…</p>

<div id="sp-charts" class="sp-charts"></div>

<p id="sp-fallback" class="callout" style="display:none;">
  <strong>Dati non disponibili.</strong> Il file statico non è stato trovato
  o non è leggibile. Riprova più tardi, o segnala il problema.
</p>

<p>Ambiti previsti in questa sezione, non ancora coperti dai grafici sopra:</p>
<ul>
  <li>Spesa pubblica italiana per funzione (COFOG), con serie storica pluriennale</li>
  <li>Voci di dettaglio della finanza pubblica oltre l'anno singolo</li>
</ul>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.4/chart.umd.min.js"></script>
<script>
(function () {
  var CATEGORIE = [
    { key: "totale",      titolo: "Spesa pubblica totale",     unit: "% del PIL" },
    { key: "debito",      titolo: "Debito pubblico",           unit: "% del PIL" },
    { key: "pensioni",    titolo: "Protezione sociale",        unit: "% del PIL" },
    { key: "sanita",      titolo: "Sanità",                    unit: "% del PIL" },
    { key: "istruzione",  titolo: "Istruzione",                unit: "% del PIL" },
    { key: "interessi",   titolo: "Interessi sul debito",      unit: "% del PIL" }
  ];

  var COLORE_ITALIA = "#7A342E";
  var COLORE_ALTRI = "#33455F";

  fetch("{{ '/assets/data/eurostat.json' | relative_url }}")
    .then(function (r) {
      if (!r.ok) { throw new Error("HTTP " + r.status); }
      return r.json();
    })
    .then(function (data) {
      var stato = document.getElementById("sp-stato");
      var d = new Date(data.generated_at);
      var dataFmt = d.toLocaleDateString("it-IT", { year: "numeric", month: "long", day: "numeric" });
      stato.innerHTML = "Fonte: " + data.source + " &middot; anno di riferimento " + data.year +
        " &middot; dati aggiornati il " + dataFmt +
        " &middot; <a href=\"" + data.source_url + "\">Eurostat</a>";

      var container = document.getElementById("sp-charts");

      CATEGORIE.forEach(function (cat) {
        var valori = data[cat.key];
        if (!valori || Object.keys(valori).length === 0) { return; }

        var voci = Object.keys(valori).map(function (geo) {
          return { geo: geo, valore: valori[geo] };
        });
        voci.sort(function (a, b) { return b.valore - a.valore; });

        var block = document.createElement("div");
        block.className = "sp-chart-block";

        var h = document.createElement("h3");
        h.className = "sp-chart-title";
        h.textContent = cat.titolo;
        block.appendChild(h);

        var canvasWrap = document.createElement("div");
        canvasWrap.className = "sp-chart-canvas";
        var canvas = document.createElement("canvas");
        canvasWrap.appendChild(canvas);
        block.appendChild(canvasWrap);

        container.appendChild(block);

        new Chart(canvas.getContext("2d"), {
          type: "bar",
          data: {
            labels: voci.map(function (v) { return v.geo; }),
            datasets: [{
              data: voci.map(function (v) { return v.valore; }),
              backgroundColor: voci.map(function (v) {
                return v.geo === "IT" ? COLORE_ITALIA : COLORE_ALTRI;
              }),
              borderRadius: 2,
              maxBarThickness: 28
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: {
                callbacks: {
                  label: function (ctx) { return ctx.parsed.y + " " + cat.unit; }
                }
              }
            },
            scales: {
              x: {
                grid: { display: false },
                ticks: { font: { family: "IBM Plex Mono", size: 11 } }
              },
              y: {
                grid: { color: "#D2CBB8" },
                ticks: { font: { family: "IBM Plex Mono", size: 11 } }
              }
            }
          }
        });
      });
    })
    .catch(function (err) {
      document.getElementById("sp-stato").style.display = "none";
      document.getElementById("sp-fallback").style.display = "block";
      console.error("Errore caricamento dati spesa pubblica:", err);
    });
})();
</script>

<style>
.sp-charts {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 28px;
  margin: 28px 0 36px;
}
.sp-chart-block {
  background: var(--paper-dim);
  border: 1px solid var(--line-soft);
  padding: 16px 18px 20px;
}
.sp-chart-title {
  font-family: var(--font-mono);
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--ink-soft);
  margin: 0 0 12px;
}
.sp-chart-canvas {
  position: relative;
  height: 220px;
}
</style>
