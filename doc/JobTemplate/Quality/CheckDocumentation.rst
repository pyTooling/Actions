.. _JOBTMPL/CheckDocumentation:

CheckDocumentation
##################

The ``CheckDocumentation`` job checks the level of documentation coverage for Python files.

.. topic:: Features

   * Check documentation coverage in Python code using :pypi:`docstr_coverage`.
   * Check documentation coverage in Python code using :pypi:`interrogate`.

.. topic:: Behavior

   1. Checkout repository.
   2. Setup Python environment and install dependencies.
   3. Run ``docstr_coverage``.
   3. Run ``interrogate``.

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-CheckDocumentation.png
      :width: 600px

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * :gh:`actions/setup-python`
   * pip

     * :pypi:`docstr_coverage`
     * :pypi:`interrogate`


.. _JOBTMPL/CheckDocumentation/Instantiation:

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
     ConfigParams:
       uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5
       with:
         package_name: myPackage

     DocCoverage:
       uses: pyTooling/Actions/.github/workflows/CheckDocumentation.yml@r5
       needs:
         - ConfigParams
       with:
         directory:    ${{ needs.ConfigParams.outputs.package_directory }}


.. seealso::

   :ref:`JOBTMPL/ConfigParams`
     ``ConfigParams`` is usualy


.. _JOBTMPL/CheckDocumentation/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/CheckDocumentation/Inputs>`

+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                          | Required | Type     | Default                                                           |
+=========================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/CheckDocumentation/Input/ubuntu_image_version`            | no       | string   | ``'24.04'``                                                       |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/CheckDocumentation/Input/python_version`                  | no       | string   | ``'3.13'``                                                        |
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

ubuntu_image_version
====================

:Type:            string
:Required:        no
:Default Value:   ``'24.04'``
:Possible Values: See `actions/runner-images - Available Images <https://github.com/actions/runner-images?tab=readme-ov-file#available-images>`__
                  for available Ubuntu image versions.
:Description:     Version of the Ubuntu image used to run this job.

                  .. note::

                     Unfortunately, GitHub Actions has only a `limited set of functions <https://docs.github.com/en/actions/reference/workflows-and-actions/expressions#functions>`__,
                     thus, the usual Ubuntu image name like ``'ubuntu-24.04'`` can't be split into image name and image
                     version.


.. _JOBTMPL/CheckDocumentation/Input/python_version:

python_version
==============

:Type:            string
:Required:        no
:Default Value:   ``'3.13'``
:Possible Values: Any valid Python version conforming to the pattern ``<major>.<minor>`` or ``pypy-<major>.<minor>``. |br|
                  See `actions/python-versions - available Python versions <https://github.com/actions/python-versions>`__
                  and `actions/setup-python - configurable Python versions <https://github.com/actions/setup-python>`__.
:Description:     Python version used to run Python code in this job.


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
