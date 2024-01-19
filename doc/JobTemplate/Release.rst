.. _JOBTMPL/GitHubReleasePage:

Release
#######

This job creates a Release Page on GitHub.

**Release Template in Markdown**:

.. parsed-literal::

   **Automated Release created on: ${{ steps.getVariables.outputs.datetime }}**

   # New Features
   * tbd

   # Changes
   * tbd

   # Bug Fixes
   * tbd

**Behavior:**

1. Extract information from environment variables provided by GitHub Actions.
2. Create a Release Page on GitHub

**Dependencies:**

* :gh:`actions/create-release` (unmaintained)

Instantiation
*************

Simple Example
==============

.. code-block:: yaml

   jobs:
     Release:
       uses: pyTooling/Actions/.github/workflows/Release.yml@r0


Complex Example
===============

.. code-block:: yaml

   jobs:
     Release:
       uses: pyTooling/Actions/.github/workflows/Release.yml@r0
       if: startsWith(github.ref, 'refs/tags')
       needs:
         - Package


Parameters
**********

This job template needs no input parameters.


Secrets
*******

This job template needs no secrets.


Results
*******

This job template has no output parameters.
