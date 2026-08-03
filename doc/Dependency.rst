Dependencies
############

This is a summary of dependencies used by the provided job templates. For more details, see each job template.

* Actions provided by GitHub

  * :gh:`actions/checkout`
  * :gh:`actions/setup-python`
  * :gh:`actions/github-script` - used by :ref:`JOBTMPL/TagReleaseCommit` to dispatch the tag pipeline.
  * :gh:`actions/upload-pages-artifact` - used by :ref:`JOBTMPL/PublishToGitHubPages`.
  * :gh:`actions/deploy-pages` - used by :ref:`JOBTMPL/PublishToGitHubPages`.

* Actions provided by pyTooling

  * :gh:`pyTooling/upload-artifact` - wraps :gh:`actions/upload-artifact` and packs the uploaded files into a
    tarball, so file modes and symbolic links survive the round trip.
  * :gh:`pyTooling/download-artifact` - wraps :gh:`actions/download-artifact` and unpacks that tarball again.

* Code Quality Services

  * :gh:`codecov/codecov-action`
  * :gh:`codacy/codacy-coverage-reporter-action`

* Reporting

  * :gh:`dorny/test-reporter`

* Miscellaneous

  * :gh:`msys2/setup-msys2`
  * :gh:`geekyeggo/delete-artifact`
  * :gh:`GitHub command line tool 'gh' <cli/cli>` - preinstalled on GitHub runners; used by
    :ref:`JOBTMPL/PrepareJob` and :ref:`JOBTMPL/PublishReleaseNotes`.
  * :dockerhub:`pytooling/miktex <pytooling/miktex:sphinx>` - the container :ref:`JOBTMPL/LaTeXDocumentation` runs in.

* System packages installed through ``apt``

  * `graphviz <https://graphviz.org/>`__ - used by :ref:`JOBTMPL/SphinxDocumentation` to render diagrams.
  * `zstd <https://facebook.github.io/zstd/>`__ - used by :ref:`JOBTMPL/PublishReleaseNotes` to compress release
    assets.
  * Further packages specified by the caller via the ``apt``, ``brew`` and ``pacboy`` parameters of
    :ref:`JOBTMPL/UnitTesting` and :ref:`JOBTMPL/ApplicationTesting`.

* Python packages installed through :term:`pip`

  * :term:`bandit` (:pypi:`PyPI package <bandit>`) - :ref:`JOBTMPL/CheckCodeQuality`
  * :term:`build` (:pypi:`PyPI package <build>`) - :ref:`JOBTMPL/Package`
  * :term:`Coverage.py` (:pypi:`PyPI package <coverage>`) - :ref:`JOBTMPL/PublishCoverageResults`
  * :term:`docstr_coverage` (:pypi:`PyPI package <docstr_coverage>`) - :ref:`JOBTMPL/CheckDocumentation`
  * :term:`interrogate` (:pypi:`PyPI package <interrogate>`) - :ref:`JOBTMPL/CheckDocumentation`
  * :term:`pyEDAA.Reports` (:pypi:`PyPI package <pyEDAA.Reports>`) - :ref:`JOBTMPL/PublishTestResults`
  * :term:`pylint` (:pypi:`PyPI package <pylint>`) - :ref:`JOBTMPL/CheckCodeQuality`
  * :term:`radon` (:pypi:`PyPI package <radon>`) - :ref:`JOBTMPL/CheckCodeQuality`
  * :term:`twine` (:pypi:`PyPI package <twine>`) - :ref:`JOBTMPL/PublishOnPyPI`
  * :pypi:`wheel` - installed by most job templates before the caller's requirements.

* Python packages installed through the caller's requirements file

  These are *not* installed by the job templates. The templates only run the tools, so the caller decides the version:

  * :term:`mypy` (:pypi:`PyPI package <mypy>`) - :ref:`JOBTMPL/StaticTypeCheck`
  * :term:`pytest` (:pypi:`PyPI package <pytest>`) and :term:`Coverage.py` (:pypi:`PyPI package <coverage>`) -
    :ref:`JOBTMPL/UnitTesting`, :ref:`JOBTMPL/ApplicationTesting`
  * :term:`Sphinx` (:pypi:`PyPI package <Sphinx>`), its theme and extensions - :ref:`JOBTMPL/SphinxDocumentation`
