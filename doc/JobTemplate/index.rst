.. _JOBTMPL:

Overview
########

The following list categorizes all pre-defined job templates, which can be instantiated in a pipeline (GitHub Action
Workflow). They can also serve as an example for creating or deriving own job templates.

.. grid:: 5

   .. grid-item::
      :columns: 2

      .. rubric:: All-In-One Templates

      * :ref:`JOBTMPL/CompletePipeline`

      .. rubric:: Global Templates

      * :ref:`JOBTMPL/Parameters`
      * :ref:`JOBTMPL/PrepareJob`
      * :ref:`JOBTMPL/ExtractConfiguration`

   .. grid-item::
      :columns: 2

      .. rubric:: Documentation

      * :ref:`JOBTMPL/CheckDocumentation`
      * :ref:`JOBTMPL/VerifyDocs`
      * :ref:`JOBTMPL/SphinxDocumentation`
      * :ref:`JOBTMPL/LaTeXDocumentation`

      .. rubric:: Unit Tests, Code Coverage

      * :ref:`JOBTMPL/ApplicationTesting`
      * :ref:`JOBTMPL/UnitTesting`

   .. grid-item::
      :columns: 2

      .. rubric:: Code Quality

      * :ref:`JOBTMPL/StaticTypeChecking`
      * *code formatting (planned)*
      * *coding style (planned)*
      * *code linting (planned)*

      .. rubric:: Build and Packaging

      * :ref:`JOBTMPL/Package`
      * :ref:`JOBTMPL/InstallPackage`

   .. grid-item::
      :columns: 2

      .. rubric:: Publishing

      * :ref:`JOBTMPL/PublishOnPyPI`
      * :ref:`JOBTMPL/PublishTestResults`
      * :ref:`JOBTMPL/PublishCoverageResults`
      * :ref:`JOBTMPL/PublishToGitHubPages`

      .. rubric:: Releasing

      * :ref:`JOBTMPL/PublishReleaseNotes`
      * :ref:`JOBTMPL/TagReleaseCommit`

   .. grid-item::
      :columns: 2

      .. rubric:: Cleanup Templates

      * :ref:`JOBTMPL/IntermediateCleanup`
      * :ref:`JOBTMPL/ArtifactCleanup`

   .. grid-item::
      :columns: 2

      .. rubric:: :ref:`JOBTMPL/Deprecated`

      * :ref:`JOBTMPL/CodeCoverage`
      * :ref:`JOBTMPL/NightlyRelease`
      * :ref:`JOBTMPL/BuildTheDocs`


Instantiation
*************

When instantiating a template, a ``jobs:<Name>:uses`` is used to refer to a template file. Unfortunately, besides the
GitHub SLUG (*<Organization>/<Repository>*), also the full path to the template needs to be gives, but still it can't be
outside of ``.github/workflows`` to create a cleaner repository structure. Finally, the path contains a branch name
postfixed by ``@<branch>`` (tags are still not supported by GitHub Actions). A ``jobs:<Name>:with:`` section can be used
to handover input parameters to the template.

.. code-block:: yaml

   on:
     push:
     workflow_dispatch:

   jobs:
     <InstanceName>:
       uses: <GitHubOrganization>/<Repository>/.github/workflows/<Template>.yml@v0
       with:
         <Param1>: <Value>
