* * *

# **<tiny>{{include.id | slice:0,4}}</tiny>{{include.id | slice:4,2}}{% if include.also-as %} / <tiny>{{include.also-as | slice:0,4}}</tiny>{{include.also-as | slice:4,2}}{% endif %}** [{{include.name}}](https://codeforces.com/contest/{{include.id | slice:0,4}}/problem/{{include.id | slice:4,2}}) {% if include.rating %}{% include rating.md %}{% endif %}

{% include labels.md %}
