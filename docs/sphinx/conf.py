# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# type: ignore

import os

# import matplotlib
from pkg_resources import parse_version

from lvmieb import __version__


# Are we building in RTD?
on_rtd = os.environ.get("READTHEDOCS") == "True"


# -- Project information -----------------------------------------------------

project = "lvmieb"
copyright = "{0}, {1}".format("2021", "SDSS LVMI softwareteam in Kyung Hee university")
author = "Changgon Kim, Mingyeong Yang, Taeeun Kim"

# The full version, including alpha/beta/rc tags
version = parse_version(__version__).base_version
release = __version__

# Are we building in RTD?
on_rtd = os.environ.get("READTHEDOCS") == "True"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
    "sphinx.ext.inheritance_diagram",
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_click",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "py:obj"

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

releases_github_path = "sdss/lvmieb"
releases_document_name = ["changelog"]
releases_unstable_prehistory = True

# Intersphinx mappings
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
# 'astropy': ('http://docs.astropy.org/en/latest', None),
# 'matplotlib': ('https://matplotlib.org/', None),
# 'scipy': ('https://docs.scipy.org/doc/scipy/reference', None)}

autodoc_mock_imports = ["_tkinter", "asynctest"]
autodoc_member_order = "groupwise"
autodoc_default_options = {"members": None, "show-inheritance": None}
autodoc_typehints = "description"

napoleon_use_rtype = False
napoleon_use_ivar = True

copybutton_prompt_text = r">>> |\$ "
copybutton_prompt_is_regexp = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "furo"
html_logo = "_static/sdssv_logo.png"
html_title = "lvmieb"
html_favicon = "./_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# See https://github.com/rtfd/readthedocs.org/issues/1776 for why we do this
if on_rtd:
    html_static_path = []
else:
    html_static_path = ["_static"]
