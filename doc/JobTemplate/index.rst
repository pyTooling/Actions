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

The job templates (GitHub Action *Reusable Workflows*) need to be stored in the same directory where normal pipelines
(GitHub Action *Workflows*) are located: ``.github/workflows/<template>.yml``. These template files are distinguished
from a normal pipeline by a ``on:workflow_call:`` section compared to an ``on:push`` section.

**Job Template Definition:**

The ``workflow_call`` allows the definition of input and output parameters.

.. code-block:: yaml

   on:
     workflow_call:
       inputs:
         <Param1>:
           # ...
       outputs:
         # ...

   jobs:
     <JobName>:
       # ...

**Job Template Instantiation:**

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


Development
***********

.. todo:: JobTemplate:Development Needs documentation
