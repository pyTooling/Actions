.. _JOBTMPL/CompletePipeline:

CompletePipeline
################

The ``CompletePipeline`` job template is a workaround for the limitations of GitHub Actions to handle global variables in
GitHub Actions workflows (see `actions/runner#480 <https://github.com/actions/runner/issues/480>`__.

It generates output parameters with artifact names and a job matrix to be used in later running jobs.

**Behavior:**

.. todo:: Parameters:Behavior Needs documentation.

**Dependencies:**

*None*

Instantiation
*************

Simple Example
==============

The following instantiation example creates a job `Params` derived from job template `Parameters` version `r0`. It only
requires a `name` parameter to create the artifact names.

.. code-block:: yaml

   name: Pipeline

   on:
     push:
     workflow_dispatch:

   jobs:
     Params:
       uses: pyTooling/Actions/.github/workflows/CompletePipeline.yml@r0
       with:
         name: pyTooling
