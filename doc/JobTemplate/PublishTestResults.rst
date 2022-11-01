.. _JOBTMPL/PublishTestResults:

PublishTestResults
##################

This job downloads all artifacts and uploads jUnit XML reports as a Markdown page to GitHub Actions to visualize the
results a an item in the job list. For publishing, :gh:`dorny/test-reporter` is used.

**Behavior:**

1. Checkout repository
2. Download (all) artifacts
3. Publish test results as a markdown report page to GitHub Actions.

.. note::

   The :gh:`actions/download-artifact` does not support wildcards to specify a subset of artifacts for downloading.
   Thus, all artifacts need to be downloaded.

**Dependencies:**

* :gh:`actions/checkout`
* :gh:`actions/download-artifact`
* :gh:`dorny/test-reporter`


Instantiation
*************

Simple Example
==============

.. code-block:: yaml

   jobs:
     PublishTestResults:
       uses: pyTooling/Actions/.github/workflows/PublishTestResults.yml@r0

Complex Example
===============

.. code-block:: yaml

   jobs:
     CodeCoverage:
       # ...

     UnitTesting:
       # ...

     PublishTestResults:
       uses: pyTooling/Actions/.github/workflows/PublishTestResults.yml@r0
       needs:
         - CodeCoverage
         - UnitTesting

Template Parameters
*******************

report_files
============

Pattern of jUnit report files to publish as Markdown.

The parameter can be a comma separated list. Wildcards are supported.

.. hint::

   All artifacts are downloaded into directory ``artifacts``, thus the pattern should include this directory as a
   prefix.

+----------+----------+---------------------------------+
| Required | Type     | Default                         |
+==========+==========+=================================+
| optional | string   | ``artifacts/**/*.xml``          |
+----------+----------+---------------------------------+


Secrets
*******

This job template needs no secrets.

Results
*******

This job template has no output parameters.
