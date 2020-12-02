* * *

# **<small>{{include.id | slice:0,4}}</small>{{include.id | slice:4,2}}{% if include.also-as %} / <small>{{include.also-as | slice:0,4}}</small>{{include.also-as | slice:4,2}}{% endif %}** [{{include.name}}](https://codeforces.com/contest/{{include.id | slice:0,4}}/problem/{{include.id | slice:4,2}})

🏷 {{include.labels}} {% if include.code %}
[(Code)]({{include.code}})
{% endif %}
