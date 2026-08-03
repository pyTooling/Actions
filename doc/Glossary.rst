Glossary
########

.. glossary::

   Bandit
     Bandit is a tool designed to find common security issues in Python code.

     :Source Code:   `github.com/PyCQA/bandit/ <https://github.com/PyCQA/bandit/>`__
     :Package:       `pypi.org/project/bandit/ <https://pypi.org/project/bandit/>`__
     :Documentation: `bandit.readthedocs.io/ <https://bandit.readthedocs.io/>`__

   build
     A simple, correct Python build frontend.

     :Source Code:   `github.com/pypa/build/ <https://github.com/pypa/build/>`__
     :Package:       `pypi.org/project/build/ <https://pypi.org/project/build/>`__
     :Documentation: `build.pypa.io/ <https://build.pypa.io/>`__

   Codacy
     .. todo:: Add description of Codacy.

     :Cloud Service: `Codacy.com <https://www.codacy.com/>`__

   CodeCov
     .. todo:: Add description of CodeCov.

     :Cloud Service: `Codecov.io <https://about.codecov.io/>`__

   Coverage.py
     The code coverage tool for Python.

     :Source Code:   `github.com/nedbat/coveragepy/ <https://github.com/nedbat/coveragepy/>`__
     :Package:       `pypi.org/project/coverage/ <https://pypi.org/project/coverage/>`__
     :Documentation: `coverage.readthedocs.io/ <https://coverage.readthedocs.io/>`__

   delete-artifact
     A GitHub Action to deletes artifacts within the workflow run.

     :Source Code:   `github.com/GeekyEggo/delete-artifact/ <https://github.com/GeekyEggo/delete-artifact/>`__
     :Marketplace:   `github.com/marketplace/actions/delete-artifact/ <https://github.com/marketplace/actions/delete-artifact/>`__
     :README:        `github.com/GeekyEggo/delete-artifact → README.md <https://github.com/GeekyEggo/delete-artifact/blob/main/README.md>`__

   download-artifact
     GitHub Action downloading artifacts within a workflow run. :gh:`pyTooling/download-artifact` wraps
     :gh:`actions/download-artifact` and unpacks the tarball created by :term:`upload-artifact`, so file modes and
     symbolic links are restored.

     :Source Code:   `github.com/pyTooling/download-artifact/ <https://github.com/pyTooling/download-artifact/>`__
     :Marketplace:   `github.com/marketplace/actions/pytooling-download-artifact/ <https://github.com/marketplace/actions/pytooling-download-artifact/>`__

   docstr_coverage
     Docstring coverage analysis and rating for Python.

     :Source Code:   `github.com/HunterMcGushion/docstr_coverage/ <https://github.com/HunterMcGushion/docstr_coverage/>`__
     :Package:       `pypi.org/project/docstr_coverage/ <https://pypi.org/project/docstr_coverage/>`__
     :Documentation: `docstr-coverage.readthedocs.io/ <https://docstr-coverage.readthedocs.io/>`__

   gh
     GitHub’s official command line tool.

     :Source Code:   `github.com/cli/cli/ <https://github.com/cli/cli/>`__
     :Documentation: `cli.github.com/manual/ <https://cli.github.com/manual/>`__

   GitHub Pages
     GitHub Pages is a static site hosting service that takes HTML, CSS, and JavaScript files straight from a repository
     on GitHub, optionally runs the files through a build process, and publishes a website.

     :Documentation: https://docs.github.com/en/pages

   interrogate
     Explain yourself! Interrogate a codebase for docstring coverage.

     :Source Code:   `github.com/econchick/interrogate/ <https://github.com/econchick/interrogate/>`__
     :Package:       `pypi.org/project/interrogate/ <https://pypi.org/project/interrogate/>`__
     :Documentation: `interrogate.readthedocs.io/ <https://interrogate.readthedocs.io/>`__

   MikTeX
     MiKTeX is a modern TeX distribution for Windows, Linux and macOS.

     :Source Code:   `github.com/MiKTeX/miktex/ <https://github.com/MiKTeX/miktex/>`__
     :Documentation: `miktex.org/ <https://miktex.org/>`__

   pyTooling/MiKTeX
     Docker images shipping a :term:`MikTeX` installation with ``latexmk`` and a set of preinstalled LaTeX packages,
     so a LaTeX document can be translated to PDF without downloading packages at build time. The ``sphinx`` tag adds
     the packages :term:`Sphinx` emits into its LaTeX output.

     :Source Code:   `github.com/pyTooling/MiKTeX/ <https://github.com/pyTooling/MiKTeX/>`__
     :Docker Image:  :dockerhub:`pytooling/miktex <pytooling/miktex>`

   mypy
     Optional static typing for Python.

     :Source Code:   `github.com/python/mypy/ <https://github.com/python/mypy/>`__
     :Package:       `pypi.org/project/mypy/ <https://pypi.org/project/mypy/>`__
     :Documentation: `www.mypy-lang.org/ <https://www.mypy-lang.org/>`__

   pyEDAA.Reports
     A collection of various (EDA tool-specific) report data formats.

     :Source Code:   `github.com/edaa-org/pyEDAA.Reports/ <https://github.com/edaa-org/pyEDAA.Reports/>`__
     :Package:       `pypi.org/project/pyEDAA.Reports/ <https://pypi.org/project/pyEDAA.Reports/>`__
     :Documentation: `edaa-org.github.io/pyEDAA.Reports/ <https://edaa-org.github.io/pyEDAA.Reports/>`__

   pip
     The Python package installer.

     :Source Code:   `github.com/pypa/pip/ <https://github.com/pypa/pip/>`__
     :Package:       `pypi.org/project/pip/ <https://pypi.org/project/pip/>`__
     :Documentation: `pip.pypa.io/ <https://pip.pypa.io/>`__

   pylint
     Static code analyzer for Python. It checks a code base without running it and reports errors, violations of
     coding conventions, code smells and refactoring suggestions. Each finding has a category and an identifier
     (e.g. ``C0116``), so individual checks can be enabled, disabled or configured per project.

     :Source Code:   `github.com/pylint-dev/pylint/ <https://github.com/pylint-dev/pylint/>`__
     :Package:       `pypi.org/project/pylint/ <https://pypi.org/project/pylint/>`__
     :Documentation: `pylint.readthedocs.io/ <https://pylint.readthedocs.io/>`__

   PyPI
     Find, install and publish Python packages with the Python Package Index.

     :Cloud Service: `PyPI.org <https://pypi.org/>`__

   pytest
     The pytest framework makes it easy to write small tests, yet scales to support complex functional testing.

     :Source Code:   `github.com/pytest-dev/pytest/ <https://github.com/pytest-dev/pytest/>`__
     :Package:       `pypi.org/project/pytest/ <https://pypi.org/project/pytest/>`__
     :Documentation: `pytest.org/ <https://pytest.org/>`__

   radon
     Computes code metrics for Python code:

     * **Raw metrics** - lines of code, logical lines, comment lines, blank lines.
     * **Cyclomatic complexity** - the number of linearly independent paths through a function, graded from *A* to
       *F*.
     * **Halstead metrics** - vocabulary, length, volume, difficulty, effort and the estimated number of bugs,
       derived from the operators and operands in the code.
     * **Maintainability index** - a single score combining cyclomatic complexity, lines of code and comment ratio.

     :Source Code:   `github.com/rubik/radon/ <https://github.com/rubik/radon/>`__
     :Package:       `pypi.org/project/radon/ <https://pypi.org/project/radon/>`__
     :Documentation: `radon.readthedocs.io/ <https://radon.readthedocs.io/>`__

   Sphinx
     The Sphinx documentation generator.

     :Source Code:   `github.com/sphinx-doc/sphinx/ <https://github.com/sphinx-doc/sphinx/>`__
     :Package:       `pypi.org/project/sphinx/ <https://pypi.org/project/sphinx/>`__
     :Documentation: `www.sphinx-doc.org/ <https://www.sphinx-doc.org/>`__

   Test Reporter
     Displays test results from popular testing frameworks directly in GitHub.

     :Source Code:   `github.com/dorny/test-reporter/ <https://github.com/dorny/test-reporter/>`__
     :Marketplace:   `github.com/marketplace/actions/test-reporter/ <https://github.com/marketplace/actions/test-reporter/>`__
     :README:        `github.com/dorny/test-reporter → README.md <https://github.com/dorny/test-reporter/blob/main/README.md>`__

   upload-artifact
     GitHub Action uploading artifacts within a workflow run. :gh:`pyTooling/upload-artifact` wraps
     :gh:`actions/upload-artifact` and packs the uploaded files into a tarball first, because the original action
     does not preserve file modes and symbolic links.

     :Source Code:   `github.com/pyTooling/upload-artifact/ <https://github.com/pyTooling/upload-artifact/>`__
     :Marketplace:   `github.com/marketplace/actions/pytooling-upload-artifact/ <https://github.com/marketplace/actions/pytooling-upload-artifact/>`__

   twine
     Utilities for interacting with PyPI.

     :Source Code:   `github.com/pypa/twine/ <https://github.com/pypa/twine/>`__
     :Package:       `pypi.org/project/twine/ <https://pypi.org/project/twine/>`__
     :Documentation: `twine.readthedocs.io/ <https://twine.readthedocs.io/>`__

   wheel
     Reference implementation of the Python wheel packaging standard. It is installed alongside :term:`pip` by most
     job templates, because a source distribution that has to be built during installation needs it.

     :Source Code:   `github.com/pypa/wheel/ <https://github.com/pypa/wheel/>`__
     :Package:       `pypi.org/project/wheel/ <https://pypi.org/project/wheel/>`__
     :Documentation: `wheel.readthedocs.io/ <https://wheel.readthedocs.io/>`__
