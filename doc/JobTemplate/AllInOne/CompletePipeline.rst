.. _JOBTMPL/CompletePipeline:

CompletePipeline
################

The ``CompletePipeline`` job template is the combination of almost all job templates offered by pyTooling/Actions in a
single workflow template. If fulfills all needs to test, package, document, publish and release Python code from GitHub.
It can be used for simple Python packages as well as namespace packages.

.. topic:: Features

   .. grid:: 3

      .. grid-item::
         :columns: 4

         .. rubric:: Testing

         * Run unit tests.
         * Run platform tests.
         * Run application tests on target platform.

         .. rubric:: Code Quality

         * Collect code coverage.
         * Check documentation coverage.
         * Check static typing closure.

         .. rubric:: Report Handling

         * Merge unit test results into a single summary report.
         * Merge code coverage results into a single summary report.

      .. grid-item::
         :columns: 4

         .. rubric:: Documentation

         * Compile documentation using Sphinx as HTML and LaTeX.
         * Translate LaTeX documentation to PDF.

         .. rubric:: Publishing Results

         * GitHub Pipeline Summary

           * Publich unittest results using :gh:`dorny/test-reporter`.

         * GitHub Pages

           * Publish HTML documentation to GitHub Pages.

         * Codacy

           * Publish code coverage to Codacy.

         * CodeCov

           * Publish code coverage to CodeCov.
           * Publish unittest results to CodeCov.

      .. grid-item::
         :columns: 4

         .. rubric:: Packaging

         * Package as wheel.
         * Install wheel on target platform.
         * Upload to PyPI.

         .. rubric:: Releasing

         * Automatic tagging of merge commits on main branch to trigger a tagged pipeline (release pipeline).
         * Create a release page with text derived from pull request description.

.. topic:: Behavior

   1. Infer information from ``${{ github.ref }}`` variable.
   2. Extract Python project settings from :file:`pyproject.toml`.
   3. Compute job matrix based on system, Python version, environment, ... for job variants.
   4. Run unit tests using pytest and collect code coverage.
   5. Run platform tests using pytest and collect code coverage.
   6. Run application tests using pytest.
   7. Package code as wheel.
   8. Check documentation coverage using docstr_coverage and interrogate.
   9. Verify type annotation using static typing analysis using mypy.
   10. Merge unit test results and code coverage results.
   11. Generate HTML and LaTeX documentations using Sphinx.
   12. Translate LaTeX documentation to PDF using MikTeX.
   13. Publish unit test and code coverage results to cloud services.
   14. Publish documentation to GitHub Pages.
   15. Publish wheel to PyPI.
   16. Create a GitHub release page and upload release assets.


.. topic:: Pipeline Graph

   .. image:: ../../_static/pyTooling-Actions-SimplePackage.png

.. topic:: Dependencies

   .. dropdown:: Expand List
      :animate: fade-in-slide-down
      :icon: codescan
      :color: muted

      .. grid:: 2

         .. grid-item::
            :columns: 6

            * :ref:`pyTooling/Actions/.github/workflows/PrepareJob.yml <JOBTMPL/PrepareJob>`

              * :gh:`actions/checkout`
              * :gh:`GitHub command line tool 'gh' <cli/cli>`

            * :ref:`pyTooling/Actions/.github/workflows/Parameters.yml <JOBTMPL/Parameters>`
            * :ref:`pyTooling/Actions/.github/workflows/ExtractConfiguration.yml <JOBTMPL/ExtractConfiguration>`

              * :gh:`actions/checkout`
              * :gh:`actions/setup-python`

                * :pypi:`wheel`
                * :pypi:`tomli`

            * :ref:`pyTooling/Actions/.github/workflows/UnitTesting.yml <JOBTMPL/UnitTesting>`

              * :gh:`actions/checkout`
              * :gh:`msys2/setup-msys2`
              * :gh:`actions/setup-python`
              * :gh:`pyTooling/download-artifact`

                * :gh:`actions/download-artifact`

              * :gh:`pyTooling/upload-artifact`

                * :gh:`actions/upload-artifact`

              * apt: Packages specified via :ref:`JOBTMPL/UnitTesting/Input/apt` parameter.
              * homebrew: Packages specified via :ref:`JOBTMPL/UnitTesting/Input/brew` parameter.
              * MSYS2: Packages specified via :ref:`JOBTMPL/UnitTesting/Input/pacboy` parameter.
              * pip

                * :pypi:`wheel`
                * :pypi:`tomli`
                * Python packages specified via :ref:`JOBTMPL/UnitTesting/Input/requirements` or
                  :ref:`JOBTMPL/UnitTesting/Input/mingw_requirements` parameter.

            * :ref:`pyTooling/Actions/.github/workflows/ApplicationTesting.yml <JOBTMPL/ApplicationTesting>`
            * :ref:`pyTooling/Actions/.github/workflows/CheckDocumentation.yml <JOBTMPL/CheckDocumentation>`

              * :gh:`actions/checkout`
              * :gh:`actions/setup-python`
              * pip

                * :pypi:`docstr_coverage`
                * :pypi:`interrogate`

            * :ref:`pyTooling/Actions/.github/workflows/StaticTypeCheck.yml <JOBTMPL/StaticTypeCheck>`
            * :ref:`pyTooling/Actions/.github/workflows/Package.yml <JOBTMPL/Package>`

              * :gh:`actions/checkout`
              * :gh:`actions/setup-python`
              * :gh:`pyTooling/upload-artifact`

                * :gh:`actions/upload-artifact`

              * pip

                * :pypi:`build`
                * :pypi:`wheel`

            * :ref:`pyTooling/Actions/.github/workflows/PublishTestResults.yml <JOBTMPL/PublishTestResults>`

              * :gh:`actions/checkout`
              * :gh:`pyTooling/download-artifact`

                * :gh:`actions/download-artifact`

              * pip

                * :pypi:`pyEDAA.Reports`

              * :gh:`dorny/test-reporter`
              * :gh:`codecov/test-results-action`
              * :gh:`pyTooling/upload-artifact`

                * :gh:`actions/upload-artifact`

         .. grid-item::
            :columns: 6

            * :ref:`pyTooling/Actions/.github/workflows/PublishCoverageResults.yml <JOBTMPL/PublishCoverageResults>`

              * :gh:`actions/checkout`
              * :gh:`pyTooling/download-artifact`

                * :gh:`actions/download-artifact`

              * pip

                * :pypi:`coverage`
                * :pypi:`tomli`

              * :gh:`pyTooling/upload-artifact`

                * :gh:`actions/upload-artifact`

              * :gh:`codecov/codecov-action`
              * :gh:`codacy/codacy-coverage-reporter-action`

            * :ref:`pyTooling/Actions/.github/workflows/SphinxDocumentation.yml <JOBTMPL/SphinxDocumentation>`

              * :gh:`actions/checkout`
              * :gh:`actions/setup-python`
              * :gh:`pyTooling/download-artifact`

                * :gh:`actions/download-artifact`

              * :gh:`pyTooling/upload-artifact`

                * :gh:`actions/upload-artifact`

              * apt

                * `graphviz <https://graphviz.org/>`__

              * pip

                * :pypi:`wheel`
                * Python packages specified via :ref:`JOBTMPL/SphinxDocumentation/Input/requirements` parameter.

            * :ref:`pyTooling/Actions/.github/workflows/LaTeXDocumentation.yml <JOBTMPL/LaTeXDocumentation>`

              * :gh:`pyTooling/download-artifact`

                * :gh:`actions/download-artifact`

              * :gh:`pyTooling/upload-artifact`

                * :gh:`actions/upload-artifact`

              * :gh:`addnab/docker-run-action`

                * :dockerhub:`pytooling/miktex <pytooling/miktex:sphinx>`

            * :ref:`pyTooling/Actions/.github/workflows/PublishToGitHubPages.yml <JOBTMPL/PublishToGitHubPages>`
            * :ref:`pyTooling/Actions/.github/workflows/PublishOnPyPI.yml <JOBTMPL/PublishOnPyPI>`

              * :gh:`pyTooling/download-artifact`

                * :gh:`actions/download-artifact`
              * :gh:`actions/setup-python`
              * :gh:`geekyeggo/delete-artifact`

              * pip

                * :pypi:`wheel`
                * :pypi:`twine`

            * :ref:`pyTooling/Actions/.github/workflows/TagReleaseCommit.yml <JOBTMPL/TagReleaseCommit>`

              * :gh:`actions/github-script`

            * :ref:`pyTooling/Actions/.github/workflows/PublishReleaseNotes.yml <JOBTMPL/PublishReleaseNotes>`

              * :gh:`actions/checkout`
              * ``gh`` (GitHub command line interface)
              * ``jq`` (JSON processing)
              * apt

                * zstd

            * :ref:`pyTooling/Actions/.github/workflows/IntermediateCleanUp.yml <JOBTMPL/IntermediateCleanUp>`

              * :gh:`geekyeggo/delete-artifact`

            * :ref:`pyTooling/Actions/.github/workflows/ArtifactCleanUp.yml <JOBTMPL/ArtifactCleanUp>`

              * :gh:`geekyeggo/delete-artifact`


.. _JOBTMPL/CompletePipeline/Instantiation:

Instantiation
*************

The following instantiation example creates a ``SimplePackage`` job derived from job template ``CompletePipeline``
version ``@r5``. It only requires the `package_name` parameter to run a full pipeline suitable for a Python project.

   .. grid:: 2

      .. grid-item::
         :columns: 6

         .. tab-set::

            .. tab-item:: Simple Package
               :sync: Simple

               .. code-block:: yaml

                  name: Pipeline

                  jobs:
                    SimplePackage:
                      uses: pyTooling/Actions/.github/workflows/CompletePipeline.yml@r5
                      with:

                        package_name: myPackage

            .. tab-item:: Namespace Package
               :sync: Namespace

               .. code-block:: yaml

                  name: Pipeline

                  jobs:
                    NamespacePackage:
                      uses: pyTooling/Actions/.github/workflows/CompletePipeline.yml@r5
                      with:
                        package_namespace: myFramework
                        package_name:      Extension

      .. grid-item::
         :columns: 6

         .. tab-set::

            .. tab-item:: Simple Package
               :sync: Simple

               .. code-block::

                  📂ProjectRoot/
                    📂myFramework/

                      📦SubPackage/
                        🐍__init__.py
                        🐍SubModuleA.py
                      🐍__init__.py
                      🐍ModuleB.py


            .. tab-item:: Namespace Package
               :sync: Namespace

               .. code-block::

                  📂ProjectRoot/
                    📂myFramework/
                      📂Extension/
                        📦SubPackage/
                          🐍__init__.py
                          🐍SubModuleA.py
                        🐍__init__.py
                        🐍ModuleB.py


.. _JOBTMPL/CompletePipeline/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/CompletePipeline/Inputs>`

+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| Parameter Name                                                      | Required | Type     | Default                                           |
+=====================================================================+==========+==========+===================================================+
| :ref:`JOBTMPL/CompletePipeline/Input/package_namespace`             | no       | string   | ``''``                                            |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/package_name`                  | yes      | string   | — — — —                                           |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/unittest_python_version`       | no       | string   | ``'3.13'``                                        |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/unittest_python_version_list`  | no       | string   | ``'3.9 3.10 3.11 3.12 3.13'``                     |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/unittest_system_list`          | no       | string   | ``'ubuntu windows macos macos-arm ucrt64'``       |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/unittest_include_list`         | no       | string   | ``''``                                            |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/unittest_exclude_list`         | no       | string   | ``'windows-arm:3.9 windows-arm:3.10'``            |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/unittest_disable_list`         | no       | string   | ``'windows-arm:pypy-3.10 windows-arm:pypy-3.11'`` |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/apptest_python_version`        | no       | string   | ``'3.13'``                                        |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/apptest_python_version_list`   | no       | string   | ``''``                                            |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/apptest_system_list`           | no       | string   | ``'ubuntu windows macos macos-arm ucrt64'``       |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/apptest_include_list`          | no       | string   | ``''``                                            |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/apptest_exclude_list`          | no       | string   | ``'windows-arm:3.9 windows-arm:3.10'``            |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/apptest_disable_list`          | no       | string   | ``'windows-arm:pypy-3.10 windows-arm:pypy-3.11'`` |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/codecov`                       | no       | string   | ``'false'``                                       |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/codacy`                        | no       | string   | ``'false'``                                       |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/dorny`                         | no       | string   | ``'false'``                                       |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/CompletePipeline/Input/cleanup`                       | no       | string   | ``'true'``                                        |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/CompletePipeline/Secrets>`

+-----------------------------------------------------------+----------+----------+--------------+
| Token Name                                                | Required | Type     | Default      |
+===========================================================+==========+==========+==============+
| :ref:`JOBTMPL/CompletePipeline/Secret/PYPI_TOKEN`         | no       | string   | — — — —      |
+-----------------------------------------------------------+----------+----------+--------------+
| :ref:`JOBTMPL/CompletePipeline/Secret/CODECOV_TOKEN`      | no       | string   | — — — —      |
+-----------------------------------------------------------+----------+----------+--------------+
| :ref:`JOBTMPL/CompletePipeline/Secret/CODACY_TOKEN`       | no       | string   | — — — —      |
+-----------------------------------------------------------+----------+----------+--------------+

.. rubric:: Goto :ref:`output parameters <JOBTMPL/CompletePipeline/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/CompletePipeline/Inputs:

Input Parameters
****************

.. _JOBTMPL/CompletePipeline/Input/package_namespace:

package_namespace
=================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid Python namespace.
:Description:     In case the package is a Python namespace package, the name of the library's or package's namespace
                  needs to be specified using this parameter. |br|
                  In case of a simple Python package, this parameter must be specified as an empty string (``''``),
                  which is the default.
:Example:
                  .. grid:: 2

                     .. grid-item::
                        :columns: 5

                        .. rubric:: Example Instantiation

                        .. code-block:: yaml

                           name: Pipeline

                           jobs:
                             NamespacePackage:
                               uses: pyTooling/Actions/.github/workflows/CompletePipeline.yml@r5
                               with:
                                 package_namespace: myFramework
                                 package_name:      Extension

                     .. grid-item::
                        :columns: 4

                        .. rubric:: Example Directory Structure

                        .. code-block::

                           📂ProjectRoot/
                             📂myFramework/
                               📂Extension/
                                 📦SubPackage/
                                   🐍__init__.py
                                   🐍SubModuleA.py
                                 🐍__init__.py
                                 🐍ModuleB.py


.. _JOBTMPL/CompletePipeline/Input/package_name:

package_name
============

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: Any valid Python package name.
:Description:     In case of a simple Python package, this package's name is specified using this parameter. |br|
                  In case the package is a Python namespace package, the parameter
                  :ref:`JOBTMPL/CompletePipeline/Input/package_namespace` must be specified, too.
:Example:
                  .. grid:: 2

                     .. grid-item::
                        :columns: 5

                        .. rubric:: Example Instantiation

                        .. code-block:: yaml

                           name: Pipeline

                           jobs:
                             SimplePackage:
                               uses: pyTooling/Actions/.github/workflows/CompletePipeline.yml@r5
                               with:
                                 package_name: myPackage

                     .. grid-item::
                        :columns: 4

                        .. rubric:: Example Directory Structure

                        .. code-block::

                           📂ProjectRoot/
                             📂myFramework/
                               📦SubPackage/
                                 🐍__init__.py
                                 🐍SubModuleA.py
                               🐍__init__.py
                               🐍ModuleB.py


.. _JOBTMPL/CompletePipeline/Input/unittest_python_version:

unittest_python_version
=======================

:Type:            string
:Required:        no
:Default Value:   ``'3.13'``
:Possible Values: Any valid Python version conforming to the pattern ``<major>.<minor>`` or ``pypy-<major>.<minor>``. |br|
                  See `actions/python-versions - available Python versions <https://github.com/actions/python-versions>`__
                  and `actions/setup-python - configurable Python versions <https://github.com/actions/setup-python>`__.
:Description:     The default Python version used for intermediate jobs using Python tools.

                  In case :ref:`JOBTMPL/CompletePipeline/Input/unittest_python_version_list` is empty, this default
                  version is used to populate the :ref:`JOBTMPL/CompletePipeline/Input/unittest_python_version_list`
                  parameter.


.. _JOBTMPL/CompletePipeline/Input/unittest_python_version_list:

unittest_python_version_list
============================

:Type:            string
:Required:        no
:Default Value:   ``'3.9 3.10 3.11 3.12 3.13'``
:Possible Values: A space separated list of valid Python versions conforming to the pattern ``<major>.<minor>`` or
                  ``pypy-<major>.<minor>``.
:Description:     The list of space-separated Python versions used for unit testing.

                  .. include:: ../PythonVersionList.rst


.. _JOBTMPL/CompletePipeline/Input/unittest_system_list:

unittest_system_list
====================

:Type:            string
:Required:        no
:Default Value:   ``'ubuntu windows macos macos-arm mingw64 ucrt64'``
:Possible Values: A space separated list of system names.
:Description:     The list of space-separated systems used for unit testing.

                  .. include:: ../SystemList.rst


.. _JOBTMPL/CompletePipeline/Input/unittest_include_list:

unittest_include_list
=====================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: A space separated list of ``<system>:<python_version>`` tuples.
:Description:     List of space-separated ``<system>:<python_version>`` tuples to be included into the list of unittest
                  variants.

                  For more details see :ref:`JOBTMPL/Parameters/Input/include_list`.


.. _JOBTMPL/CompletePipeline/Input/unittest_exclude_list:

unittest_exclude_list
=====================

:Type:            string
:Required:        no
:Default Value:   ``'windows-arm:3.9 windows-arm:3.10'``
:Possible Values: A space separated list of ``<system>:<python_version>`` tuples.
:Description:     List of space-separated ``<system>:<python_version>`` tuples to be excluded from the list of unittest
                  variants.

                  For more details see :ref:`JOBTMPL/Parameters/Input/exclude_list`.


.. _JOBTMPL/CompletePipeline/Input/unittest_disable_list:

unittest_disable_list
=====================

:Type:            string
:Required:        no
:Default Value:   ``'windows-arm:pypy-3.10 windows-arm:pypy-3.11'``
:Possible Values: A space separated list of ``<system>:<python_version>`` tuples.
:Description:     List of space-separated ``<system>:<python_version>`` tuples to be temporarily disabled from the list
                  of unittest variants. |br|
                  Each disabled item creates a warning in the workflow log.

                  For more details see :ref:`JOBTMPL/Parameters/Input/disable_list`.


.. _JOBTMPL/CompletePipeline/Input/apptest_python_version:

apptest_python_version
======================

:Type:            string
:Required:        no
:Default Value:   ``'3.13'``
:Possible Values: Any valid Python version conforming to the pattern ``<major>.<minor>`` or ``pypy-<major>.<minor>``. |br|
                  See `actions/python-versions - available Python versions <https://github.com/actions/python-versions>`__
                  and `actions/setup-python - configurable Python versions <https://github.com/actions/setup-python>`__.
:Description:     The default Python version used for intermediate jobs using Python tools.

                  In case :ref:`JOBTMPL/CompletePipeline/Input/apptest_python_version_list` is empty, this default
                  version is used to populate the :ref:`JOBTMPL/CompletePipeline/Input/apptest_python_version_list`
                  parameter.


.. _JOBTMPL/CompletePipeline/Input/apptest_python_version_list:

apptest_python_version_list
===========================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: A space separated list of valid Python versions conforming to the pattern ``<major>.<minor>`` or
                  ``pypy-<major>.<minor>```.
:Description:     The list of space-separated Python versions used for application testing.

                  As this list is empty by default, the value is derived from
                  :ref:`JOBTMPL/CompletePipeline/Input/apptest_python_version`.

                  .. include:: ../PythonVersionList.rst


.. _JOBTMPL/CompletePipeline/Input/apptest_system_list:

apptest_system_list
===================

:Type:            string
:Required:        no
:Default Value:   ``'ubuntu windows macos macos-arm mingw64 ucrt64'``
:Possible Values: A space separated list of system names.
:Description:     The list of space-separated systems used for application testing.

                  .. include:: ../SystemList.rst


.. _JOBTMPL/CompletePipeline/Input/apptest_include_list:

apptest_include_list
====================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: A space separated list of ``<system>:<python_version>`` tuples.
:Description:     List of space-separated ``<system>:<python_version>`` tuples to be included into the list of
                  application test variants.

                  For more details see :ref:`JOBTMPL/Parameters/Input/include_list`.


.. _JOBTMPL/CompletePipeline/Input/apptest_exclude_list:

apptest_exclude_list
====================

:Type:            string
:Required:        no
:Default Value:   ``'windows-arm:3.9 windows-arm:3.10'``
:Possible Values: A space separated list of ``<system>:<python_version>`` tuples.
:Description:     List of space-separated ``<system>:<python_version>`` tuples to be excluded from the list of
                  appliation test variants.

                  For more details see :ref:`JOBTMPL/Parameters/Input/exclude_list`.


.. _JOBTMPL/CompletePipeline/Input/apptest_disable_list:

apptest_disable_list
====================

:Type:            string
:Required:        no
:Default Value:   ``'windows-arm:pypy-3.10 windows-arm:pypy-3.11'``
:Possible Values: A space separated list of ``<system>:<python_version>`` tuples.
:Description:     List of space-separated ``<system>:<python_version>`` tuples to be temporarily disabled from the list
                  of application test variants. |br|
                  Each disabled item creates a warning in the workflow log.

                  For more details see :ref:`JOBTMPL/Parameters/Input/disable_list`.


.. _JOBTMPL/CompletePipeline/Input/codecov:

codecov
=======

:Type:            string
:Required:        no
:Default Value:   ``'false'``
:Possible Values: ``'true'``, ``'false'``
:Description:     If *true*, publish merged code coverage results and a merged unit test summary to CodeCov. |br|
                  Secret :ref:`JOBTMPL/CompletePipeline/Secret/CODECOV_TOKEN` must be set.


.. _JOBTMPL/CompletePipeline/Input/codacy:

codacy
======

:Type:            string
:Required:        no
:Default Value:   ``'false'``
:Possible Values: ``'true'``, ``'false'``
:Description:     If *true*, publish merged code coverage results to Codacy. |br|
                  Secret :ref:`JOBTMPL/CompletePipeline/Secret/CODACY_TOKEN` must be set.


.. _JOBTMPL/CompletePipeline/Input/dorny:

dorny
=====

:Type:            string
:Required:        no
:Default Value:   ``'false'``
:Possible Values: ``'true'``, ``'false'``
:Description:     If *true*, publish a merged unit test summary as pipeline result.


.. _JOBTMPL/CompletePipeline/Input/cleanup:

cleanup
=======

:Type:            string
:Required:        no
:Default Value:   ``'true'``
:Possible Values: ``'true'``, ``'false'``
:Description:     If *false*, do not remove intermediate artifacts. |br|
                  This might help debugging artifact handovers between jobs.


.. _JOBTMPL/CompletePipeline/Secrets:

Secrets
*******

The workflow template uses the following secrets to publish results to other services.


.. _JOBTMPL/CompletePipeline/Secret/PYPI_TOKEN:

PYPI_TOKEN
==========

:Type:            string
:Required:        no
:Default Value:   — — — —
:Description:     The token to publish and upload packages on `PyPI <https://pypi.org/>`__.


.. _JOBTMPL/CompletePipeline/Secret/CODECOV_TOKEN:

CODECOV_TOKEN
=============

:Type:            string
:Required:        no
:Default Value:   — — — —
:Description:     The token to publish code coverage and unit test results to `CodeCov <https://about.codecov.io//>`__.


.. _JOBTMPL/CompletePipeline/Secret/CODACY_TOKEN:

CODACY_TOKEN
============

:Type:            string
:Required:        no
:Default Value:   — — — —
:Description:     The token to publish code coverage results to `Codacy <https://www.codacy.com/>`__.


.. _JOBTMPL/CompletePipeline/Outputs:

Outputs
*******

This job template has no output parameters.


.. _JOBTMPL/CompletePipeline/Optimizations:

Optimizations
*************

The following optimizations can be used to reduce the template's runtime.

.. todo::

   CompletePipeline::Optimizations Needs a list of optimizations.
