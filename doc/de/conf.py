#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Language specific configuration file, inheriting from the main /doc
conf.py file and adjusting the variables that depend on the language.
"""

import os
import sys

sys.path.insert(0, os.path.abspath('..'))
from conf import *

language = 'de'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_autodoc/modules.rst']

html_theme_path = ['../']
html_logo = '../theme/static/qiskit-logo-white-no-margin.gif'
html_favicon = '../theme/static/favicon.ico'
