.. _ACTION/WithPostStep:

with-post-step
##############

JavaScript Actions support defining ``pre``, ``pre-if``, ``post`` and ``post-if`` steps, which allow executing steps at
the beginning or the end of a job, regardless of intermediate steps failing. Unfortunately, those are not available for
any other Action type.

Action **with-post-step** is a generic JavaScript Action to execute a main command and to set a further command as a
post step. It allows using the ``post`` feature with scripts written in Bash, Python or any other interpreted language
available on the environment.

**Example Usage:**

.. code-block:: yaml

   jobs:
     Image:
       steps:
         - ...

         - name: Push container image
           uses: ./with-post-step
           with:
             main: |
               echo '${{ github.token }}' | docker login ghcr.io -u GitHub-Actions --password-stdin
               docker push ghcr.io/pytooling/releaser
             post: docker logout ghcr.io

.. seealso::

   * `actions/runner#1478 <https://github.com/actions/runner/issues/1478>`__.
