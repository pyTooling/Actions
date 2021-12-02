# Tip

**Tip** is a Docker GitHub Action written in Python.

**Tip** allows to keep a GitHub Release of type pre-release and its artifacts up to date with latest builds.
Combined with a workflow that is executed periodically, **Tip** allows to provide a fixed release name for users willing
to use daily/nightly artifacts of a project.

Furthermore, when any [semver](https://semver.org) compilant tagged commit is pushed, **Tip** can create a release and
upload assets.

## Context

GitHub provides official clients for the GitHub API through [github.com/octokit](https://github.com/octokit):

- [octokit.js](https://github.com/octokit/octokit.js) ([octokit.github.io/rest.js](https://octokit.github.io/rest.js))
- [octokit.rb](https://github.com/octokit/octokit.rb) ([octokit.github.io/octokit.rb](http://octokit.github.io/octokit.rb))
- [octokit.net](https://github.com/octokit/octokit.net) ([octokitnet.rtfd.io](https://octokitnet.rtfd.io))

When GitHub Actions was released in 2019, two Actions were made available through [github.com/actions](https://github.com/actions) for dealing with GitHub Releases:

- [actions/create-release](https://github.com/actions/create-release)
- [actions/upload-release-asset](https://github.com/actions/upload-release-asset)

However, those Actions were contributed by an employee in spare time, not officially supported by GitHub.
Therefore, they were unmaintained before GitHub Actions was out of the private beta (see [actions/upload-release-asset#58](https://github.com/actions/upload-release-asset/issues/58)) and, a year later, archived.
Those Actions are based on [actions/toolkit](https://github.com/actions/toolkit)'s hydrated version of octokit.js.

From a practical point of view, [actions/github-script](https://github.com/actions/github-script) is the natural replacement to those Actions, since it allows to use a pre-authenticated octokit.js client along with the workflow run context.
Still, it requires writing plain JavaScript.

Alternatively, there are non-official GitHub API libraries available in other languages (see [docs.github.com: rest/overview/libraries](https://docs.github.com/en/rest/overview/libraries)).
**Tip** is based on [PyGithub/PyGithub](https://github.com/PyGithub/PyGithub), a Python client for the GitHub API.

**Tip** was originally created in [eine/tip](https://github.com/eine/tip), as an enhanced alternative to using
`actions/create-release` and `actions/upload-release-asset`, in order to cover certain use cases that were being
migrated from Travis CI to GitHub Actions.
The main limitation of GitHub's Actions was/is verbosity and not being possible to dynamically define the list of assets
to be uploaded.

On the other hand, GitHub Actions artifacts do require login in order to download them.
Conversely, assets of GitHub Releases can be downloaded without login.
Therefore, in order to make CI results available to the widest audience, some projects prefer having tarballs available
as assets.
In this context, one of the main use cases of **Tip** is pushing artifacts as release assets.
Thus, the name of the Action.

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
    - uses: actions/checkout@v2

    # Build your application, tool, artifacts, etc.
    - name: Build
      run: |
        echo "Build some tool and generate some artifacts" > artifact.txt

    # Update tag and pre-release
    # - Update (force-push) tag to the commit that is used in the workflow.
    # - Upload artifacts defined by the user.
    - uses: pyTooling/Actions/tip@main
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
        files: |
          artifact.txt
          README.md
```

### Composite Action

The default implementation of **Tip** is a Container Action.
Therefore, in each run, the container image is built before starting the job.
Alternatively, a Composite Action version is available: `uses: pyTooling/Actions/tip/composite@main`.
The Composite version installs the dependencies on the host (the runner environment), instead of using a container.
Both implementations are functionally equivalent from **Tip**'s point of view; however, the Composite Action allows users
to tweak the version of Python by using [actions/setup-python](https://github.com/actions/setup-python) before.

## Options

All options can be optionally provided as environment variables: `INPUT_TOKEN`, `INPUT_FILES`, `INPUT_TAG`, `INPUT_RM` and/or `INPUT_SNAPSHOTS`.

### token (required)

Token to make authenticated API calls; can be passed in using `{{ secrets.GITHUB_TOKEN }}`.

### files (required)

Either a single filename/pattern or a multi-line list can be provided. All the artifacts are uploaded regardless of the hierarchy.

For creating/updating a release without uploading assets, set `files: none`.

### tag

The default tag name for the tip/nightly pre-release is `tip`, but it can be optionally overriden through option `tag`.

### rm

Set option `rm` to `true` for systematically removing previous artifacts (e.g. old versions). Otherwise (by default), all previours artifacts are preserved or overwritten.

### snapshots

Whether to create releases from any tag or to treat some as snapshots. By default, all the tags with non-empty `prerelease` field (see [semver.org: Is there a suggested regular expression (RegEx) to check a SemVer string?](https://semver.org/#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string)) are considered snapshots; neither a release is created nor assets are uploaded.

## Advanced/complex use cases

**Tip** is essentially a very fine wrapper to use the GitHub Actions context data along with the classes
and methods of PyGithub.

Similarly to [actions/github-script](https://github.com/actions/github-script), users with advanced/complex requirements might find it desirable to write their own Python script, instead of using **Tip**.
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

      - uses: actions/download-artifact@v2

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
