.. _JOBTMPL/CheckDocumentation:
.. index::
   single: docstr_coverage; CheckDocumentation Template
   single: interrogate; CheckDocumentation Template
   single: GitHub Action Reusable Workflow; CheckDocumentation Template

CheckDocumentation
##################

The ``CheckDocumentation`` job checks the level of documentation coverage for Python files.

.. topic:: Features

   * Check documentation coverage in Python code using :term:`docstr_coverage`.
   * Check documentation coverage in Python code using :term:`interrogate`.

.. topic:: Behavior

   1. Checkout repository.
   2. Setup Python (:ref:`JOBTMPL/CheckDocumentation/Input/python_version`) and install the dependencies.
   3. Run :term:`interrogate` on :ref:`JOBTMPL/CheckDocumentation/Input/directory`, failing below
      :ref:`JOBTMPL/CheckDocumentation/Input/fail_under` percent.
   4. Run :term:`docstr_coverage` on :ref:`JOBTMPL/CheckDocumentation/Input/directory`.

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-CheckDocumentation.png
      :width: 600px

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * :gh:`actions/setup-python`
   * pip

     * :term:`docstr_coverage` (:pypi:`PyPI package <docstr_coverage>`)
     * :term:`interrogate` (:pypi:`PyPI package <interrogate>`)

.. _JOBTMPL/CheckDocumentation/Instantiation:

Instantiation
*************

The following instantiation example creates a ``Params`` job derived from job template ``Parameters`` version ``@r7``. It only
requires a `name` parameter to create the artifact names.

.. code-block:: yaml

   jobs:
     ConfigParams:
       uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r7
       with:
         package_name: myPackage

     DocCoverage:
       uses: pyTooling/Actions/.github/workflows/CheckDocumentation.yml@r7
       needs:
         - ConfigParams
       with:
         directory: ${{ needs.ConfigParams.outputs.package_directory }}


.. seealso::

   :ref:`JOBTMPL/ExtractConfiguration`
     ``ExtractConfiguration`` is usually used to compute the path to the package's source code directory.


.. _JOBTMPL/CheckDocumentation/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/CheckDocumentation/Inputs>`

+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                          | Required | Type     | Default                                                           |
+=========================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/CheckDocumentation/Input/ubuntu_image_version`            | no       | string   | ``'26.04'``                                                       |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/CheckDocumentation/Input/python_version`                  | no       | string   | ``'3.14'``                                                        |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/CheckDocumentation/Input/directory`                       | yes      | string   | — — — —                                                           |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/CheckDocumentation/Input/fail_under`                      | no       | string   | ``'80'``                                                          |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/CheckDocumentation/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/CheckDocumentation/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/CheckDocumentation/Inputs:

Input Parameters
****************

.. _JOBTMPL/CheckDocumentation/Input/ubuntu_image_version:

.. include:: ../_ubuntu_image_version.rst


.. _JOBTMPL/CheckDocumentation/Input/python_version:

.. include:: ../_python_version.rst


.. _JOBTMPL/CheckDocumentation/Input/directory:

directory
=========

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: Any valid directory or sub-directory.
:Description:     Directory where the Python code is located.


.. _JOBTMPL/CheckDocumentation/Input/fail_under:

fail_under
==========

:Type:            string
:Required:        no
:Default Value:   ``'80'``
:Possible Values: Any valid percentage from 0 to 100 encoded as string.
:Description:     A minimum percentage level for good documentation. If the documentation coverage is below this level,
                  the coverage is considered a fail.


.. _JOBTMPL/CheckDocumentation/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/CheckDocumentation/Outputs:

Outputs
*******

This job template has no output parameters.
