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
         doc: ${{ fromJson(needs.Params.outputs.params).artifacts.doc }}
         coverage: ${{ fromJson(needs.Params.outputs.params).artifacts.coverage }}
         typing: ${{ fromJson(needs.Params.outputs.params).artifacts.typing }}

Parameters
**********

doc
===

Name of the documentation artifact.

+----------+----------+--------------+
| Required | Type     | Default      |
+==========+==========+==============+
| yes      | string   | — — — —      |
+----------+----------+--------------+

coverage
========

Name of the coverage artifact.

+----------+----------+-----------------+
| Required | Type     | Default         |
+==========+==========+=================+
| optional | string   | ``""``          |
+----------+----------+-----------------+


typing
======

Name of the typing artifact.

+----------+----------+-----------------+
| Required | Type     | Default         |
+==========+==========+=================+
| optional | string   | ``""``          |
+----------+----------+-----------------+


Secrets
*******

This job template needs no secrets.

Results
*******

This job template has no output parameters.
