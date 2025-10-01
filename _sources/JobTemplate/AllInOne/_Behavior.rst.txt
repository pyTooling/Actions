1. Infer information from ``${{ github.ref }}`` variable.
2. Extract Python project settings from :file:`pyproject.toml`.
3. Compute job matrix based on system, Python version, environment, ... for job variants.
4. Run unit tests using pytest and collect code coverage.
5. Run platform tests using pytest and collect code coverage.
6. Run application tests using pytest.
7. Package code as wheel.
8. Check documentation coverage using docstr_coverage and interrogate.
9. Verify type annotation using static typing analysis using mypy.
10. Merge unit test results and code coverage results.
11. Generate HTML and LaTeX documentations using Sphinx.
12. Translate LaTeX documentation to PDF using MikTeX.
13. Publish unit test and code coverage results to cloud services.
14. Publish documentation to GitHub Pages.
15. Publish wheel to PyPI.
16. Create a GitHub release page and upload release assets.
