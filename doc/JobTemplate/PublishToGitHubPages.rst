.. _JOBTMPL/PublishToGitHubPages:

PublishToGitHubPages
####################

This job publishes HTML content from artifacts of other jobs to GitHub Pages.

**Behavior:**

1. Checkout repository.
2. Download artifacts.
3. Push HTML files to branch ``gh-pages``.

**Dependencies:**

* :gh:`actions/checkout`
* :gh:`actions/download-artifact`

Instantiation
*************

Simple Example
==============

.. code-block:: yaml

   jobs:
     BuildTheDocs:
       # ...

     PublishToGitHubPages:
       uses: pyTooling/Actions/.github/workflows/PublishToGitHubPages.yml@r0
       needs:
         - BuildTheDocs
       with:
         doc: Documentation


Complex Example
===============

.. code-block:: yaml

   jobs:
     PublishToGitHubPages:
       uses: pyTooling/Actions/.github/workflows/PublishToGitHubPages.yml@r0
       needs:
         - Params
         - BuildTheDocs
         - Coverage
         - StaticTypeCheck
       with:
         doc: ${{ fromJson(needs.Params.outputs.artifact_names).documentation_html }}
         coverage: ${{ fromJson(needs.Params.outputs.artifact_names).codecoverage_html }}
         typing: ${{ fromJson(needs.Params.outputs.artifact_names).statictyping_html }}


Parameters
**********

doc
===

+----------------+----------+----------+--------------+
| Parameter Name | Required | Type     | Default      |
+================+==========+==========+==============+
| doc            | yes      | string   | — — — —      |
+----------------+----------+----------+--------------+

Name of the documentation artifact.


coverage
========

+----------------+----------+----------+-----------------+
| Parameter Name | Required | Type     | Default         |
+================+==========+==========+=================+
| coverage       | optional | string   | ``""``          |
+----------------+----------+----------+-----------------+

Name of the coverage artifact.


typing
======

+----------------+----------+----------+-----------------+
| Parameter Name | Required | Type     | Default         |
+================+==========+==========+=================+
| typing         | optional | string   | ``""``          |
+----------------+----------+----------+-----------------+

Name of the typing artifact.



Secrets
*******

This job template needs no secrets.

Results
*******

This job template has no output parameters.
