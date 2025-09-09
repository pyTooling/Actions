.. _JOBTMPL/IntermediateCleanUp:

IntermediateCleanUp
###################

The ``IntermediateCleanUp`` job template is used to remove intermediate artifacts like unit test artifacts for each job
variant after test results have been merged into a single file.

.. topic:: Features

   * Delete artifacts from pipeline.

.. topic:: Behavior

   1. Delete all SQLite code coverage artifacts if given as a parameter.
   2. Delete all JUnit XML report artifacts if given as a parameter.

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-IntermediateCleanUp.png
      :width: 400px

.. topic:: Dependencies

   * :gh:`geekyeggo/delete-artifact`


.. _JOBTMPL/IntermediateCleanUp/Instantiation:

Instantiation
*************

The following instantiation example creates a ``Params`` job derived from job template ``Parameters`` version ``@r5``. It only
requires a `name` parameter to create the artifact names.

.. code-block:: yaml

   name: Pipeline

   on:
     push:
     workflow_dispatch:

   jobs:
     Params:
       uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5
       with:
         name: pyTooling


.. seealso::

   :ref:`JOBTMPL/ArtifactCleanup`
     ``ArtifactCleanup`` is used to remove artifacts like unit test report artifacts after artifact's content has been
     (post-)processed or published.


.. _JOBTMPL/IntermediateCleanUp/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/IntermediateCleanUp/Inputs>`

+----------------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| Parameter Name                                                             | Required | Type     | Default                                           |
+============================================================================+==========+==========+===================================================+
| :ref:`JOBTMPL/IntermediateCleanUp/Input/ubuntu_image_version`              | no       | string   | ``'24.04'``                                       |
+----------------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/IntermediateCleanUp/Input/sqlite_coverage_artifacts_prefix`  | no       | string   | ``''``                                            |
+----------------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/IntermediateCleanUp/Input/xml_unittest_artifacts_prefix`     | no       | string   | ``''``                                            |
+----------------------------------------------------------------------------+----------+----------+---------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/IntermediateCleanUp/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/IntermediateCleanUp/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/IntermediateCleanUp/Inputs:

Input Parameters
****************

.. _JOBTMPL/IntermediateCleanUp/Input/ubuntu_image_version:

.. include:: ../_ubuntu_image_version.rst


.. _JOBTMPL/IntermediateCleanUp/Input/sqlite_coverage_artifacts_prefix:

sqlite_coverage_artifacts_prefix
================================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name including ``*``.
:Description:     Prefix for SQLite coverage artifacts to be removed.


.. _JOBTMPL/IntermediateCleanUp/Input/xml_unittest_artifacts_prefix:

xml_unittest_artifacts_prefix
=============================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name including ``*``.
:Description:     Prefix for XML unittest artifacts to be removed.


.. _JOBTMPL/IntermediateCleanUp/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/IntermediateCleanUp/Outputs:

Outputs
*******

This job template has no output parameters.


.. _JOBTMPL/IntermediateCleanUp/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).
