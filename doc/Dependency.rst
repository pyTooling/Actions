Dependencies
############

This is a summary of dependencies used by the provided job templates. For more details, see each job template.

* Actions provided by GitHub

  * :gh:`actions/checkout`
  * :gh:`actions/setup-python`
  * :gh:`actions/github-script` - used by :ref:`JOBTMPL/TagReleaseCommit` to dispatch the tag pipeline.
  * :gh:`actions/upload-pages-artifact` - used by :ref:`JOBTMPL/PublishToGitHubPages`.
  * :gh:`actions/deploy-pages` - used by :ref:`JOBTMPL/PublishToGitHubPages`.

* Actions provided by pyTooling

  * :gh:`pyTooling/upload-artifact` - wraps :gh:`actions/upload-artifact` and packs the uploaded files into a
    tarball, so file modes and symbolic links survive the round trip.
  * :gh:`pyTooling/download-artifact` - wraps :gh:`actions/download-artifact` and unpacks that tarball again.

* Code Quality Services

  * :gh:`codecov/codecov-action`
  * :gh:`codacy/codacy-coverage-reporter-action`

* Reporting

  * :gh:`dorny/test-reporter`

* Miscellaneous

  * :gh:`msys2/setup-msys2`
  * :gh:`geekyeggo/delete-artifact`
  * :gh:`GitHub command line tool 'gh' <cli/cli>` - preinstalled on GitHub runners; used by
    :ref:`JOBTMPL/PrepareJob` and :ref:`JOBTMPL/PublishReleaseNotes`.
  * :dockerhub:`pytooling/miktex <pytooling/miktex:sphinx>` - the container :ref:`JOBTMPL/LaTeXDocumentation` runs in.

Python packages installed through *pip* - :pypi:`bandit`, :pypi:`build`, :pypi:`coverage`,
:pypi:`docstr_coverage`, :pypi:`interrogate`, :pypi:`mypy`, :pypi:`pyEDAA.Reports`, :pypi:`pylint`, :pypi:`radon`,
:pypi:`Sphinx`, :pypi:`twine`, :pypi:`wheel` - are listed with the job template that installs them.
