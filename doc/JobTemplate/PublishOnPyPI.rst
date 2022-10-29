PublishOnPyPI
#############

Publish a source (``*.tar.gz``) and wheel (``*.whl``) packages to `PyPI <https://pypi.org/>`__.

Instantiation
*************

Simple Example
==============

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

.. code-block:: yaml

   jobs:
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

Template Parameters
*******************

python_version
==============

Python version used for uploading the package contents via `twine` to PyPI.

**Default:** 3.11

requirements
============

List of requirements to be installed for uploading the package contents to PyPI.

**Default:** wheel, twine

artifact
========

Name of the artifact containing the package(s).

Secrets
*******

PYPI_TOKEN
==========

The token to access the package at PyPI for uploading new data.

Template Results
****************

*None*

Dependencies
************

* actions/download-artifact
* actions/setup-python
* geekyeggo/delete-artifact
