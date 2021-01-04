---
layout: page
title: Problems
---

<ul>

{% for problem in site.data.problems %}
{% if problem.code %}
<li>
  <tiny>{{problem.id | slice:0,4}}</tiny>{{problem.id | slice:4,2}}{% if problem.also-as %} / <tiny>{{problem.also-as | slice:0,4}}</tiny>{{problem.also-as | slice:4,2}}{% endif %}

  {% capture link %}{{problem.id | slugify}}.html{% endcapture %}
  <a href="{{ link }}">
    {{problem.title}}
  </a>

  {% if problem.rating %}<rating>R:{{problem.rating}} <meter min=800 max=3600 value="{{problem.rating}}"/></rating>{% endif %}

  <labels>
  {% assign labels = problem.labels | split: ", " %}
  {% for label in labels %}
    <span class="badge tiny rounded-pill bg-warning text-dark">{{label}}</span>
  {% endfor %}
  </labels>
{% endif %}
{% endfor %}
