{% include problemHeader.md id=include.id %}

{% capture content %}p/{{include.id | slice:0,3}}/{{include.id}}.md{% endcapture %}
{% include {{ content }} %}
