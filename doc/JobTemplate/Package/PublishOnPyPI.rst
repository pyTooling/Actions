.. _JOBTMPL/PublishOnPyPI:
.. index::
   single: PyPI; PublishOnPyPI Template
   single: twine; PublishOnPyPI Template
   single: GitHub Action Reusable Workflow; PublishOnPyPI Template

PublishOnPyPI
#############

Publish a wheel (``*.whl``) packages and/or source (``*.tar.gz``) package to `PyPI <https://pypi.org/>`__.

.. topic:: Features

   * Publish a Python package to `PyPI <https://pypi.org/>`__.

.. topic:: Behavior

   1. Download package artifact
   2. Publish source package(s) (``*.tar.gz``)
   3. Publish wheel package(s) (``*.whl``)
   4. Delete the artifact

.. topic:: Preconditions

   1. A PyPI account was created and the package name is either not occupied or the user has access rights for that
      package.
   2. An access token was generated at PyPI, which can be used for uploading packages.
   3. A secret (e.g. ``PYPI_TOKEN``) was setup in GitHub Actions to handover the PyPI token to the pipeline.

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-PublishOnPyPI.png
      :width: 500px

.. topic:: Dependencies

   * :gh:`pyTooling/download-artifact`

     * :gh:`actions/download-artifact`
   * :gh:`actions/setup-python`
   * :gh:`geekyeggo/delete-artifact`

   * pip

     * :pypi:`wheel`
     * :pypi:`twine`


.. _JOBTMPL/PublishOnPyPI/Instantiation:

Instantiation
*************

Simple Example
==============

The following example demonstrates how to publish the artifact named ``Package`` to PyPI on every pipeline run triggered
by a Git tag. A secret is forwarded from GitHub secrets to a job secret.

.. code-block:: yaml

   jobs:
     # ...

     PublishOnPyPI:
       uses: pyTooling/Actions/.github/workflows/PublishOnPyPI.yml@r5
       if: startsWith(github.ref, 'refs/tags')
       with:
         artifact: Package
       secrets:
         PYPI_TOKEN: ${{ secrets.PYPI_TOKEN }}

Complex Example
===============

In this more complex example, the job depends on a parameter creation (``Params``) and packaging job (``Package``). The
used Python version is overwritten by a parameter calculated in the ``Params`` jobs. Also the artifact name is managed
by that job. Finally, the list of requirements is overwritten to load a list of requirements from ``dist/requirements.txt``.

.. code-block:: yaml

   jobs:
     Params:
       # ...

     Package:
       # ...

     PublishOnPyPI:
       uses: pyTooling/Actions/.github/workflows/PublishOnPyPI.yml@r5
       if: startsWith(github.ref, 'refs/tags')
       needs:
         - Params
         - Package
       with:
         python_version: ${{ needs.Params.outputs.python_version }}
         requirements: -r dist/requirements.txt
         artifact: ${{ fromJson(needs.Params.outputs.artifact_names).package_all }}
       secrets:
         PYPI_TOKEN: ${{ secrets.PYPI_TOKEN }}

.. seealso::

   :ref:`JOBTMPL/Package`


.. _JOBTMPL/PublishOnPyPI/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/PublishOnPyPI/Inputs>`

+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                      | Required | Type     | Default                                                           |
+=====================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/PublishOnPyPI/Input/ubuntu_image_version`             | no       | string   | ``'24.04'``                                                       |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishOnPyPI/Input/python_version`                   | no       | string   | ``'3.13'``                                                        |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishOnPyPI/Input/requirements`                     | no       | string   | ``'wheel twine'``                                                 |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishOnPyPI/Input/artifact`                         | yes      | string   | — — — —                                                           |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/PublishOnPyPI/Secrets>`

+-----------------------------------------------------------+----------+----------+--------------+
| Token Name                                                | Required | Type     | Default      |
+===========================================================+==========+==========+==============+
| :ref:`JOBTMPL/PublishOnPyPI/Secret/PYPI_TOKEN`            | no       | string   | — — — —      |
+-----------------------------------------------------------+----------+----------+--------------+

.. rubric:: Goto :ref:`output parameters <JOBTMPL/PublishOnPyPI/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/PublishOnPyPI/Inputs:

Input Parameters
****************

.. _JOBTMPL/PublishOnPyPI/Input/ubuntu_image_version:

.. include:: ../_ubuntu_image_version.rst


.. _JOBTMPL/PublishOnPyPI/Input/python_version:

.. include:: ../_python_version.rst


.. _JOBTMPL/PublishOnPyPI/Input/requirements:

requirements
============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid list of parameters for ``pip install``. |br|
                  Either a requirements file can be referenced using ``'-r path/to/requirements.txt'``, or a list of
                  packages can be specified using a space separated list like ``'wheel twine'``.
:Description:     Python dependencies to be installed through *pip*.


.. _JOBTMPL/PublishOnPyPI/Input/artifact:

artifact
========

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the packaged Python package(s).


.. _JOBTMPL/PublishOnPyPI/Secrets:

Secrets
*******


.. _JOBTMPL/PublishOnPyPI/Secret/PYPI_TOKEN:

PYPI_TOKEN
==========

:Type:            string
:Required:        no
:Default Value:   — — — —
:Description:     The token to publish and upload packages on `PyPI <https://pypi.org/>`__.


.. _JOBTMPL/PublishOnPyPI/Outputs:

Outputs
*******

This job template has no output parameters.


.. _JOBTMPL/PublishOnPyPI/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).
