.. _JOBTMPL/Cleanup:

Cleanup
#######

The category *cleanup* provides workflow templates implementing artifact cleanups (removals) from pipelines.

Running lots of unit testing, platform testing and application testing variants (operating system |times| Python version
|times| environment) creates dozens to hundrets of artifacts (unit test report, code coverage report, ...). This
consumes pipeline storage which can be freed up. Moreover, it's unclear which artifacts contain the final unit test and
code coverage reports. Thus, it's benefitial, to remove intermediate artifacts after merging reports into one summary
report.

.. topic:: Artifact Cleanups

   * :ref:`JOBTMPL/CleanupArtifacts` - remove artifacts by key into an artifact-name dictionary, in the middle of a
     pipeline as well as at its end.


.. topic:: Deprecated

   * :ref:`JOBTMPL/IntermediateCleanUp` - replaced by :ref:`JOBTMPL/CleanupArtifacts`.
   * :ref:`JOBTMPL/ArtifactCleanup` - replaced by :ref:`JOBTMPL/CleanupArtifacts`.


.. toctree::
   :hidden:

   IntermediateCleanup
   CleanupArtifacts
   ArtifactCleanup
