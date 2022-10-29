.. include:: shields.inc

.. raw:: latex

   \part{Introduction}

.. only:: html

   |  |SHIELD:svg:pyTooling-github| |SHIELD:svg:pyTooling-src-license| |SHIELD:svg:pyTooling-ghp-doc| |SHIELD:svg:pyTooling-doc-license|
   |  |SHIELD:svg:pyTooling-tag| |SHIELD:svg:pyTooling-date|

.. Disabled shields: |SHIELD:svg:pyTooling-gitter|

.. only:: latex

   |SHIELD:png:pyTooling-github| |SHIELD:png:pyTooling-src-license| |SHIELD:png:pyTooling-ghp-doc| |SHIELD:png:pyTooling-doc-license|
   |SHIELD:png:pyTooling-tag| |SHIELD:png:pyTooling-date|

.. Disabled shields: |SHIELD:svg:pyTooling-gitter|

--------------------------------------------------------------------------------

pyTooling Actions Documentation
###############################

**pyTooling Actions** are reusable steps and workflows for GitHub Actions easing the creation and maintenance of
workflows for Python projects on GitHub.

GitHub Actions workflows, actions and documentation are mostly focused on JavaScript/TypeScript as the scripting
language for writing reusable CI code.
However, Python being equally popular and capable, usage of JS/TS might be bypassed, with some caveats.
This repository gathers reusable CI tooling for testing, packaging and distributing Python projects and documentation.

Introduction
************



Package Details
***************


Contributors
************

* `Patrick Lehmann <https://GitHub.com/Paebbels>`__
* `Unai Martinez-Corral <https://GitHub.com/umarcor>`__ (Maintainer)
* `and more... <https://GitHub.com/pyTooling/Actions/graphs/contributors>`__


License
*******

.. only:: html

   This Python package (source code) is licensed under `Apache License 2.0 <Code-License.html>`__. |br|
   The accompanying documentation is licensed under `Creative Commons - Attribution 4.0 (CC-BY 4.0) <Doc-License.html>`__.

.. only:: latex

   This Python package (source code) is licensed under **Apache License 2.0**. |br|
   The accompanying documentation is licensed under **Creative Commons - Attribution 4.0 (CC-BY 4.0)**.


------------------------------------

.. |docdate| date:: %b %d, %Y - %H:%M

.. only:: html

   This document was generated on |docdate|.

.. toctree::
   :caption: Overview
   :hidden:

   Introduction
   Dependency

.. raw:: latex

   \part{Main Documentation}

.. toctree::
   :caption: Job Templates
   :hidden:

   JobTemplate/index
   JobTemplate/Parameters
   JobTemplate/CoverageCollection
   JobTemplate/UnitTesting
   JobTemplate/StaticTypeCheck
   JobTemplate/PublishTestResults
   JobTemplate/Package
   JobTemplate/PublishOnPyPI
   JobTemplate/VerifyDocs
   JobTemplate/BuildTheDocs
   JobTemplate/PublishToGitHubPages
   JobTemplate/Release
   JobTemplate/ArtifactCleanUp

.. toctree::
   :caption: Actions
   :hidden:

   Action/index
   Action/Releaser

.. raw:: latex

   \part{Appendix}

.. toctree::
   :caption: Appendix
   :hidden:

   License
   Doc-License
   genindex
   TODO
