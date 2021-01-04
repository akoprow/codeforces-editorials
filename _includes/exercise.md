<div class="alert alert-primary" role="alert">
  <tiny>{{include.id | slice:0,4}}</tiny>{{include.id | slice:4,2}}{% if include.also-as %} / <tiny>{{include.also-as | slice:0,4}}</tiny>{{include.also-as | slice:4,2}}{% endif %}

  {{include.name}}
  <a href="https://codeforces.com/contest/{{include.id | slice:0,4}}/problem/{{include.id | slice:4,2}}">
  [CF]
  </a>

  {% if include.code %}<a href="https://github.com/akoprow/competetive-programming/blob/master/src/codeforces/{{include.code}}">(Code)</a>{% endif %}

  {% if include.rating %}<rating>R:{{include.rating}} <meter min=800 max=3600 value="{{include.rating}}"/></rating>{% endif %}

  <labels>
  {% assign labels = include.labels | split: ", " %}
  {% for label in labels %}
    <span class="badge rounded-pill bg-warning text-dark">{{label}}</span>
  {% endfor %}
  </labels>
</div>
