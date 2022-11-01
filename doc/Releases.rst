Releases Management
###################

Releases
********

r0
==

.. todo:: Releases:r0 Needs documentation.

Versions
********

.. todo:: Releases:Versions Needs documentation.

Branches
********

.. todo:: Releases:Branches Needs documentation.

Tagging
*******

See context in `#5 <https://github.com/pyTooling/Actions/issues/5>`__.

Tag new releases in the ``main`` branch using a semver compatible value, starting with ``v``:

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
