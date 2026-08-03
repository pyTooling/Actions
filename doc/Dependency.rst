Dependencies
############

This is a summary of dependencies used by the provided job templates. For more details, see each job template.

* Actions provided by GitHub

  * :gh:`actions/checkout`
  * :gh:`actions/setup-python`
  * :gh:`actions/github-script`
  * :gh:`actions/upload-pages-artifact`
  * :gh:`actions/deploy-pages`

* Actions provided by pyTooling

  * :term:`upload-artifact` (:gh:`pyTooling/upload-artifact`)
  * :term:`download-artifact` (:gh:`pyTooling/download-artifact`)

* Code Quality Services

  * :gh:`codecov/codecov-action`
  * :gh:`codacy/codacy-coverage-reporter-action`

* Reporting

  * :gh:`dorny/test-reporter`

* Miscellaneous

  * :gh:`msys2/setup-msys2`
  * :gh:`geekyeggo/delete-artifact`
  * :term:`gh` - preinstalled on GitHub runners.
  * :term:`pyTooling/MiKTeX` (:dockerhub:`Docker image <pytooling/miktex>`)

* System packages installed through ``apt``

  * `graphviz <https://graphviz.org/>`__
  * `zstd <https://facebook.github.io/zstd/>`__

* System packages installed through the caller's parameters

  These are **not** installed by the job templates. The templates only pass the package lists on, so the caller
  decides which system packages a test needs:

  * ``apt`` - Debian/Ubuntu packages.
  * ``brew`` - Homebrew packages on macOS.
  * ``pacboy`` - MSYS2 packages, given in ``pacboy`` syntax.

* Python packages installed through :term:`pip`

  * :term:`bandit` (:pypi:`PyPI package <bandit>`)
  * :term:`build` (:pypi:`PyPI package <build>`)
  * :term:`Coverage.py` (:pypi:`PyPI package <coverage>`)
  * :term:`docstr_coverage` (:pypi:`PyPI package <docstr_coverage>`)
  * :term:`interrogate` (:pypi:`PyPI package <interrogate>`)
  * :term:`pyEDAA.Reports` (:pypi:`PyPI package <pyEDAA.Reports>`)
  * :term:`pylint` (:pypi:`PyPI package <pylint>`)
  * :term:`radon` (:pypi:`PyPI package <radon>`)
  * :term:`twine` (:pypi:`PyPI package <twine>`)
  * :term:`wheel` (:pypi:`PyPI package <wheel>`)

* Python packages installed through the caller's requirements file

  These are **not** installed by the job templates. The templates only run the tools, so the caller decides the
  version:

  * :term:`mypy` (:pypi:`PyPI package <mypy>`)
  * :term:`pytest` (:pypi:`PyPI package <pytest>`)
  * :term:`Coverage.py` (:pypi:`PyPI package <coverage>`)
  * :term:`Sphinx` (:pypi:`PyPI package <Sphinx>`), its theme and its extensions
