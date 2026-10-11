Repository Structure
####################

pyTooling Actions assumes a certain repository structure and usage of technologies. Besides assumed directory or file
names in default parameters to job templates, almost all can be overwritten if the target repository has a differing
structure.

* Python source code is located in a directory named after the Python package name.

  * A ``<package>/__init__.py`` should be provided with global package information like: version number, author,
    copyrights, license, maintainer, ...

* All tests are located in a ``/tests`` directory and further divided into subdirectories by testing approach.

  * E.g. unit tests are located in a ``/tests/unit`` directory.

* The package documentation is located in a ``/doc`` directory.

  * Documentation is written with ReStructured Text (ReST) and translated using Sphinx.
  * Documentation requirements are listed in a ``/doc/requirements.txt``.

* Dependencies are listed in a ``/requirements.txt``.

  * If the build process requires separate dependencies, a ``/build/requirements.txt`` is used.
  * If the publishing/distribution process requires separate dependencies, a ``/dist/requirements.txt`` is used.
  * To reduce duplication of dependencies, dependency files should recursively call each other with ``-r <path>``.

* All Python project settings are stored in a ``pyproject.toml``.
* The Python package is described in a ``setup.py``.
* Packages are build with ``build`` instead of ``setuptools``.
* A repository overview is given in a ``README.md``.

.. tree::
   :root-icon: 📂
   :node-icon: 📂
   :leaf-icon: 📄
   :icons:     > 📂, + 🐍

   - :file:`<Repository>/`
     - :file:`.github/`
       - :file:`workflows/`
         - :file:`Pipeline.yml`
       - :file:`dependabot.yml`
     - :file:`.vscode/`
       - :file:`settings.json`
     - :file:`build/`
       - :file:`requirements.txt`
     - :file:`dist/`
       - :file:`requirements.txt`
     - :file:`doc/`
       + :file:`conf.py`
       - :file:`index.rst`
       - :file:`requirements.txt`
     - :file:`<package>/`
       + :file:`__init__.py`
     - :file:`tests/`
       > :file:`unit/`
       - :file:`requirements.txt`
     - :file:`.editorconfig`
     - :file:`.gitignore`
     - :file:`LICENSE.md`
     - :file:`pyproject.toml`
     - :file:`README.md`
     - :file:`requirements.txt`
     + :file:`setup.py`
