# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Stonescript'
copyright = '2023, Martian Rex Inc.'
author = 'Deechi, Martian Rex'

release = '0.1'
version = '3.32.3'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

html_static_path = ['_static']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_css_files = [
    'css/custom.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote'
