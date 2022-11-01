.. _JOBTMPL/StaticTypeChecking:

StaticTypeCheck
###############

This job runs a static type check using mypy and collects the results. These results can be converted to a HTML report
and then uploaded as an artifact.

**Behavior:**

1. Checkout repository
2. Setup Python and install dependencies
3. Run type checking command(s).
4. Upload type checking report as an artifact

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
     StaticTypeCheck:
       uses: pyTooling/Actions/.github/workflows/StaticTypeCheck.yml@r0
       with:
         commands: |
           touch pyTooling/__init__.py
           mypy --html-report htmlmypy -p pyTooling
         report: 'htmlmypy'
         artifact: TypeChecking

Complex Example
===============

.. code-block:: yaml

   jobs:
     StaticTypeCheck:
       uses: pyTooling/Actions/.github/workflows/StaticTypeCheck.yml@r0
       needs:
         - Params
       with:
         python_version: ${{ fromJson(needs.Params.outputs.params).python_version }}
         commands: |
           touch pyTooling/__init__.py
           mypy --html-report htmlmypy -p pyTooling
         report: 'htmlmypy'
         artifact: ${{ fromJson(needs.Params.outputs.params).artifacts.typing }}

Commands
========

Example ``commands``:

1. Regular package

   .. code-block:: yaml

      commands: mypy --html-report htmlmypy -p ToolName


2. Parent namespace package

   .. code-block:: yaml

      commands: |
        touch Parent/__init__.py
        mypy --html-report htmlmypy -p ToolName

3. Child namespace package

   .. code-block:: yaml

      commands: |
        cd Parent
        mypy --html-report ../htmlmypy -p ToolName

Parameters
**********

python_version
==============

Python version.

+----------+----------+-----------------+
| Required | Type     | Default         |
+==========+==========+=================+
| optional | string   | ``3.11``        |
+----------+----------+-----------------+


requirements
============

Python dependencies to be installed through pip.

+----------+----------+-------------------------------+
| Required | Type     | Default                       |
+==========+==========+===============================+
| optional | string   | ``-r tests/requirements.txt`` |
+----------+----------+-------------------------------+


report
======

Directory to upload as an artifact.

+----------+----------+-----------------+
| Required | Type     | Default         |
+==========+==========+=================+
| optional | string   | ``htmlmypy``    |
+----------+----------+-----------------+


commands
========

Commands to run the static type checks.

+----------+----------+--------------+
| Required | Type     | Default      |
+==========+==========+==============+
| yes      | string   | — — — —      |
+----------+----------+--------------+

artifact
========

Name of the typing artifact.

+----------+----------+--------------+
| Required | Type     | Default      |
+==========+==========+==============+
| yes      | string   | — — — —      |
+----------+----------+--------------+

Secrets
*******

This job template needs no secrets.

Results
*******

This job template has no output parameters.