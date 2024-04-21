# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "my-moddd"
copyright = "2024, tirol30"
author = "tirol30"
release = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []
extensions = [
    "sphinx.ext.autodoc",  # ソースコード読み込み用
    "numpydoc",  # docstring パース用
    "sphinx_rtd_theme",  # Read the Docs テーマ (今回は不要*1)
    # "sphinx_multiversion",  # マルチバージョン用
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
