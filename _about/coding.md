---
title: "Coding"
---
{% assign skills = site.data.skills %}

Through my education, my work experience, and in doing personal projects
I have used many computer-related skills on projects of various sizes.

Here are some of the programming languages I've been able to use in my time.

{% for skill in skills.programming_languages %}
  - {{ skill }}
{% endfor %}

I've also been able to use a lot of languages, frameworks, and skills
used in web development.

{% for skill in skills.web_development %}
  - {{ skill }}
{% endfor %}

In addition, I've gotten to try some things
that don't necessarily fit into either of the above categories,
or that serve a more specific use.

{% for skill in skills.misc_programming %}
  - {{ skill }}
{% endfor %}
