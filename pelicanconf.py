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
FAVICON = "https://s.gravatar.com/avatar/a77c137e29c981a27c69112de2ec3821?s=16"
PERSONAL_PHOTO = "https://s.gravatar.com/avatar/a77c137e29c981a27c69112de2ec3821?s=200"
PERSONAL_INFO = """I'm Brian Knobbs, an engineer of many sorts who specializes in solving hard
problems and making all the pieces fit. I'm a bit obsessive over design, a lot obsessive about
security and uncomfortably obsessed with juggling. I'm a huge fan of making things with my hands,
and I'm an advocate of Python, Django and open source software in general.
"""

WORK_DESCRIPTION = """
I am a Systems Engineer/Reverse Engineer for <a href="http://redlatice.com">REDLattice</a>, a
computer security research and programming services company working to help customers design,
architect and then build domain specific applications. We specialize in building highly scalable
systems, handling enormous amounts of data and building near-real-time web applications for
interacting with large data sets. Previously I have worked with high-end, embedded network
processing devices performing deep packet inspection and modification on high throughput (40Gb+)
links, building network intrusion detection systems and custom traffic filtering and modification
applications for specific networking protocols.

<br/><br/>
<h4>Disclaimer</h4>

<em>This is my personal website and blog. Opinions expressed here are solely mine, or those of the
author, not of my employer.</em>
"""

# Feed generation is usually not desired when developing
#FEED_RSS = 'feed/index.html'
#FEED_ATOM = 'feed/atom/index.html'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('GitHub', 'http://github.com/PacketPerception'),
         ('REDLattice', 'http://redlattice.com'))

# Social widget
SOCIAL = (('github', 'https://github.com/PacketPerception'),
          ('twitter', 'https://twitter.com/PktPerception'),
          ('linkedin', 'http://www.linkedin.com/in/brianknobbs'),
          ('envelope', 'mailto:brian@packetperception.com'))

DEFAULT_PAGINATION = 10
#PAGINATED_DIRECT_TEMPLATES = ('blog-index',)
#DIRECT_TEMPLATES = ('categories', 'index', 'blog-index', 'blog')

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

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
