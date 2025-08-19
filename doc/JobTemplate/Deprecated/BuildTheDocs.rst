.. _JOBTMPL/BuildTheDocs:

BuildTheDocs
############

This jobs compiles the documentation written in ReStructured Text with Sphinx using BuildTheDocs.

**Behavior:**

1. Checkout repository.
2. Build the documentation.
3. Upload the HTML documentation as an artifact.
4. Publish the HTML documentation to GitHub Pages.

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
       uses: pyTooling/Actions/.github/workflows/BuildTheDocs.yml@r5


Complex Example
===============

.. code-block:: yaml

   jobs:
     BuildTheDocs:
       uses: pyTooling/Actions/.github/workflows/BuildTheDocs.yml@r5
       needs:
         - Params
       with:
         artifact: ${{ fromJson(needs.Params.outputs.artifact_names).documentation_html }}


Parameters
**********

artifact
========

+----------------+----------+----------+--------------+
| Parameter Name | Required | Type     | Default      |
+================+==========+==========+==============+
| artifact       | optional | string   | ``""``       |
+----------------+----------+----------+--------------+

Name of the documentation artifact.

If no artifact name is given, the job directly publishes the documentation's HTML content to GitHub Pages.


Secrets
*******

This job template needs no secrets.

Results
*******

This job template has no output parameters.
