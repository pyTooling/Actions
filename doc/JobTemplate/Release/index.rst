.. _JOBTMPL/Release:

Release
#######

The category *release* provides workflow templates implementing

* :ref:`JOBTMPL/CheckReleaseVersion` - Check that a version isn't released yet in a package registry.
* :ref:`JOBTMPL/TagReleaseCommit` - Automatically tag current commit in Git using the associate pull-requests title.
* :ref:`JOBTMPL/PublishReleaseNotes` - Create GitHub release page and upload release assets.
* :ref:`JOBTMPL/UpdateVersionBranch` - Propose the update of a major-version branch as a pull-request.

.. toctree::
   :hidden:

   CheckReleaseVersion
   TagReleaseCommit
   PublishReleaseNotes
   UpdateVersionBranch
