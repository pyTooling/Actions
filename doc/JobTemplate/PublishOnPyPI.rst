.. _JOBTMPL/PublishOnPyPI:

PublishOnPyPI
#############

Publish a source (``*.tar.gz``) package and/or wheel (``*.whl``) packages to `PyPI <https://pypi.org/>`__.

**Behavior:**

1. Download package artifact
2. Publish source package(s) (``*.tar.gz``)
3. Publish wheel package(s) (``*.whl``)
4. Delete the artifact

**Preconditions:**

A PyPI account was created and the package name is either not occupied or the user has access rights for that package.

**Requirements:**

Setup a secret (e.g. ``PYPI_TOKEN``) in GitHub to handover the PyPI token to the job.

**Dependencies:**

* :gh:`actions/download-artifact`
* :gh:`actions/setup-python`
* :gh:`geekyeggo/delete-artifact`


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
       uses: pyTooling/Actions/.github/workflows/PublishOnPyPI.yml@r0
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
       uses: pyTooling/Actions/.github/workflows/PublishOnPyPI.yml@r0
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


Parameters
**********

python_version
==============

+----------------+----------+----------+----------+
| Parameter Name | Required | Type     | Default  |
+================+==========+==========+==========+
| python_version | optional | string   | ``3.11`` |
+----------------+----------+----------+----------+

Python version used for uploading the package contents via `twine` to PyPI.


requirements
============

+----------------+----------+----------+-----------------+
| Parameter Name | Required | Type     | Default         |
+================+==========+==========+=================+
| requirements   | optional | string   | ``wheel twine`` |
+----------------+----------+----------+-----------------+

List of requirements to be installed for uploading the package contents to PyPI.


artifact
========

+----------------+----------+----------+--------------+
| Parameter Name | Required | Type     | Default      |
+================+==========+==========+==============+
| artifact       | yes      | string   | — — — —      |
+----------------+----------+----------+--------------+

Name of the artifact containing the package(s).


Secrets
*******

PYPI_TOKEN
==========

+----------------+----------+----------+--------------+
| Secret Name    | Required | Type     | Default      |
+================+==========+==========+==============+
| PYPI_TOKEN     | yes      | string   | — — — —      |
+----------------+----------+----------+--------------+

The token to access the package at PyPI for uploading new data.


Results
*******

This job template has no output parameters.
