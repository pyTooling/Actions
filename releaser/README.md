# Releaser

**Releaser** is a Docker GitHub Action written in Python.

**Releaser** allows to keep a GitHub Release of type pre-release and its artifacts up to date with latest builds.
Combined with a workflow that is executed periodically, **Releaser** allows to provide a fixed release name for users willing
to use daily/nightly artifacts of a project.

Furthermore, when any [semver](https://semver.org) compilant tagged commit is pushed, **Releaser** can create a release
and upload assets.

## Context

GitHub provides official clients for the GitHub API through [github.com/octokit](https://github.com/octokit):

- [octokit.js](https://github.com/octokit/octokit.js) ([octokit.github.io/rest.js](https://octokit.github.io/rest.js))
- [octokit.rb](https://github.com/octokit/octokit.rb) ([octokit.github.io/octokit.rb](http://octokit.github.io/octokit.rb))
- [octokit.net](https://github.com/octokit/octokit.net) ([octokitnet.rtfd.io](https://octokitnet.rtfd.io))

When GitHub Actions was released in 2019, two Actions were made available through
[github.com/actions](https://github.com/actions) for dealing with GitHub Releases:

- [actions/create-release](https://github.com/actions/create-release)
- [actions/upload-release-asset](https://github.com/actions/upload-release-asset)

However, those Actions were contributed by an employee in spare time, not officially supported by GitHub.
Therefore, they were unmaintained before GitHub Actions was out of the private beta
(see [actions/upload-release-asset#58](https://github.com/actions/upload-release-asset/issues/58))
and, a year later, archived.
Those Actions are based on [actions/toolkit](https://github.com/actions/toolkit)'s hydrated version of octokit.js.

From a practical point of view, [actions/github-script](https://github.com/actions/github-script) is the natural replacement to those Actions, since it allows to use a pre-authenticated *octokit.js* client along with the workflow run context.
Still, it requires writing plain JavaScript.

Alternatively, there are non-official GitHub API libraries available in other languages (see [docs.github.com: rest/overview/libraries](https://docs.github.com/en/rest/overview/libraries)).
**Releaser** is based on [PyGithub/PyGithub](https://github.com/PyGithub/PyGithub), a Python client for the GitHub API.

**Releaser** was originally created in [eine/tip](https://github.com/eine/tip), as an enhanced alternative to using
`actions/create-release` and `actions/upload-release-asset`, in order to cover certain use cases that were being
migrated from Travis CI to GitHub Actions.
The main limitation of GitHub's Actions was/is verbosity and not being possible to dynamically define the list of assets
to be uploaded.

On the other hand, GitHub Actions artifacts do require login in order to download them.
Conversely, assets of GitHub Releases can be downloaded without login.
Therefore, in order to make CI results available to the widest audience, some projects prefer having tarballs available
as assets.
In this context, one of the main use cases of **Releaser** is pushing artifacts as release assets.
Thus, the name of the Action.

GitHub provides an official CLI tool, written in golang: [cli/cli](https://github.com/cli/cli).
When the Python version of **Releaser** was written, `cli` was evaluated as an alternative to *PyGitHub*.
`gh release` was (and still is) not flexible enough to update the reference of a release, without deleting and
recreating it (see [cli.github.com: manual/gh_release_create](https://cli.github.com/manual/gh_release_create)).
Deletion and recreation is unfortunate, because it notifies all the watchers of a repository
(see [eine/tip#111](https://github.com/eine/tip/issues/111)).
However, [cli.github.com: manual/gh_release_upload](https://cli.github.com/manual/gh_release_upload) handles uploading
artifacts as assets faster and with better stability for larger files than *PyGitHub*
(see [msys2/msys2-installer#36](https://github.com/msys2/msys2-installer/pull/36)).
Furthermore, the GitHub CLI is installed on GitHub Actions' default virtual environments.
Although `gh` does not support login through SSH (see [cli/cli#3715](https://github.com/cli/cli/issues/3715)), on GitHub
Actions a token is available `${{ github.token }}`.
Therefore, **Releaser** uses `gh release upload` internally.

## Usage

The following block shows a minimal YAML workflow file:

```yml
name: 'workflow'

on:
  schedule:
    - cron: '0 0 * * 5'

jobs:
  mwe:
    runs-on: ubuntu-latest
    steps:

    # Clone repository
    - uses: actions/checkout@v4

    # Build your application, tool, artifacts, etc.
    - name: Build
      run: |
        echo "Build some tool and generate some artifacts" > artifact.txt

    # Update tag and pre-release
    # - Update (force-push) tag to the commit that is used in the workflow.
    # - Upload artifacts defined by the user.
    - uses: pyTooling/Actions/releaser@r0
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
        files: |
          artifact.txt
          README.md
```

### Composite Action

The default implementation of **Releaser** is a Container Action.
Therefore, a pre-built container image is pulled before starting the job.
Alternatively, a Composite Action version is available: `uses: pyTooling/Actions/releaser/composite@main`.
The Composite version installs the dependencies on the host (the runner environment), instead of using a container.
Both implementations are functionally equivalent from **Releaser**'s point of view; however, the Composite Action allows
users to tweak the version of Python by using [actions/setup-python](https://github.com/actions/setup-python) before.

## Options

All options can be optionally provided as environment variables: `INPUT_TOKEN`, `INPUT_FILES`, `INPUT_TAG`, `INPUT_RM`
and/or `INPUT_SNAPSHOTS`.

### token (required)

Token to make authenticated API calls; can be passed in using `{{ secrets.GITHUB_TOKEN }}`.

### files (required)

Either a single filename/pattern or a multi-line list can be provided. All the artifacts are uploaded regardless of the
hierarchy.

For creating/updating a release without uploading assets, set `files: none`.

### tag

The default tag name for the tip/nightly pre-release is `tip`, but it can be optionally overriden through option `tag`.

### rm

Set option `rm` to `true` for systematically removing previous artifacts (e.g. old versions).
Otherwise (by default), all previours artifacts are preserved or overwritten.

Note:
  If all the assets are removed, or if the release itself is removed, tip/nightly assets won't be available for
  users until the workflow is successfully run.
  For instance, Action [setup-ghdl-ci](https://github.com/ghdl/setup-ghdl-ci) uses assets from [ghdl/ghdl: releases/tag/nightly](https://github.com/ghdl/ghdl/releases/tag/nightly).
  Hence, it is recommended to try removing the conflictive assets only, in order to maximise the availability.

### snapshots

Whether to create releases from any tag or to treat some as snapshots.
By default, all the tags with non-empty `prerelease` field (see [semver.org: Is there a suggested regular expression (RegEx) to check a SemVer string?](https://semver.org/#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string))
are considered snapshots; neither a release is created nor assets are uploaded.

## Advanced/complex use cases

**Releaser** is essentially a very thin wrapper to use the GitHub Actions context data along with the classes
and methods of PyGithub.

Similarly to [actions/github-script](https://github.com/actions/github-script), users with advanced/complex requirements
might find it desirable to write their own Python script, instead of using **Releaser**.
In fact, since `shell: python` is supported in GitHub Actions, using Python does *not* require any Action.
For prototyping purposes, the following job might be useful:

```yml
  Release:
    name: '📦 Release'
    runs-on: ubuntu-latest
    needs:
      - ...
    if: github.event_name != 'pull_request' && (github.ref == 'refs/heads/master' || contains(github.ref, 'refs/tags/'))
    steps:

      - uses: actions/download-artifact@v3

      - shell: bash
        run: pip install PyGithub --progress-bar off

      - name: Set list of files for uploading
        id: files
        shell: python
        run: |
          from github import Github
          print("· Get GitHub API handler (authenticate)")
          gh = Github('${{ github.token }}')
          print("· Get Repository handler")
          gh_repo = gh.get_repo('${{ github.repository }}')
```

Find a non-trivial use case at [msys2/msys2-autobuild](https://github.com/msys2/msys2-autobuild).
