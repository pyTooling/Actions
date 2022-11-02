.. _JOBTMPL/Package:

Package
#######

This job packages the Python source code as a source package (``*.tar.gz``) and wheel package (``*.whl``) and uploads it
as an artifact.

**Behavior:**

1. Checkout repository
2. Setup Python and install dependencies
3. Package Python sources:

   * If parameter ``requirements`` is empty, use ``build`` package and run ``python build``.
   * If parameter ``requirements`` is ``no-isolation``, use ``build`` package in *no-isolation* mode and run
     ``python build``.
   * If parameter ``requirements`` is non-empty, use ``setuptools`` package and run ``python setup.py``.

**Dependencies:**

* :gh:`actions/checkout`
* :gh:`actions/setup-python`
* :gh:`actions/upload-artifact`

Instantiation
*************

Simple Example
==============

.. code-block:: yaml

   jobs:
     Package:
       uses: pyTooling/Actions/.github/workflows/Package.yml@r0
       with:
         artifact: Package


Complex Example
===============

.. code-block:: yaml

   jobs:
     Package:
       uses: pyTooling/Actions/.github/workflows/Package.yml@r0
       needs:
         - Params
         - Coverage
       with:
         python_version: ${{ fromJson(needs.Params.outputs.params).python_version }}
         requirements: -r build/requirements.txt
         artifact: ${{ fromJson(needs.Params.outputs.params).artifacts.Package }}


Parameters
**********

python_version
==============

+----------------+----------+----------+----------+
| Parameter Name | Required | Type     | Default  |
+================+==========+==========+==========+
| python_version | optional | string   | 3.11     |
+----------------+----------+----------+----------+

Python version.


requirements
============

+----------------+----------+----------+----------+
| Parameter Name | Required | Type     | Default  |
+================+==========+==========+==========+
| requirements   | optional | string   | ``""``   |
+----------------+----------+----------+----------+

Python dependencies to be installed through pip; if empty, use pyproject.toml through build.


artifact
========

+----------------+----------+----------+----------+
| Parameter Name | Required | Type     | Default  |
+================+==========+==========+==========+
| artifact       | yes      | string   | — — — —  |
+----------------+----------+----------+----------+

Name of the package artifact.


Secrets
*******

This job template needs no secrets.


Results
*******

This job template has no output parameters.
