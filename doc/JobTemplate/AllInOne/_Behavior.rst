1. Classify ``${{ github.ref }}`` into branch, tag or pull-request and find the pull-request associated with a
   release commit.
2. Extract Python project settings from :file:`pyproject.toml`.
3. Compute the job matrices and the artifact names based on system, Python version, environment, ... for job variants.
4. Verify that the version in the Python code matches the version derived from the tag or pull-request title.
5. Run unit tests using pytest and collect code coverage.
6. Verify type annotations using static typing analysis using mypy.
7. Check documentation coverage using docstr_coverage and interrogate.
8. Check code quality: security scanning using bandit, metrics and complexity using radon, linting using pylint.
9. Package code as source distribution and wheel.
10. Install the wheel on every target platform and verify the installed version.
11. Run application tests against the installed package using pytest.
12. Merge unit test results and code coverage results and publish them to GitHub, Codecov and Codacy.
13. Delete the per-matrix-job artifacts that have been merged.
14. Generate HTML and LaTeX documentations using Sphinx.
15. Translate LaTeX documentation to PDF using MikTeX.
16. Publish documentation to GitHub Pages.
17. Tag a release commit, which triggers a second pipeline run for the new tag.
18. Create a GitHub release page with text derived from the pull-request description and upload release assets.
19. Publish wheel to PyPI.
20. Delete the remaining artifacts.

Steps 17 to 19 form the release path: step 17 runs on the release branch and creates the tag, steps 18 and 19 run in
the tag pipeline that this tag triggers.
