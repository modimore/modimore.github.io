---
---
nav_toggle = document.getElementById('nav-toggle');

function toggle_nav_links(event) {
	var nav_link_lists = document.getElementsByClassName('nav-links');

	if (event.target == nav_toggle || nav_toggle.parentElement.contains(event.target)) {
		for (var i = 0; i < nav_link_lists.length; i++) {
			nav_link_lists[i].classList.add("expanded");
		}
	}
	else {
		for (var i = 0; i < nav_link_lists.length; i++) {
			nav_link_lists[i].classList.remove("expanded");
		}
	}
	event.stopPropagation();
}

document.addEventListener('click', toggle_nav_links);
document.addEventListener('touchstart', toggle_nav_links);
