# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# Problems with imports? Could try `export PYTHONPATH=$PYTHONPATH:`pwd`` from root project dir...
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))  # Source code dir relative to this file

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
add_module_names = False # Remove namespaces from class/method signatures
autoapi_add_toctree_entry = True
autoapi_dirs = ['../../porf']
autoapi_keep_files = True
autoapi_template_dir = '_autoapi_templates'
autosummary_generate = True  # Turn on sphinx.ext.autosummary
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries
autodoc_inherit_docstrings = True  # If no docstring, inherit from base class
author = 'Dario Quintero'
copyright = '2023, Dario Quintero'
exclude_patterns = []
extensions = [
    "autoapi.extension",
    'IPython.sphinxext.ipython_console_highlighting',
    'nbsphinx',  # Integrate Jupyter Notebooks and Sphinx
    'myst_parser',
    'sphinx.ext.autodoc',  # Core Sphinx library for auto html doc generation from docstrings
    'sphinx.ext.autosummary',  # Create neat summary tables for modules/classes/methods etc
    'sphinx.ext.coverage',
    'sphinx.ext.intersphinx',  # Link to other project's documentation (see mapping below)
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    "sphinx.ext.todo",
    'sphinx.ext.viewcode',  # Add a link to the Python source code for classes, functions etc.
    'sphinx_autodoc_typehints', # Automatically document param types (less noise in class signature)
    "sphinx_gallery.load_style",
    'sphinx-pydantic',
]
html_show_sourcelink = False  # Remove 'view source code' from top of page (for html, not python)
html_static_path = ['_static']
html_theme = 'alabaster'
project = 'porf'
set_type_checking_flag = True  # Enable 'expensive' imports for sphinx_autodoc_typehints
source_suffix = ['.rst', '.md']
templates_path = ['_templates']
mathjax3_config = {
    'tex': {'tags': 'ams', 'useLabelIds': True},
}
nbsphinx_allow_errors = True  # Continue through Jupyter errors

# nbsphinx_custom_formats = {
#     ".md": ["jupytext.reads", {"fmt": "mystnb"}],
# }

#autodoc_typehints = "description" # Sphinx-native method. Not as good as sphinx_autodoc_typehints
