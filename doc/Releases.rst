Releases Management
###################

Releases
********

r1
==

.. note:: Upcoming next release based in `v1.x.y`.

.. attention:: This release introduces breaking changes.

r0
==

.. todo:: Releases:r0 Needs documentation.

Versions
********

.. todo:: Releases:Versions Needs documentation.

Branches
********

.. mermaid::

   %%{init: { 'logLevel': 'debug', 'theme': 'neutral', 'gitGraph': {'rotateCommitLabel': false} } }%%
   gitGraph
     commit id: "-"
     branch dev
     commit id: "B"
     commit id: "C"
     checkout main
     merge dev tag: "v0.4.0"
     checkout dev
     commit id: "D"
     commit id: "E"
     commit id: "F"
     checkout main
     merge dev tag: "v0.5.0"

``dev``
=======

Development is done on branch ``dev``.

All merge requests need to target this branch.

``main``
========

Finished development is merged to branch ``main``.

Each merge-commit is tagged with a semantic version.


Tagging
*******

See context in :ghissue:`#5 Tagging/versioning of this repo <5>`.

Tagging is done by this repository's pipeline (see :ref:`DEV/Pipeline`): when a release pull-request is merged into
``main``, its title provides the version, and the merge commit is tagged once every verification workflow succeeded.
The tag's pipeline run then publishes the release page and opens a pull-request moving the release branch, e.g.
``Updating r8 from v8.1.0``.

If the pipeline couldn't tag - a failing verification workflow, for example - the same is done by hand. Tag new
releases in the ``main`` branch using a semver compatible value, starting with ``v``:

.. code-block:: bash

   git checkout main
   git tag v0.0.0
   git push upstream v0.0.0

Move the corresponding release branch (starting with ``r``) forward by creating a merge commit, and using the merged tag
as the commit message:

.. code-block:: bash

   git checkout r0
   git merge --no-ff -m 'v0.0.0' v0.0.0
   git push upstream r0
