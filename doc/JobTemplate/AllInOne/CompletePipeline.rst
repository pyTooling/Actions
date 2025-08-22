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

.. topic:: Behavior:

   .. todo:: CompletePipeline:Behavior needs documentation.

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


.. topic:: Pipeline Graph

   .. image:: ../../_static/pyTooling-Actions-SimplePackage.png

.. topic:: Dependencies

   * :ref:`pyTooling/Actions/.github/workflows/PrepareJob.yml <JOBTMPL/PrepareJob>`

     * :gh:`actions/checkout`

   * :ref:`pyTooling/Actions/.github/workflows/Parameters.yml <JOBTMPL/Parameters>`
   * :ref:`pyTooling/Actions/.github/workflows/ExtractConfiguration.yml <JOBTMPL/ExtractConfiguration>`
   * :ref:`pyTooling/Actions/.github/workflows/UnitTesting.yml <JOBTMPL/UnitTesting>`
   * :ref:`pyTooling/Actions/.github/workflows/ApplicationTesting.yml <JOBTMPL/ApplicationTesting>`
   * :ref:`pyTooling/Actions/.github/workflows/CheckDocumentation.yml <JOBTMPL/CheckDocumentation>`
   * :ref:`pyTooling/Actions/.github/workflows/StaticTypeCheck.yml <JOBTMPL/StaticTypeCheck>`
   * :ref:`pyTooling/Actions/.github/workflows/Package.yml <JOBTMPL/Package>`
   * :ref:`pyTooling/Actions/.github/workflows/PublishTestResults.yml <JOBTMPL/PublishTestResults>`
   * :ref:`pyTooling/Actions/.github/workflows/PublishCoverageResults.yml <JOBTMPL/PublishCoverageResults>`
   * :ref:`pyTooling/Actions/.github/workflows/SphinxDocumentation.yml <JOBTMPL/SphinxDocumentation>`
   * :ref:`pyTooling/Actions/.github/workflows/LaTeXDocumentation.yml <JOBTMPL/LaTeXDocumentation>`
   * :ref:`pyTooling/Actions/.github/workflows/PublishToGitHubPages.yml <JOBTMPL/PublishToGitHubPages>`
   * :ref:`pyTooling/Actions/.github/workflows/PublishOnPyPI.yml <JOBTMPL/PublishOnPyPI>`
   * :ref:`pyTooling/Actions/.github/workflows/TagReleaseCommit.yml <JOBTMPL/TagReleaseCommit>`
   * :ref:`pyTooling/Actions/.github/workflows/PublishReleaseNotes.yml <JOBTMPL/PublishReleaseNotes>`
   * :ref:`pyTooling/Actions/.github/workflows/IntermediateCleanUp.yml <JOBTMPL/IntermediateCleanUp>`

     * :gh:`geekyeggo/delete-artifact`

   * :ref:`pyTooling/Actions/.github/workflows/ArtifactCleanUp.yml <JOBTMPL/ArtifactCleanUp>`

     * :gh:`geekyeggo/delete-artifact`


.. _JOBTMPL/CompletePipeline/Instantiation:

Instantiation
*************

Simple Example
==============

The following instantiation example creates a job `Params` derived from job template `Parameters` version `r0`. It only
requires a `name` parameter to create the artifact names.

.. code-block:: yaml

   name: Pipeline

   on:
     push:
     workflow_dispatch:

   jobs:
     Params:
       uses: pyTooling/Actions/.github/workflows/CompletePipeline.yml@r5
       with:
         name: pyTooling

.. _JOBTMPL/CompletePipeline/Parameters:

Parameters
**********

.. topic:: Parameter Summary

   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | Parameter Name                                                      | Required | Type     | Default                                      |
   +=====================================================================+==========+==========+==============================================+
   | :ref:`JOBTMPL/CompletePipeline/Param/package_namespace`             | no       | string   | ``''``                                       |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/package_name`                  | yes      | string   | — — — —                                      |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/unittest_python_version`       | no       | string   | ``'3.13'``                                   |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/unittest_python_version_list`  | no       | string   | ``'3.9 3.10 3.11 3.12 3.13'``                |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/unittest_system_list`          | no       | string   | ``'ubuntu windows macos macos-arm ucrt64'``  |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/unittest_include_list`         | no       | string   | ``''``                                       |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/unittest_exclude_list`         | no       | string   | ``''``                                       |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/unittest_disable_list`         | no       | string   | ``''``                                       |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/apptest_python_version`        | no       | string   | ``'3.13'``                                   |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/apptest_python_version_list`   | no       | string   | ``''``                                       |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/apptest_system_list`           | no       | string   | ``'ubuntu windows macos macos-arm ucrt64'``  |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/apptest_include_list`          | no       | string   | ``''``                                       |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/apptest_exclude_list`          | no       | string   | ``''``                                       |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/apptest_disable_list`          | no       | string   | ``''``                                       |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/codecov`                       | no       | string   | ``'false'``                                  |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/codacy`                        | no       | string   | ``'false'``                                  |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/dorny`                         | no       | string   | ``'false'``                                  |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+
   | :ref:`JOBTMPL/CompletePipeline/Param/cleanup`                       | no       | string   | ``'true'``                                   |
   +---------------------------------------------------------------------+----------+----------+----------------------------------------------+

.. topic:: :ref:`Secret Summary <JOBTMPL/CompletePipeline/Secrets>`

   +-----------------------------------------------------------+----------+----------+--------------+
   | Token Name                                                | Required | Type     | Default      |
   +===========================================================+==========+==========+==============+
   | :ref:`JOBTMPL/CompletePipeline/Secret/PYPI_TOKEN`         | no       | string   | — — — —      |
   +-----------------------------------------------------------+----------+----------+--------------+
   | :ref:`JOBTMPL/CompletePipeline/Secret/CODECOV_TOKEN`      | no       | string   | — — — —      |
   +-----------------------------------------------------------+----------+----------+--------------+
   | :ref:`JOBTMPL/CompletePipeline/Secret/CODACY_TOKEN`       | no       | string   | — — — —      |
   +-----------------------------------------------------------+----------+----------+--------------+

.. topic:: :ref:`Output Summary <JOBTMPL/CompletePipeline/Results>`

   This job template has no output parameters.


.. _JOBTMPL/CompletePipeline/Param/package_namespace:

package_namespace
=================

+-------------------------------+----------+----------+--------------+
| Parameter Name                | Required | Type     | Default      |
+===============================+==========+==========+==============+
| package_namespace             | no       | string   | ``''``       |
+-------------------------------+----------+----------+--------------+

In case the package is a Python namespace package, the name of the library's or package's namespace needs to be
specified using this parameter. |br|
In case of a simple Python package, this parameter must be specified as an empty string (``''``), which is the default.

.. grid:: 2

   .. grid-item::
      :columns: 4

      .. rubric:: Example

      .. code-block:: yaml

         jobs:
           NamespacePackage:
             uses: pyTooling/Actions/.github/workflows/CompletePipeline.yml@r5
             with:
               package_namespace: myFramework
               package_name:      Extension

   .. grid-item::
      :columns: 4

      .. rubric:: Example

      .. code-block::

         📂ProjectRoot/
           📂myFramework/
             📂Extension/
               📦SubPackage/
                 🐍__init__.py
                 🐍SubModuleA.py
               🐍__init__.py
               🐍ModuleB.py


.. _JOBTMPL/CompletePipeline/Param/package_name:

package_name
============

+-------------------------------+----------+----------+--------------+
| Parameter Name                | Required | Type     | Default      |
+===============================+==========+==========+==============+
| package_name                  | yes      | string   | — — — —      |
+-------------------------------+----------+----------+--------------+

In case of a simple Python package, this package's name is specified using this parameter. |br|
In case the package is a Python namespace package, the parameter :ref:`JOBTMPL/CompletePipeline/Param/package_namespace`
must be specified, too.

.. rubric:: Example

.. grid:: 2

   .. grid-item::
      :columns: 4

      .. rubric:: Example

      .. code-block:: yaml

         jobs:
           SimplePackage:
             uses: pyTooling/Actions/.github/workflows/CompletePipeline.yml@r5
             with:
               package_name: myPackage

   .. grid-item::
      :columns: 4

      .. rubric:: Example

      .. code-block::

         📂ProjectRoot/
           📂myFramework/
             📦SubPackage/
               🐍__init__.py
               🐍SubModuleA.py
             🐍__init__.py
             🐍ModuleB.py

.. _JOBTMPL/CompletePipeline/Param/unittest_python_version:

unittest_python_version
=======================

+-------------------------------+----------+----------+--------------+
| Parameter Name                | Required | Type     | Default      |
+===============================+==========+==========+==============+
| unittest_python_version       | no       | string   | ``'3.13'``   |
+-------------------------------+----------+----------+--------------+

The default Python version used for intermediate jobs using Python tools.

In case :ref:`JOBTMPL/CompletePipeline/Param/unittest_python_version_list` is empty, this default version is used to
populate the ``unittest_python_version_list`` parameter.


.. _JOBTMPL/CompletePipeline/Param/unittest_python_version_list:

unittest_python_version_list
============================

+-------------------------------+----------+----------+-------------------------------------+
| Parameter Name                | Required | Type     | Default                             |
+===============================+==========+==========+=====================================+
| unittest_python_version_list  | no       | string   | ``'3.9 3.10 3.11 3.12 3.13'``       |
+-------------------------------+----------+----------+-------------------------------------+

The list of space-separated Python versions used for unit testing.

.. include:: ../PythonVersionList.rst


.. _JOBTMPL/CompletePipeline/Param/unittest_system_list:

unittest_system_list
====================

+-------------------------------+----------+----------+-----------------------------------------------------+
| Parameter Name                | Required | Type     | Default                                             |
+===============================+==========+==========+=====================================================+
| unittest_system_list          | no       | string   | ``'ubuntu windows macos macos-arm mingw64 ucrt64'`` |
+-------------------------------+----------+----------+-----------------------------------------------------+

The list of space-separated systems used for unit testing.

.. include:: ../SystemList.rst


.. _JOBTMPL/CompletePipeline/Param/unittest_include_list:

unittest_include_list
=====================

+-------------------------------+----------+----------+--------------+
| Parameter Name                | Required | Type     | Default      |
+===============================+==========+==========+==============+
| unittest_include_list         | no       | string   | ``''``       |
+-------------------------------+----------+----------+--------------+

The name of the library or package.


.. _JOBTMPL/CompletePipeline/Param/unittest_exclude_list:

unittest_exclude_list
=====================

+-------------------------------+----------+----------+--------------+
| Parameter Name                | Required | Type     | Default      |
+===============================+==========+==========+==============+
| unittest_exclude_list         | no       | string   | ``''``       |
+-------------------------------+----------+----------+--------------+

The name of the library or package.


.. _JOBTMPL/CompletePipeline/Param/unittest_disable_list:

unittest_disable_list
=====================

+-------------------------------+----------+----------+--------------+
| Parameter Name                | Required | Type     | Default      |
+===============================+==========+==========+==============+
| unittest_disable_list         | no       | string   | ``''``       |
+-------------------------------+----------+----------+--------------+

The name of the library or package.


.. _JOBTMPL/CompletePipeline/Param/apptest_python_version:

apptest_python_version
======================

+-------------------------------+----------+----------+--------------+
| Parameter Name                | Required | Type     | Default      |
+===============================+==========+==========+==============+
| apptest_python_version        | no       | string   | ``'3.13'``   |
+-------------------------------+----------+----------+--------------+

The name of the library or package.


.. _JOBTMPL/CompletePipeline/Param/apptest_python_version_list:

apptest_python_version_list
===========================

+-------------------------------+----------+----------+--------------+
| Parameter Name                | Required | Type     | Default      |
+===============================+==========+==========+==============+
| apptest_python_version_list   | no       | string   | ``''``       |
+-------------------------------+----------+----------+--------------+

The name of the library or package.


.. _JOBTMPL/CompletePipeline/Param/apptest_system_list:

apptest_system_list
===================

+-------------------------------+----------+----------+--------------------------------------------------+
| Parameter Name                | Required | Type     | Default                                          |
+===============================+==========+==========+==================================================+
| apptest_system_list           | no       | string   | ``'ubuntu windows macos macos-arm ucrt64'``      |
+-------------------------------+----------+----------+--------------------------------------------------+

The name of the library or package.


.. _JOBTMPL/CompletePipeline/Param/apptest_include_list:

apptest_include_list
====================

+-------------------------------+----------+----------+--------------+
| Parameter Name                | Required | Type     | Default      |
+===============================+==========+==========+==============+
| apptest_include_list          | no       | string   | ``''``       |
+-------------------------------+----------+----------+--------------+

The name of the library or package.


.. _JOBTMPL/CompletePipeline/Param/apptest_exclude_list:

apptest_exclude_list
====================

+-------------------------------+----------+----------+--------------+
| Parameter Name                | Required | Type     | Default      |
+===============================+==========+==========+==============+
| apptest_exclude_list          | no       | string   | ``''``       |
+-------------------------------+----------+----------+--------------+

The name of the library or package.


.. _JOBTMPL/CompletePipeline/Param/apptest_disable_list:

apptest_disable_list
====================

+-------------------------------+----------+----------+--------------+
| Parameter Name                | Required | Type     | Default      |
+===============================+==========+==========+==============+
| apptest_disable_list          | no       | string   | ``''``       |
+-------------------------------+----------+----------+--------------+

The name of the library or package.


.. _JOBTMPL/CompletePipeline/Param/codecov:

codecov
=======

+-------------------------------+----------+----------+--------------+
| Parameter Name                | Required | Type     | Default      |
+===============================+==========+==========+==============+
| codecov                       | no       | string   | ``'false'``  |
+-------------------------------+----------+----------+--------------+

The name of the library or package.


.. _JOBTMPL/CompletePipeline/Param/codacy:

codacy
======

+-------------------------------+----------+----------+--------------+
| Parameter Name                | Required | Type     | Default      |
+===============================+==========+==========+==============+
| codacy                        | no       | string   | ``'false'``  |
+-------------------------------+----------+----------+--------------+

The name of the library or package.


.. _JOBTMPL/CompletePipeline/Param/dorny:

dorny
=====

+-------------------------------+----------+----------+--------------+
| Parameter Name                | Required | Type     | Default      |
+===============================+==========+==========+==============+
| dorny                         | no       | string   | ``'false'``  |
+-------------------------------+----------+----------+--------------+

The name of the library or package.


.. _JOBTMPL/CompletePipeline/Param/cleanup:

cleanup
=======

+-------------------------------+----------+----------+--------------+
| Parameter Name                | Required | Type     | Default      |
+===============================+==========+==========+==============+
| cleanup                       | no       | string   | ``'true'``   |
+-------------------------------+----------+----------+--------------+

The name of the library or package.


.. _JOBTMPL/CompletePipeline/Secrets:

Secrets
*******

The workflow template uses the following secrets to publish results to other services.

.. _JOBTMPL/CompletePipeline/Secret/PYPI_TOKEN:

PYPI_TOKEN
==========

+-------------------------------+----------+----------+--------------+
| Token Name                    | Required | Type     | Default      |
+===============================+==========+==========+==============+
| PYPI_TOKEN                    | no       | string   | — — — —      |
+-------------------------------+----------+----------+--------------+

The name of the library or package.


.. _JOBTMPL/CompletePipeline/Secret/CODECOV_TOKEN:

CODECOV_TOKEN
=============

+-------------------------------+----------+----------+--------------+
| Token Name                    | Required | Type     | Default      |
+===============================+==========+==========+==============+
| CODECOV_TOKEN                 | no       | string   | — — — —      |
+-------------------------------+----------+----------+--------------+

The name of the library or package.


.. _JOBTMPL/CompletePipeline/Secret/CODACY_TOKEN:

CODACY_TOKEN
============

+-------------------------------+----------+----------+--------------+
| Token Name                    | Required | Type     | Default      |
+===============================+==========+==========+==============+
| CODACY_TOKEN                  | no       | string   | — — — —      |
+-------------------------------+----------+----------+--------------+

The name of the library or package.

.. _JOBTMPL/CompletePipeline/Results:

Results
*******

This job template has no output parameters.
