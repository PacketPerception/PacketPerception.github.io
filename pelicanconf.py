#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Brian Knobbs'
SITENAME = u'Packet Perception'
SITEURL = ''

PATH = 'content'

THEME = 'theme'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

#WITH_FUTURE_DATES = False
TEMPLATE_PAGES = {'blog.html': 'blog.html'}
STATIC_PATHS = ['images', 'extra/CNAME', 'extra/README']
EXTRA_PATH_METADATA = {'extra/README': {'path': 'README.md'}, 'extra/CNAME': {'path': 'CNAME'}}

# Feed generation is usually not desired when developing

# Feed generation is usually not desired when developing
#FEED_RSS = 'feed/index.html'
#FEED_ATOM = 'feed/atom/index.html'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/PacketPerception'),
          ('envelope', 'mailto:brian@packetperception.com'))

DEFAULT_PAGINATION = 10
#PAGINATED_DIRECT_TEMPLATES = ('blog-index',)
#DIRECT_TEMPLATES = ('categories', 'index', 'blog-index', 'blog')

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

#DEFAULT_DATE_FORMAT = ('%d/%b/%Y %a')

# Formatting for urls
#ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
#ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"

# ===theme settings===========================
POST_LIMIT = 3
#FAVICON = 'https://dl.dropboxusercontent.com/u/299446/logo.png'
#ICON = 'https://dl.dropboxusercontent.com/u/299446/logo.png'
#SHORTCUT_ICON = 'https://dl.dropboxusercontent.com/u/299446/logo.png'
DISQUS_SITENAME = 'packetperception'
