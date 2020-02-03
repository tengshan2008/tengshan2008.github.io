#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Master'
SITENAME = 'Personal Blog'
SITEURL = 'https://tengshan2008.github.com'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/medius'

STATIC_PATHS = ['images']

# Medius config
MEDIUS_CATEGORIES = {
    'Default': {
        'description': '默认文章',
        'logo': 'https://raw.githubusercontent.com/tengshan2008/tengshan2008.github.io/master/images/default-logo.jpg',
        'thumbnail': 'https://raw.githubusercontent.com/tengshan2008/tengshan2008.github.io/master/images/article-line.png'
    }
}

MEIDUS_AUTHORS = {
    'Master': '这个人很懒，什么都没有写。',
    'cover': 'https://raw.githubusercontent.com/tengshan2008/tengshan2008.github.io/master/images/banner.png',
    'image': 'https://raw.githubusercontent.com/tengshan2008/tengshan2008.github.io/master/images/author.jpg',
    'links': (('github-square', 'https://github.com/tengshan2008'),
              ('envelope-square', '#')),
}
