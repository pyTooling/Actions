.. _JOBTMPL/BuildTheDocs:

BuildTheDocs
############

This jobs compiles the documentation written in ReStructured Text with Sphinx using BuildTheDocs.

**Behavior:**

1. Checkout repository.
2. Build the documentation.
3. Upload the HTML documentation as an artifact.

**Dependencies:**

* :gh:`actions/checkout`
* :gh:`buildthedocs/btd`
* :gh:`actions/upload-artifact`


Instantiation
*************

Simple Example
==============

.. code-block:: yaml

   jobs:
     BuildTheDocs:
       uses: pyTooling/Actions/.github/workflows/BuildTheDocs.yml@r0
       with:
         artifact: Documentation

Complex Example
===============

.. code-block:: yaml

   jobs:
     BuildTheDocs:
       uses: pyTooling/Actions/.github/workflows/BuildTheDocs.yml@r0
       needs:
         - Params
       with:
         artifact: ${{ fromJson(needs.Params.outputs.params).artifacts.doc }}


Parameters
**********

artifact
========

Name of the documentation artifact.

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
