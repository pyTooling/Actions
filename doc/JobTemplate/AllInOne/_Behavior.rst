1. Classify ``${{ github.ref }}`` into branch, tag or pull-request and find the pull-request associated with a
   release commit.
2. Extract Python project settings from :file:`pyproject.toml`.
3. Compute the job matrices and the artifact names based on system, Python version, environment, ... for job variants
   (:ref:`JOBTMPL/CompletePipeline/Input/unittest_python_version_list`,
   :ref:`JOBTMPL/CompletePipeline/Input/unittest_system_list`,
   :ref:`JOBTMPL/CompletePipeline/Input/unittest_include_list`,
   :ref:`JOBTMPL/CompletePipeline/Input/unittest_exclude_list`,
   :ref:`JOBTMPL/CompletePipeline/Input/unittest_disable_list`).
4. Verify that the version in the Python code matches the version derived from the tag or pull-request title.
5. Run unit tests using pytest and collect code coverage.
6. Verify type annotations using static typing analysis using mypy.
7. Check documentation coverage using docstr_coverage and interrogate.
8. Check code quality: security scanning using bandit (:ref:`JOBTMPL/CompletePipeline/Input/bandit`), metrics and
   complexity using radon, linting using pylint (:ref:`JOBTMPL/CompletePipeline/Input/pylint`).
9. Package code as source distribution and wheel.
10. Install the wheel on every target platform and verify the installed version.
11. Run application tests against the installed package using pytest
    (:ref:`JOBTMPL/CompletePipeline/Input/apptest`,
    :ref:`JOBTMPL/CompletePipeline/Input/apptest_python_version_list`,
    :ref:`JOBTMPL/CompletePipeline/Input/apptest_system_list`).
12. Merge unit test results and code coverage results and publish them to GitHub
    (:ref:`JOBTMPL/CompletePipeline/Input/dorny`), Codecov (:ref:`JOBTMPL/CompletePipeline/Input/codecov`) and Codacy
    (:ref:`JOBTMPL/CompletePipeline/Input/codacy`).
13. Delete the per-matrix-job artifacts that have been merged (:ref:`JOBTMPL/CompletePipeline/Input/cleanup`).
14. Generate HTML and LaTeX documentations using Sphinx
    (:ref:`JOBTMPL/CompletePipeline/Input/documentation_steps`: ``html``, ``latex``).
15. Translate LaTeX documentation to PDF using MikTeX
    (:ref:`JOBTMPL/CompletePipeline/Input/documentation_steps`: ``pdf``,
    :ref:`JOBTMPL/CompletePipeline/Input/miktex_image`, :ref:`JOBTMPL/CompletePipeline/Input/miktex_update`).
16. Publish documentation to GitHub Pages (:ref:`JOBTMPL/CompletePipeline/Input/documentation_steps`: ``pages``).
17. Tag a release commit, which triggers a second pipeline run for the new tag
    (:ref:`JOBTMPL/CompletePipeline/Input/auto_tag`).
18. Create a GitHub release page with text derived from the pull-request description and upload release assets.
19. Publish wheel to PyPI.
20. Delete the remaining artifacts (:ref:`JOBTMPL/CompletePipeline/Input/cleanup`).

Steps 17 to 19 form the release path: step 17 runs on the release branch and creates the tag, steps 18 and 19 run in
the tag pipeline that this tag triggers.

Steps 8, 11, 13, 14, 15, 16, 17 and 20 can be switched off by the parameters listed with them. A step that is
switched off is *skipped*; every other step is executed as usual. Steps 1 to 7, 9, 10, 12, 18 and 19 are always
executed - step 12 only decides per service whether the results are published.
