---
title: "Software Development"
---
{% assign skills = site.data.skills %}

In addition to just writing code, both at school and in my work experience I have had opportunities to develop skills in the related areas.

## Software Design

{% for skill in skills.software_development %}
  - {{ skill }}
{% endfor %}

## Teamwork and Project Management

{% for skill in skills.teamwork %}
 - {{ skill }}
{% endfor %}
