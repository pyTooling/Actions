.. _JOBTMPL/InstallPackage:

InstallPackage (beta)
#####################

The ``InstallPackage`` job template takes a generated Python package and installs it on the target platform. Afterwards
the installation is verified. This aims for packaging and dependency mistakes in the package.

.. topic:: Features

   * Install generated Python package on the target platform.

.. topic:: Behavior

   * Download Python package as artifact.
   * Prepare the Python environment.
   * Install the Python package using ``pip``.
   * Read out and verify the package version.

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-InstallPackage.png
      :width: 600px

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * :gh:`pyTooling/download-artifact`

     * :gh:`actions/download-artifact`

   * :gh:`msys2/setup-msys2`
   * :gh:`actions/setup-python`
   * pip

     * :pypi:`pip`
     * :pypi:`wheel`


.. _JOBTMPL/InstallPackage/Instantiation:

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

   :ref:`JOBTMPL/Package`
     ``InstallPackage`` is usualy


.. _JOBTMPL/InstallPackage/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/InstallPackage/Inputs>`

+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                      | Required | Type     | Default                                                           |
+=====================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/InstallPackage/Input/ubuntu_image`                    | no       | string   | ``'ubuntu-24.04'``                                                |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/InstallPackage/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/InstallPackage/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/InstallPackage/Inputs:

Input Parameters
****************

.. _JOBTMPL/InstallPackage/Input/ubuntu_image:

ubuntu_image
============


.. _JOBTMPL/InstallPackage/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/InstallPackage/Outputs:

Outputs
*******

This job template has no output parameters.


.. _JOBTMPL/InstallPackage/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).
