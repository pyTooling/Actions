Repository Structure
####################

pyTooling Actions assumes a certain repository structure and usage of technologies. Besides assumed directory or file
names in default parameters to job templates, almost all can be overwritten if the target repository has a differing
structure.

* Python source code is located in a directory named after the Python package name.
* All tests are located in a ``/tests`` directory and separated by testing approach.
  * E.g. unit tests are located in a ``/tests/unit`` directory.
* The package documentation is located in a ``/doc`` directory.
  * Documentation is written with ReStructured Text (ReST) and translated using Sphinx.
  * Documentation requirements are listed in a ``/doc/requirements.txt``.
* Dependencies are listed in a ``/requirements.txt``.
  * If the build process requires separate dependencies, a ``/build/requirements.txt`` is used.
  * If the publishing/distribution process requires separate dependencies, a ``/dist/requirements.txt`` is used.
* All Python project settings are stored in a ``pyproject.toml``.
* The Python package is described in a ``setup.py``.
* A repository overview is given in a ``README.md``.

.. code-block::

   <Repository>/
     .github/
       workflows/
         Pipeline.yml
       dependabot.yml
     .vscode/
       settings.json
     build/
       requirements.txt
     dist/
       requirements.txt
     doc/
       conf.py
       index.rst
       requirements.txt
     <package>
       __init__.py
     tests/
       unit/
       requirements.txt
     .editorconfig
     .gitignore
     LICENSE.md
     pyproject.toml
     README.md
     requirements.txt
     setup.py

