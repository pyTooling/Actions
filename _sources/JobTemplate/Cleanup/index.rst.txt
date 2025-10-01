.. _JOBTMPL/Cleanup:

Cleanup
#######

The category *cleanup* provides workflow templates implementing artifact cleanups (removals) from pipelines.

Running lots of unit testing, platform testing and application testing variants (operating system |times| Python version
|times| environment) creates dozens to hundrets of artifacts (unit test report, code coverage report, ...). This
consumes pipeline storage which can be freed up. Moreover, it's unclear which artifacts contain the final unit test and
code coverage reports. Thus, it's benefitial, to remove intermediate artifacts after merging reports into one summary
report.

.. topic:: Intermediate cleanups

   * :ref:`JOBTMPL/IntermediateCleanup` - remove intermediate artifacts after merging reports into one summary report.


.. topic:: Final cleanups

   * :ref:`JOBTMPL/ArtifactCleanup` - remove artifacts after publising results and creating release assets.


.. toctree::
   :hidden:

   IntermediateCleanup
   ArtifactCleanup
