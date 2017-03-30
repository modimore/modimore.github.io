---
layout: page
title: About
permalink: /about/
sitenav_visible: true
---
<ul class="lw-group content-list">
	{% for page in site.about %}
		<li class="lw-cell-12-6">
			<a class="content-link" href="{{ page.url | prepend: site.basurl }}">{{ page.title }}</a>
		</li>
	{% endfor %}
</ul>
