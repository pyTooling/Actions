.. _JOBTMPL/Setup:

Pipeline Setup
##############

The category *pipeline setup* provides workflow templates implementing preparation steps suitable for every pipeline.

* :ref:`JOBTMPL/Parameters` - Compute a matrix of (operating system |times| Python version |times| environment)
  combinations for unit testing, platform testing or application testing and provide the result as a JSON string via
  pipeline outputs.
* :ref:`JOBTMPL/PrepareJob` - Check GitHub Action environment variables and commits to provide precomputed variables as
  pipeline outputs.
* :ref:`JOBTMPL/ExtractConfiguration` - Extract configuration settings from :file:`pyproject.toml` and provide settings
  as pipeline outputs.

.. toctree::
   :hidden:

   PrepareJob
   Parameters
   ExtractConfiguration
