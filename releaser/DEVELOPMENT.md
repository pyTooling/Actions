# Releaser Development

- The connection issues explained in "Troubleshooting" might be related to some problem deep inside the Python libraries.
  Some users tried [cli/cli](https://github.com/cli/cli), which is written in golang, as an alternative to **Releaser**
  (see [msys2/msys2-installer#36](https://github.com/msys2/msys2-installer/pull/36)).
  In fact, when the Python version of **Releaser** was written, `cli` was evaluated as an alternative to PyGitHub.
  `gh release` was (and still is) not flexible enough to update the reference of a release, without deleting and
  recreating it (see [cli.github.com: manual/gh_release_create](https://cli.github.com/manual/gh_release_create)).
  Deletion and recreation is unfortunate, because it notifies all the watchers of a repository
  (see [eine/tip#111](https://github.com/eine/tip/issues/111)).
  Nevertheless, it might be desirable to evaluate using `gh release upload` (see [cli.github.com: manual/gh_release_upload](https://cli.github.com/manual/gh_release_upload)) in **Releaser**.
    - Login through SSH is not supported by `cli` (see [cli/cli#3715](https://github.com/cli/cli/issues/3715)); however,
      on GitHub Actions a token is available `${{ github.token }}` and `cli` is installed by default.

- In order to avoid **Releaser** and the dependencies being installed at runtime, we should add a workflow to build a
  container image and push it to the GitHub Container Registry (say `ghcr.io/pyTooling/Releaser`).
  Then, update `action.yml` to use that image instead of the `Dockerfile`.
  That would remove the performance penalty of having additional dependencies (such as
  [pyTooling/pyAttributes](https://github.com/pyTooling/pyAttributes) or
  [willmcgugan/rich](https://github.com/willmcgugan/rich)).

- It might be desirable to have pyTooling.Version.SemVersion handle the regular expression from
  [semver.org](https://semver.org/#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string), and use
  proper Python classes in **Releaser**.
