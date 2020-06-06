**tip** is a Docker GitHub Action written in Python. **tip** allows to keep a pre-release and its artifacts up to date with a latest builds. Combined with a workflow that is executed periodically, **tip** allows to provide a fixed release name for users willing to use daily/nightly artifacts of a project.

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

The default tag name is `tip`, but it can be optionally overriden through option `tag` or setting envvar `INPUT_TAG`.

If you systematically want to remove previous artifacts (e.g. old versions), set the `rm` option to true.
