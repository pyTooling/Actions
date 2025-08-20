.. _JOBTMPL:

Overview
########

The following list categorizes all pre-defined job templates, which can be instantiated in a pipeline (GitHub Action
Workflow). They can also serve as an example for creating or deriving own job templates.

.. include:: Templates.rst


.. _JOBTMPL/Instantiation:

Instantiation
*************

When instantiating a template, a ``jobs:<Name>:uses`` is used to refer to a template file. Unfortunately, besides the
GitHub SLUG (*<Organization>/<Repository>*), also the full path to the template needs to be gives. Unfortunately, it
can't be outside of the ``.github/workflows`` directory creating a cleaner repository structure. Finally, the path
contains a branch name postfixed by ``@<branch>`` (tags are still not supported by GitHub Actions). Repositories usually
offer a ``@v2``/``@r2`` syntax for refering to the second version/revision.

Allmost all templates are generic and offer lots of configuration options. For handing over input parameters, a
``jobs:<Name>:with:`` node with a dictionary can be used. Additionally, some templates might require secrets, which
are passed from GitHub's ``secrets`` context to the template by using a ``jobs:<Name>:secrets:`` node.

Some templates might provide output parameters, which can be used in dependent jobs by setting a job dependency using
``jobs:<Name>:needs:``. The output parameter can be retrieved by accessing the ``needs`` context.

.. code-block:: yaml

   on:
     push:
     workflow_dispatch:
     schedule:
   # Every Friday at 22:00 - rerun pipeline to check for dependency-based issues
       - cron: '0 22 * * 5'

   jobs:
     <InstanceName>:
       uses: <GitHubOrganization>/<Repository>/.github/workflows/<Template>.yml@r5
       with:
         <Param1>: <Value1>
         <Param2>: <Value2>
       secrets:
         <Secret1>: ${{ secrets.<SecretVariable1> }}
         <Secret2>: ${{ secrets.<SecretVariable2> }}

     <OtherInstance>:
       ...
       needs:
         - <InstanceName>
       ...
       with:
         <Param1>: ${{ needs.<InstanceName>.outputs.<Output1> }}
