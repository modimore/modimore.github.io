#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Quinn Mortimer'
SITENAME = 'modimore.github.io'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['articles']

OUTPUT_PATH = '../pelican-build'

# INDEX_SAVE_AS = 'articles.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
ARTICLE_URL = 'articles/{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'English'

THEME = 'themes/notmyidea-modified'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links
LINKS = [('GitHub', 'https://github.com/modimore'),
         ('BreezeBlocks','https://pypi.org/pypi/breezeblocks/'),
         ('Add Pythia', 'https://discordapp.com/oauth2/authorize?client_id=202861748133298177&scope=bot&permissions=3072'),
         ('BreezeBlocks ', 'https://breezeblocks.readthedocs.io/en/latest'),
        ]

# Flair
FLAIR = [('https://stackoverflow.com/users/7737781/quinn-mortimer', 'https://stackoverflow.com/users/flair/7737781.png?theme=clean', 'Stack Overflow profile for Quinn Mortimer'),
         ('https://projecteuler.net/profile/modimore.png', 'https://projecteuler.net/profile/modimore.png', 'Project Euler stats for Quinn Mortimer'),
        ]

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
