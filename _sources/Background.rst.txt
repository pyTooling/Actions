Background
##########

GitHub Actions supports five procedures to reuse code:

- JavaScript Action:

  - `docs.github.com: actions/creating-actions/creating-a-javascript-action <https://docs.github.com/en/actions/creating-actions/creating-a-javascript-action>`__

- Container Action:

  - `docs.github.com: actions/creating-actions/creating-a-docker-container-action <https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action>`__

- Container Step:

  - `docs.github.com: actions/learn-github-actions/workflow-syntax-for-github-actions#example-using-a-docker-public-registry-action <https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions#example-using-a-docker-public-registry-action>`__
  - `docs.github.com: actions/learn-github-actions/workflow-syntax-for-github-actions#jobsjob_idstepswithargs <https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions#jobsjob_idstepswithargs>`__

- Composite Action:

  - `docs.github.com: actions/creating-actions/creating-a-composite-action <https://docs.github.com/en/actions/creating-actions/creating-a-composite-action>`__
  - `github.blog/changelog: 2020-08-07-github-actions-composite-run-steps <https://github.blog/changelog/2020-08-07-github-actions-composite-run-steps/>`__
  - `github.blog/changelog: 2021-08-25-github-actions-reduce-duplication-with-action-composition <https://github.blog/changelog/2021-08-25-github-actions-reduce-duplication-with-action-composition/>`__

- Reusable Workflow:

  - `docs.github.com: actions/learn-github-actions/reusing-workflows <https://docs.github.com/en/actions/learn-github-actions/reusing-workflows>`__
  - `github.blog/changelog: 2021-10-05-github-actions-dry-your-github-actions-configuration-by-reusing-workflows <https://github.blog/changelog/2021-10-05-github-actions-dry-your-github-actions-configuration-by-reusing-workflows/>`__

Container Actions and Container Steps are almost equivalent: Actions use a configuration file (``action.yml``), while
Steps do not.
Leaving JavaScript and Container Actions and Steps aside, the main differences between Composite Actions and Reusable
Workflows are the following:

- Composite Actions can be executed from a remote/external path or from the checked out branch, and from any location.
  However, Reusable Workflows can only be used through a remote/external path (``{owner}/{repo}/{path}/{filename}@{ref}``),
  where ``{path}`` must be ``.github/workflows``, and ``@{ref}`` is required.
  See `actions/runner#1493 <https://github.com/actions/runner/issues/1493>`__.
  As a result:

  - Local Composite Actions cannot be used without a prior repo checkout, but Reusable Workflows can be used without
    checkout.
  - Testing development versions of local Reusable Workflows is cumbersome, because PRs do not pick the modifications by
    default.

- Composite Actions can include multiple steps, but not multiple jobs.
  Conversely, Reusable Workflows can include multiple jobs, and multiple steps in each job.
- Composite Actions can include multiple files, so it's possible to use files from the Action or from the user's repository.
  Conversely, Reusable Workflows are a single YAML file, with no additional files retrieved by default.

Callable vs dispatchable workflows
**********************************

Reusable Workflows are defined through the ``workflow_call`` event kind.
Similarly, any "regular" Workflow can be triggered through a ``workflow_dispatch`` event.
Both event kinds support ``input`` options, which are usable within the Workflow.
Therefore, one might intuitively try to write a workflow which is both callable and dispatchable.
In other words, which can be either reused from another workflow, or triggered through the API.
Unfortunately, that is not the case.
Although ``input`` options can be duplicated for both events, GitHub's backend exposes them through different objects.
In dispatchable Workflows, the object is ``${{ github.event.inputs }}``, while callable workflows receive ``${{ inputs }}``.

As a result, in order to make a reusable workflow dispatchable, a wrapper workflow is required.
See, for instance, `hdl/containers: .github/workflows/common.yml <https://github.com/hdl/containers/blob/main/.github/workflows/common.yml>`__
and `hdl/containers: .github/workflows/dispatch.yml <https://github.com/hdl/containers/blob/main/.github/workflows/dispatch.yml>`__.
Alternatively, a normalisation job might be used, similar to the ``Parameters`` in this repo.

Call hierarchy
**************

Reusable Workflows cannot call other Reusable Workflows, however, they can use Composite Actions and Composite Actions
can call other Actions.
Therefore, in some use cases it is sensible to combine one layer of reusable workflows for orchestrating the jobs, along
with multiple layers of composite actions.

Script with post step
*********************

JavaScript Actions support defining ``pre``, ``pre-if``, ``post`` and ``post-if`` steps, which allow executing steps at
the beginning or the end of a job, regardless of intermediate steps failing.
Unfortunately, those are not available for any other Action type.

Action [with-post-step](with-post-step) is a generic JS Action to execute a main command and to set a command as a post
step.
It allows using the ``post`` feature with scripts written in bash, python or any other interpreted language available on
the environment.
See: `actions/runner#1478 <https://github.com/actions/runner/issues/1478>`__.
