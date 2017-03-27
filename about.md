---
layout: page
title: About
permalink: /about/
sitenav_visible: true
---

{% for page in site.about %}
[{{page.title}}]({{page.url}})
{% endfor %}
