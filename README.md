**tip** is a Docker GitHub Action written in Python. **tip** allows to keep a pre-release and its artifacts up to date with latest builds. Combined with a workflow that is executed periodically, **tip** allows to provide a fixed release name for users willing to use daily/nightly artifacts of a project.

# Usage

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
    - uses: eine/tip@master
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
        files: |
          artifact.txt
          README.md
```

Note that the tag and the pre-release need to be created manually the first time. The workflow above will fail if the release does not exist.

# Options

All options can be optionally provided as environment variables: `INPUT_TOKEN`, `INPUT_FILES`, `INPUT_TAG` and/or `INPUT_RM`.

## token (required)

Token to make authenticated API calls; can be passed in using `{{ secrets.GITHUB_TOKEN }}`.

## files (required)

Either a single filename/pattern or a multi-line list can be provided. All the artifacts are uploaded regardless of the hierarchy.

## tag

The default tag name for the tip/nightly pre-release is `tip`, but it can be optionally overriden through option `tag`.

## rm

Set option `rm` to `true` for systematically removing previous artifacts (e.g. old versions). Otherwise (by default), all previours artifacts are preserved or overwritten.
