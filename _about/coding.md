---
title: "Coding"
---
{% assign skills = site.data.skills %}

Through my education, my work experience, and in doing personal projects
I have used many computer-related skills on projects of various sizes.

Here are some of the languages I've been able to use in my time.

{% for skill in skills.languages %}
  - {{ skill }}
{% endfor %}

In addition to the languages above, I have experience with these web frameworks.

{% for skill in skills.web_development %}
  - {{ skill }}
{% endfor %}

I've also got to work with some frameworks and APIS for game devlopment and graphics.

{% for skill in skills.game_dev_and_graphics %}
  - {{ skill }}
{% endfor %}
