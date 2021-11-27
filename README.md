# Actions

Reusable steps and workflows for GitHub Actions, focused on Python packages.

## Script with post step

JavaScript Actions support defining `pre`, `pre-if`, `post` and `post-if` steps, which allow executing steps at the
beginning or the end of a job, regardless of intermediate steps failing.
Unfortunately, those are not available for any other Action type.

Action [with-post-step](with-post-step) is a generic JS Action to execute a main command and to set a command as a post
step.
It allows using the `post` feature with scripts written in bash, python or any other interpreted language available on
the environment.
See: [actions/runner#1478](https://github.com/actions/runner/issues/1478).
