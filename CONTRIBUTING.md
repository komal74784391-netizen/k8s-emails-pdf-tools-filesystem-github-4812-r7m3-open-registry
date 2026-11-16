# Registry Contribution Rules

## Files

- `registry/registry.json` - one record per catalog entry. Do not add or remove
  entries outside a release cycle.
- `registry/release_ledger.json` - decisions recorded by the release governance
  team.
  This ledger is the authoritative record of release state. When the ledger
  and an artifact-side manifest disagree, the ledger wins; artifact manifests
  routinely lag behind governance decisions.

## Entry schema

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | stable catalog identifier |
| `title` | string | human-readable artifact title |
| `artifact_type` | string | one of toolkit / dataset / model / benchmark |
| `maintained_by` | string | owning team |
| `repo_url` | string | optional absolute repository URL |

`repo_url` must point at an artifact that is publicly available at sync time.
Entries that cannot be published keep the field empty (or omit it entirely).
Never link to a placeholder project.

The repository URL of a published artifact is the absolute URL of its source
folder, i.e. `https://github.com/<owner>/<repository>/tree/main/artifacts/<artifact-folder>`.

## Sync workflow

1. Read `registry/registry.json` and `registry/release_ledger.json`.
2. Inspect each artifact's own source folder before writing anything.
3. Update `repo_url` only where the release policy allows.
4. Notify the release-governance contact with the standard sync message.
