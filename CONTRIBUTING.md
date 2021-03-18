# `publicador` Contributing Guide

Hi! We're really excited that you are interested in contributing to `publicador`. Before submitting your contribution, please make sure to take a moment and read through the following guidelines:

+   [Code of Conduct](https://github.com/instituciones-abiertas/publicador/blob/main/CODE_OF_CONDUCT.md)
+   [Issue Reporting Guidelines](#issue-reporting-guidelines)
+   [Pull Request Guidelines](#pull-request-guidelines)
+   [Development Setup](#development-setup)

## Issue Reporting Guidelines

- Always use our [**bug**](https://github.com/instituciones-abiertas/publicador/issues/new?assignees=&labels=bug&template=bug_report.md&title=) or [**feature**](https://github.com/instituciones-abiertas/publicador/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=) templates to create an issue.

## Pull Request Guidelines

+  The `main` branch is just a snapshot of the latest stable release. All development should be done in dedicated branches. **Do not submit PRs against the `main` branch.**

+  Checkout a topic branch from the relevant branch, e.g. `develop`, and merge back against that branch. Please follow this convention for the new branch: `issueNumber-githubUsername-commitTitle`.

+  Most of the contributed work should generally target the `lib` directory or the `assets` directory on rare occasions when the client needs a `javascript` poke.

+  It's OK to have multiple small commits as you work on the PR. We may squash them before merging if necessary.

+   Make sure `make test` passes. (see [**development setup**](#development-setup))

+   If adding a new feature:
    +   Add accompanying test cases.
    +   Provide a convincing reason to add this feature. Ideally, you should open a suggestion issue first and have it approved before working on it.

+   If fixing a bug:
    +   If you are resolving a special issue, please follow the branch naming convention mentioned above.
    +   Provide a detailed description of the bug in the PR. Live demo preferred.
    +   Add appropriate test coverage if applicable.

## Development Setup

You will need `python` version 3.

### Committing Changes

We don't expect any strict convention, but we'd be grateful if you summarize what your modifications content is about when writing a commit.

## Attribution

This Contributing Guidelines were adapted from the [Vue.js Contributing Guide][vue-js-contributing-guide].

[vue-js-contributing-guide]: https://github.com/vuejs/vue/blob/dev/.github/CONTRIBUTING.md
