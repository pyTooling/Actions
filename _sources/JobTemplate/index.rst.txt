.. _JOBTMPL:

Overview
########

The following list categorizes all pre-defined job templates, which can be instantiated in a pipeline (GitHub Action
Workflow). They can also serve as an example for creating or driving own job templates.

**Table of Contents:**

.. hlist::
   :columns: 2

   * **Global Templates**

     * :ref:`JOBTMPL/Parameters`

   * **Unit Tests, Code Coverage, Code Quality, ...**

     * :ref:`JOBTMPL/UnitTesting`
     * :ref:`JOBTMPL/CodeCoverage`
     * :ref:`JOBTMPL/StaticTypeChecking`
     * *code formatting (planned)*
     * *coding style (planned)*
     * *code linting (planned)*

   * **Build and Packaging**

     * :ref:`JOBTMPL/Package`

   * **Documentation**

     * :ref:`JOBTMPL/VerifyDocumentation`
     * :ref:`JOBTMPL/BuildTheDocs`

   * **Releasing, Publishing**

     * :ref:`JOBTMPL/GitHubReleasePage`
     * :ref:`JOBTMPL/PyPI`
     * :ref:`JOBTMPL/PublishTestResults`
     * :ref:`JOBTMPL/PublishToGitHubPages`

   * **Cleanups**

     * :ref:`JOBTMPL/ArtifactCleanup`


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
