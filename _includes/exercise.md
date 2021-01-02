<div class="alert alert-primary" role="alert">
  <tiny>{{include.id | slice:0,4}}</tiny>{{include.id | slice:4,2}}{% if include.also-as %} / <tiny>{{include.also-as | slice:0,4}}</tiny>{{include.also-as | slice:4,2}}{% endif %}

  {{include.name}}
  <a href="https://codeforces.com/contest/{{include.id | slice:0,4}}/problem/{{include.id | slice:4,2}}">
  [CF]
  </a>

  {% if include.rating %}{% include rating.md %}{% endif %}

  <labels>
  {% assign labels = include.labels | split: ", " %}
  {% for label in labels %}
    <span class="badge rounded-pill bg-warning text-dark">{{label}}</span>
  {% endfor %}
  </labels>
</div>
