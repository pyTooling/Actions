.. _JOBTMPL/AllInOne:

All-In-One
##########

The category *all-in-one* provides workflow templates implementing all necessary steps (jobs) for testing and publishing
a Python project. It utilizes allmost all of ``pyTooling/Acion``'s workflow templates.

Such a all-in-one workflow template covers:

* unit testing
* code coverage collections
* documentation checking
* pulishing of unit test and code coverage results
* merging of test reports
* packaging as wheel
* publishing wheels tp PyPI
* documentation generation via Sphinx and Miktex
* automatic tagging of release commits
* releasing

.. topic:: Provides *all-in-one* workflow templates

   * :ref:`JOBTMPL/CompletePipeline` - Use all of ``pyTooling/Acion``'s workflow templates by instantiation of a single
     workflow template.

.. image:: ../../_static/pyTooling-Actions-SimplePackage.png

.. toctree::
   :hidden:

   CompletePipeline
