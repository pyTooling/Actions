.. _JOBTMPL/Package:
.. index::
   single: build; Package Template
   single: GitHub Action Reusable Workflow; Package Template

Package
#######

This job packages the Python source code as a source package (``*.tar.gz``) and wheel package (``*.whl``) and uploads it
as an artifact.

.. topic:: Features

   * Package source code as wheel and source distribution.
   * Support packaging using :pypi:`build` (recommended) or :pypi:`setuptools`.

.. topic:: Behavior

   1. Checkout repository.
   2. Setup Python and install dependencies.
   3. Package Python sources:

      * If parameter :ref:`JOBTMPL/Package/Input/requirements` is empty, use :pypi:`build` for packaging and execute
        ``python -m build ...``.
      * If parameter :ref:`JOBTMPL/Package/Input/requirements` is ``no-isolation``, use :pypi:`build` for packaging in
        *no-isolation* mode executing ``python -m build --no-isolation ...``.
      * If parameter :ref:`JOBTMPL/Package/Input/requirements` is non-empty, use :pypi:`setuptools` for package and
        execute ``python setup.py ...``.

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-Package.png
      :width: 500px

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * :gh:`actions/setup-python`
   * :gh:`pyTooling/upload-artifact`

     * :gh:`actions/upload-artifact`

   * pip

     * :pypi:`build`
     * :pypi:`wheel`


.. _JOBTMPL/Package/Instantiation:

Instantiation
*************

Simple Example
==============

.. code-block:: yaml

   jobs:
     Package:
       uses: pyTooling/Actions/.github/workflows/Package.yml@r6
       with:
         artifact: Package


Complex Example
===============

.. code-block:: yaml

   jobs:
     Package:
       uses: pyTooling/Actions/.github/workflows/Package.yml@r6
       needs:
         - Params
       with:
         python_version: ${{ needs.Params.outputs.python_version }}
         requirements: -r build/requirements.txt
         artifact: ${{ fromJson(needs.Params.outputs.artifact_names).package_all }}


.. _JOBTMPL/Package/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/Package/Inputs>`

+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                      | Required | Type     | Default                                                           |
+=====================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/Package/Input/ubuntu_image_version`                   | no       | string   | ``'24.04'``                                                       |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Package/Input/python_version`                         | no       | string   | ``'3.13'``                                                        |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Package/Input/requirements`                           | no       | string   | ``''``                                                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Package/Input/artifact`                               | yes      | string   | — — — —                                                           |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/Package/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/Package/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/Package/Inputs:

Input Parameters
****************

.. _JOBTMPL/Package/Input/ubuntu_image_version:

.. include:: ../_ubuntu_image_version.rst


.. _JOBTMPL/Package/Input/python_version:

.. include:: ../_python_version.rst


.. _JOBTMPL/Package/Input/requirements:

requirements
============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid list of parameters for ``pip install``. |br|
                  Either a requirements file can be referenced using ``'-r path/to/requirements.txt'``, or a list of
                  packages can be specified using a space separated list like ``'build wheel'``.
:Behavior:        If the value is an empty string, :pypi:`build` is used for packaging. |br|
                  if the value is ``no-isolation``, :pypi:`build` is used in *no-isolation* mode for packaging. |br|
                  otherwise, a list of requirements is assumed and :pypi:`setuptools` is used for packaging.
:Description:     Python dependencies to be installed through *pip*.


.. _JOBTMPL/Package/Input/artifact:

artifact
========

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the packaged Python code.


.. _JOBTMPL/Package/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/Package/Outputs:

Outputs
*******

This job template has no output parameters.


.. _JOBTMPL/Package/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).
