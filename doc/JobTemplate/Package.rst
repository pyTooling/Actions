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

* actions/checkout@v2
* actions/setup-python@v2
* actions/upload-artifact@v2

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

Python version.

+----------+----------+----------+
| Required | Type     | Default  |
+==========+==========+==========+
| optional | string   | 3.11     |
+----------+----------+----------+

requirements
============

Python dependencies to be installed through pip; if empty, use pyproject.toml through build.

+----------+----------+----------+
| Required | Type     | Default  |
+==========+==========+==========+
| optional | string   | ``""``   |
+----------+----------+----------+

artifact
========

Name of the package artifact.

+----------+----------+----------+
| Required | Type     | Default  |
+==========+==========+==========+
| yes      | string   | — — — —  |
+----------+----------+----------+

Secrets
*******

This job template needs no secrets.

Results
*******

This job template has no output parameters.
