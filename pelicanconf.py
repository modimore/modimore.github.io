#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Quinn Mortimer'
SITENAME = 'modimore.github.io'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['articles']

OUTPUT_PATH = '../pelican-build'
DELETE_OUTPUT_DIRECTORY = True

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

# Blogroll
LINKS = [('BreezeBlocks on RtD', 'https://pypi.python.org/pypi/breezeblocks/'),
         ('BreezeBlocks on PyPi', 'https://breezeblocks.readthedocs.io/en/latest'),
         ('Pythia Discord Bot', 'https://discordapp.com/oauth2/authorize?client_id=202861748133298177&scope=bot&permissions=3072')
        ]

# Social widget
SOCIAL = [('GitHub', 'https://github.com/modimore'),
         ]

DEFAULT_PAGINATION = 2

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
