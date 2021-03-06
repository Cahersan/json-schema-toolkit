# -*- coding: utf-8 -*-
#
# This document is free and open-source software, subject to the OSI-approved
# BSD license below.
#
# Copyright (c) 2013 Alexis Petrounias <www.petrounias.org>,
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# * Neither the name of the author nor the names of its contributors may be used
# to endorse or promote products derived from this software without specific
# prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

""" Sphinx configuration for JSON Schema Toolkit.
"""

__status__ = "alpha"
__version__ = "1.0.0a1"
__maintainer__ = (u"Alexis Petrounias <www.petrounias.org>", )
__author__ = (u"Alexis Petrounias <www.petrounias.org>", )

# Python
import sys, os


sys.path.append(os.path.abspath('../..'))

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'JSON Schema Toolkit'
copyright = u'2013 Alexis Petrounias <www.petrounias.org>'

version = '1.0.0'
release = '1.0.0a1'

pygments_style = 'sphinx'

html_theme = 'default'

html_static_path = ['_static']

htmlhelp_basename = 'JSONSchemaToolkitdoc'

latex_documents = [
  ('index', 'JSONSchemaToolkit.tex', u'JSON Schema Toolkit Documentation',
   u'Alexis Petrounias \\textless{}www.petrounias.org\\textgreater{}', 'manual'),
]

man_pages = [
    ('index', 'jsonschematoolkit', u'JSON Schema Toolkit Documentation',
     [u'Alexis Petrounias <www.petrounias.org>'], 1)
]

texinfo_documents = [
  ('index', 'JSONSchemaToolkit', u'JSON Schema Toolkit Documentation',
   u'Alexis Petrounias <www.petrounias.org>', 'JSONSchemaToolkit',
  'Programmatic building of JSON schemas (recursive field mappings) with validation, a Django JSON Field, and native PostgreSQL JSON type constraints.',
   'Miscellaneous'),
]
