---
layout: default
title: Home
description: "Dati pubblici italiani verificati: spesa pubblica, proprietà societarie, carriere politiche, norme. Fonti citate, metodologia trasparente, nessuna narrazione."
---

<p class="prose__kicker" style="margin-top:34px;">Presentazione</p>
<p style="max-width: 64ch; font-size: 17.5px;">
  L'Osservatorio raccoglie dati pubblici italiani — spesa pubblica, proprietà
  societaria, carriere politiche, cornici normative, e altro nel tempo — per
  comporre, un fascicolo alla volta, un ritratto dell'Italia in dati e fatti.
  I dati sono ricercati con l'aiuto dell'intelligenza artificiale e verificati
  alla fonte; dove il dato da solo non basta, si aggiunge un commento umano,
  segnalato come tale. Le conclusioni restano al lettore. Ogni dato pubblicato
  riporta la fonte, la data di aggiornamento e i limiti noti — si veda la
  <a href="{{ '/metodologia/' | relative_url }}">nota metodologica</a>.
</p>

<ol class="titoli">
  {% for t in site.titoli %}
  <li class="titolo-entry">
    <div class="titolo-entry__numero">Titolo<span>{{ t.numero }}</span></div>
    <div>
      <h2 class="titolo-entry__titolo"><a href="{{ '/' | append: t.slug | append: '/' | relative_url }}">{{ t.titolo }}</a></h2>
      <p class="titolo-entry__sommario">{{ t.sommario }}</p>
    </div>
    <span class="stato {% if t.stato == 'attivo' %}stato--attivo{% else %}stato--dev{% endif %}">{{ t.stato }}</span>
  </li>
  {% endfor %}
</ol>
