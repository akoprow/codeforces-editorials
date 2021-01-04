<div class="alert alert-primary" role="alert">
  {% assign problem = site.data.problems | find:'id',include.id %}
  <tiny>{{include.id | slice:0,4}}</tiny>{{include.id | slice:4,2}}{% if problem.also-as %} / <tiny>{{problem.also-as | slice:0,4}}</tiny>{{problem.also-as | slice:4,2}}{% endif %}

  {% capture link %}/problems/{{include.id | slugify}}.html{% endcapture %}
  <a href="{{ link }}">
    {{problem.title}}
  </a>
  <a href="https://codeforces.com/contest/{{include.id | slice:0,4}}/problem/{{include.id | slice:4,2}}">
  [CF]
  </a>

  {% if problem.code %}<a href="https://github.com/akoprow/competetive-programming/blob/master/src/codeforces/{{include.code}}">(Code)</a>{% endif %}

  {% if problem.rating %}<rating>R:{{problem.rating}} <meter min=800 max=3600 value="{{problem.rating}}"/></rating>{% endif %}

  <labels>
  {% assign labels = problem.labels | split: ", " %}
  {% for label in labels %}
    <span class="badge rounded-pill bg-warning text-dark">{{label}}</span>
  {% endfor %}
  </labels>
</div>
