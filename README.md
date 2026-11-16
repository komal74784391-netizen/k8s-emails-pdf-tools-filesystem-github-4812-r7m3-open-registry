# Open Methods Registry

Public-facing index of reproducible methods artifacts produced by Compass Analytics.

`registry/registry.json` is the source of truth for the generated public catalog
page. It contains one record per artifact in the current release cycle.

`registry/release_ledger.json` is maintained by the release governance team and
records the most recent release decisions. See `CONTRIBUTING.md` for field rules
and the release-state policy.

Artifact sources live under `artifacts/<artifact-folder>/` in this repository.
