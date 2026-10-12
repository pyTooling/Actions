.. _JOBTMPL/Package:
.. index::
   single: build; Package Template
   single: wheel; Package Template
   single: GitHub Action Reusable Workflow; Package Template

Package
#######

This job packages the Python source code as a source package (``*.tar.gz``) and wheel package (``*.whl``) and uploads it
as an artifact.

.. topic:: Features

   * Package source code as wheel and source distribution.
   * Support packaging using :term:`build` (recommended) or :pypi:`setuptools`.
   * Check the packages' metadata for direct references, which :term:`PyPI` rejects.

.. topic:: Behavior

   1. Checkout repository.
   2. Setup Python and install dependencies.
   3. Package the Python sources:

      * If parameter :ref:`JOBTMPL/Package/Input/requirements` is empty, use :term:`build` for packaging and execute
        ``python -m build ...``.
      * If parameter :ref:`JOBTMPL/Package/Input/requirements` is ``no-isolation``, use :term:`build` for packaging in
        *no-isolation* mode executing ``python -m build --no-isolation ...``.
      * If parameter :ref:`JOBTMPL/Package/Input/requirements` is non-empty, use :pypi:`setuptools` for packaging and
        execute ``python setup.py ...``.

      Both a source distribution and a wheel are built.

   4. Check both packages' metadata (``Requires-Dist``) for direct references like
      ``name @ git+https://...``, which :term:`PyPI` rejects. Each reference is reported as a warning naming the
      requirement, its extras and the packages it appears in. The result is the output
      :ref:`JOBTMPL/Package/Output/pypi_compliant`.
   5. Upload both packages in a single artifact
      (:ref:`JOBTMPL/Package/Input/artifact`).

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-Package.png
      :width: 500px

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * :gh:`actions/setup-python`
   * :ghsrc:`CheckPyPICompliance <.github/actions/CheckPyPICompliance>`

     * :pypi:`packaging`

   * :gh:`pyTooling/upload-artifact`

     * :gh:`actions/upload-artifact`

   * pip

     * :term:`build` (:pypi:`PyPI package <build>`)
     * :term:`wheel` (:pypi:`PyPI package <wheel>`)

.. _JOBTMPL/Package/Instantiation:

Instantiation
*************

Simple Example
==============

.. code-block:: yaml

   jobs:
     Package:
       uses: pyTooling/Actions/.github/workflows/Package.yml@r8
       with:
         artifact: Package


Complex Example
===============

.. code-block:: yaml

   jobs:
     Package:
       uses: pyTooling/Actions/.github/workflows/Package.yml@r8
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
| :ref:`JOBTMPL/Package/Input/ubuntu_image_version`                   | no       | string   | ``'26.04'``                                                       |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Package/Input/python_version`                         | no       | string   | ``'3.15'``                                                        |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Package/Input/requirements`                           | no       | string   | ``''``                                                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Package/Input/artifact`                               | yes      | string   | — — — —                                                           |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/Package/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/Package/Outputs>`

+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| Result Name                                                         | Type     | Description                                                       |
+=====================================================================+==========+===================================================================+
| :ref:`JOBTMPL/Package/Output/pypi_compliant`                        | string   | ``'true'``, if no package has a direct reference.                 |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+


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
:Behavior:        If the value is an empty string, :term:`build` is used for packaging. |br|
                  if the value is ``no-isolation``, :term:`build` is used in *no-isolation* mode for packaging. |br|
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

.. _JOBTMPL/Package/Output/pypi_compliant:

pypi_compliant
==============

:Type:            string
:Possible Values: ``'true'`` / ``'false'``
:Description:     ``'false'``, if the metadata of a built package - wheel or source distribution - has a direct
                  reference in ``Requires-Dist`` (``name @ git+https://...``, ``name @ https://...``), which
                  :term:`PyPI` rejects with *400 Bad Request*; else ``'true'``. Each reference is reported as a
                  warning of the *Package* job. |br|
                  Pass it to :ref:`JOBTMPL/TagReleaseCommit/Input/pypi_compliant` to refuse tagging such a release,
                  and to :ref:`JOBTMPL/PublishOnPyPI/Input/pypi_compliant` to refuse its upload.


.. _JOBTMPL/Package/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).
