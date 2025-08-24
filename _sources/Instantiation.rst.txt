Instantiantion
##############

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


Example Pipelines
*****************

Documentation Only (Sphinx)
===========================

.. code-block:: yaml

   name: Pipeline

   on:
     push:
     workflow_dispatch:

   jobs:
     BuildTheDocs:
       uses: pyTooling/Actions/.github/workflows/BuildTheDocs.yml@r5
       with:
         artifact: Documentation

     PublishToGitHubPages:
       uses: pyTooling/Actions/.github/workflows/PublishToGitHubPages.yml@r5
       needs:
         - BuildTheDocs
       with:
         doc: Documentation

     ArtifactCleanUp:
       name: 🗑️ Artifact Cleanup
       needs:
         - BuildTheDocs
         - PublishToGitHubPages
       runs-on: ubuntu-24.04

       steps:
         - name: 🗑️ Delete artifacts
           uses: geekyeggo/delete-artifact@v5
           with:
             name: Documentation


Simple Package
==============


Package with Unit Tests
=======================


Package with Code Coverage
==========================

Complex Pipeline
================


Further Reference Examples
**************************

Find further usage cases in the following list of projects:

- `edaa-org/pyEDAA.ProjectModel <https://github.com/edaa-org/pyEDAA.ProjectModel/tree/main/.github/workflows>`__
- `edaa-org/pySVModel <https://github.com/edaa-org/pySVModel/tree/main/.github/workflows>`__
- `VHDL/pyVHDLModel <https://github.com/VHDL/pyVHDLModel/tree/main/.github/workflows>`__
