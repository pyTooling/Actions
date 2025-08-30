# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
from sys import path as sys_path
from os.path import abspath
from pathlib import Path

from pyTooling.Packaging import extractVersionInformation

# ==============================================================================
# Project configuration
# ==============================================================================
githubNamespace = "pyTooling"
githubProject = "Actions"
pythonProject = "pyDummy"
directoryName = pythonProject.replace('.', '/')


# ==============================================================================
# Project paths
# ==============================================================================
ROOT = Path(__file__).resolve().parent

sys_path.insert(0, abspath("."))
sys_path.insert(0, abspath(".."))
sys_path.insert(0, abspath(f"../{directoryName}"))


# ==============================================================================
# Project information and versioning
# ==============================================================================
# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
packageInformationFile = Path(f"../{directoryName}/__init__.py")
versionInformation = extractVersionInformation(packageInformationFile)

author =    versionInformation.Author
copyright = versionInformation.Copyright
version =   ".".join(versionInformation.Version.split(".")[:2])  # e.g. 2.3    The short X.Y version.
release =   versionInformation.Version


# ==============================================================================
# Miscellaneous settings
# ==============================================================================
# The master toctree document.
master_doc = "index"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
	"_build",
	"_theme",
	"Thumbs.db",
	".DS_Store"
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "manni"


# ==============================================================================
# Restructured Text settings
# ==============================================================================
prologPath = Path("prolog.inc")
try:
	with prologPath.open("r", encoding="utf-8") as fileHandle:
		rst_prolog = fileHandle.read()
except Exception as ex:
	print(f"[ERROR:] While reading '{prologPath}'.")
	print(ex)
	rst_prolog = ""


# ==============================================================================
# Options for HTML output
# ==============================================================================
html_theme = "sphinx_rtd_theme"
html_theme_options = {
	"logo_only": True,
	"vcs_pageview_mode": 'blob',
	"navigation_depth": 5,
}
html_css_files = [
	'css/override.css',
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_logo = str(Path(html_static_path[0]) / "logo.png")
html_favicon = str(Path(html_static_path[0]) / "icon.png")

# Output file base name for HTML help builder.
htmlhelp_basename = f"{githubProject}Doc"

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
html_last_updated_fmt = "%d.%m.%Y"

# ==============================================================================
# Python settings
# ==============================================================================
modindex_common_prefix = [
	f"{pythonProject}."
]

# ==============================================================================
# Options for LaTeX / PDF output
# ==============================================================================
from textwrap import dedent

latex_elements = {
	# The paper size ('letterpaper' or 'a4paper').
	"papersize": "a4paper",

	# The font size ('10pt', '11pt' or '12pt').
	#'pointsize': '10pt',

	# Additional stuff for the LaTeX preamble.
	"preamble": dedent(r"""
		% ================================================================================
		% User defined additional preamble code
		% ================================================================================
		% Add more Unicode characters for pdfLaTeX.
		% - Alternatively, compile with XeLaTeX or LuaLaTeX.
		% - https://GitHub.com/sphinx-doc/sphinx/issues/3511
		%
		\ifdefined\DeclareUnicodeCharacter
			\DeclareUnicodeCharacter{2265}{$\geq$}
			\DeclareUnicodeCharacter{21D2}{$\Rightarrow$}
		\fi


		% ================================================================================
		"""),

	# Latex figure (float) alignment
	#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
	( master_doc,
		f"{githubProject}.tex",
		f"The {githubProject} Documentation",
		f"Patrick Lehmann",
		f"manual"
	),
]


# ==============================================================================
# Extensions
# ==============================================================================
extensions = [
# Standard Sphinx extensions
	"sphinx.ext.autodoc",
	"sphinx.ext.extlinks",
	"sphinx.ext.intersphinx",
	"sphinx.ext.inheritance_diagram",
	"sphinx.ext.todo",
	"sphinx.ext.graphviz",
	"sphinx.ext.mathjax",
	"sphinx.ext.ifconfig",
	"sphinx.ext.viewcode",
# SphinxContrib extensions
	"sphinxcontrib.mermaid",
# Other extensions
	"sphinx_design",
	"sphinx_copybutton",
	"sphinx_autodoc_typehints",
	"autoapi.sphinx",
	"sphinx_reports",
# User defined extensions
]


# ==============================================================================
# Sphinx.Ext.InterSphinx
# ==============================================================================
intersphinx_mapping = {
	"python":   ("https://docs.python.org/3", None),
}


# ==============================================================================
# Sphinx.Ext.AutoDoc
# ==============================================================================
# see: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration
#autodoc_default_options = {
#	"private-members": True,
#	"special-members": True,
#	"inherited-members": True,
#	"exclude-members": "__weakref__"
#}
#autodoc_class_signature = "separated"
autodoc_member_order = "bysource"       # alphabetical, groupwise, bysource
autodoc_typehints = "both"
#autoclass_content = "both"


# ==============================================================================
# Sphinx.Ext.ExtLinks
# ==============================================================================
extlinks = {
	"gh":        (f"https://GitHub.com/%s", "GitHub: %s"),
	"ghissue":   (f"https://GitHub.com/{githubNamespace}/{githubProject}/issues/%s", "issue #%s"),
	"ghpull":    (f"https://GitHub.com/{githubNamespace}/{githubProject}/pull/%s", "pull request #%s"),
	"ghsrc":     (f"https://GitHub.com/{githubNamespace}/{githubProject}/blob/main/%s", None),
	"wiki":      (f"https://en.wikipedia.org/wiki/%s", None),
	"pypi":      (f"https://pypi.org/project/%s/", "PyPI: %s"),
	"dockerhub": (f"https://hub.docker.com/r/%s", "Docker Hub: %s"),
}


# ==============================================================================
# Sphinx.Ext.Graphviz
# ==============================================================================
graphviz_output_format = "svg"


# ==============================================================================
# SphinxContrib.Mermaid
# ==============================================================================
mermaid_params = [
	'--backgroundColor', 'transparent',
]
mermaid_verbose = True


# ==============================================================================
# Sphinx.Ext.Inheritance_Diagram
# ==============================================================================
inheritance_node_attrs = {
#	"shape": "ellipse",
#	"fontsize": 14,
#	"height": 0.75,
	"color": "dodgerblue1",
	"style": "filled"
}


# ==============================================================================
# Sphinx.Ext.ToDo
# ==============================================================================
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
todo_link_only = True


# ==============================================================================
# sphinx-reports
# ==============================================================================
report_unittest_testsuites = {
	"src": {
		"name":        f"{pythonProject}",
		"xml_report":  "../report/unit/unittest.xml",
	}
}
report_codecov_packages = {
	"src": {
		"name":        f"{pythonProject}",
		"json_report": "../report/coverage/coverage.json",
		"fail_below":  80,
		"levels":      "default"
	}
}
report_doccov_packages = {
	"src": {
		"name":       f"{pythonProject}",
		"directory":  f"../{directoryName}",
		"fail_below": 80,
		"levels":     "default"
	}
}


# ==============================================================================
# Sphinx_Design
# ==============================================================================
# sd_fontawesome_latex = True


# ==============================================================================
# AutoAPI.Sphinx
# ==============================================================================
autoapi_modules = {
	f"{pythonProject}":  {
		"template": "package",
		"output":   pythonProject,
		"override": True
	}
}

for directory in [mod for mod in Path(f"../{directoryName}").iterdir() if mod.is_dir() and mod.name != "__pycache__"]:
	print(f"Adding module rule for '{pythonProject}.{directory.name}'")
	autoapi_modules[f"{pythonProject}.{directory.name}"] = {
		"template": "module",
		"output":   pythonProject,
		"override": True
	}
