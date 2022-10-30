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
         python_version: ${{ fromJson(needs.Params.outputs.params).python_version }}
         requirements: -r dist/requirements.txt
         artifact: ${{ fromJson(needs.Params.outputs.params).artifacts.Package }}
       secrets:
         PYPI_TOKEN: ${{ secrets.PYPI_TOKEN }}

Parameters
**********

python_version
==============

Python version used for uploading the package contents via `twine` to PyPI.

+----------+----------+----------+
| Required | Type     | Default  |
+==========+==========+==========+
| optional | string   | 3.11     |
+----------+----------+----------+


requirements
============

List of requirements to be installed for uploading the package contents to PyPI.

+----------+----------+--------------+
| Required | Type     | Default      |
+==========+==========+==============+
| optional | string   | wheel, twine |
+----------+----------+--------------+


artifact
========

Name of the artifact containing the package(s).

+----------+----------+--------------+
| Required | Type     | Default      |
+==========+==========+==============+
| yes      | string   | — — — —      |
+----------+----------+--------------+

Secrets
*******

PYPI_TOKEN
==========

The token to access the package at PyPI for uploading new data.

+----------+----------+--------------+
| Required | Type     | Default      |
+==========+==========+==============+
| yes      | string   | — — — —      |
+----------+----------+--------------+

Results
*******

*None*

Dependencies
************

* actions/download-artifact
* actions/setup-python
* geekyeggo/delete-artifact
