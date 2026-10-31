# egovframe-badge project context

Observed from the `work` source at `d9edd95191ccc067587668ea221e4a7b7e420aba` on 2026-10-26.
This is a maintenance context card, not a claim that application checks were run during adoption.

## Role and public entry points

Self-contained static SVG badge source for public eGovFrame README consumers. Entry points are stable `badges/<version>/<style>.svg` URLs, language variants/buttons, `versions.json`, the single `assets/egovframe-mark.svg` logo source and Python scripts for generation/version detection/documentation sync.

## Evidence and maintenance boundaries

- `README.md`: stable raw badge URLs, detection semantics, SVG design and logo licensing distinction.
- `docs/contributing/CONTRIBUTING.en.md`: generator-only SVG edits, document source/sync rules and contribution process.
- `docs/config.yml`: six language source maps and default language.
- `.github/workflows/verify.yml`: Python 3.12, PyYAML 6.0.3, unittest suite and generator --check.
- `scripts/generate.py`, `scripts/detect_version.py`, `scripts/sync_readme.py` and `tests/` are the relevant implementation/check paths. No root AGENTS or CodeGraph index was present.

Keep the change scope and workflow policy in the [constitution](constitution.md); concept cards
link there rather than repeating the policy. Author a concept card only for actual planned work.

## Build and verification commands

- CI environment: Python 3.12 and PyYAML==6.0.3. Use isolated uv execution rather than global pip in this workspace.
- Test suite: `uv run --with PyYAML==6.0.3 python -m unittest discover -s tests -v`.
- Generated output: `uv run scripts/generate.py --check`; generation uses the same script without --check and intentionally rewrites assets.
- Documentation synchronization: `uv run --with PyYAML==6.0.3 scripts/sync_readme.py` after editing localized sources.
- Version detector example: `uv run scripts/detect_version.py --project <synthetic-project> --readme README.md --language en --style flat --check`. Choose real fixture inputs for later behavior changes. These checks were not run for adoption.

For this tooling-only adoption, verify Spec Kit CLI/integration status, installed core/bug commands,
constitution completeness, and template resolution/scaffold presence. Full application build,
lint, tests, formatter, external services, and deployment are not part of that smoke check.

## Upstream and submission baseline

This is the owner's source repository, not a GitHub fork, and remote metadata reports no actual upstream. Its verified default is main. Adoption advances only work; main and the existing egovframework branch are preserved. There is no invented external upstream or upstream-submit baseline.

For later owner-repository contributions, follow the verified main/default policy from a separate clean Orca worktree. Do not create a fictitious upstream or transfer work-only scaffolding to the public consumer/main track. Record the exact base and select only application/assets/tests/user-documentation patches appropriate to that change.
No PR is created by adoption. Do not merge `work` or cherry-pick its adoption commit into a submission.
Preserve existing submission branches and PRs. Inspect changed paths and commits against the exact
base before any later PR; exclude work-only scaffolding without deleting upstream-owned files.

## Working with the pinned tooling

Installed by `uvx --from specify-cli==1.2.3 specify init --here --force --non-interactive
--integration omp --script sh --extension bug` after checking for existing path conflicts.
The CLI's init metadata pins 1.2.3; native agent commands live in `.omp/commands/`, including
`speckit.bug.assess.md`, `speckit.bug.fix.md`, and `speckit.bug.test.md`.
Use official upgrade support for future changes and preserve local customizations.
The new [domain model card template](../templates/model-card-template.md) aligns concept meanings
before specification; it is not an ML performance or benchmark card.

Observed submission base: `d9edd95191ccc067587668ea221e4a7b7e420aba` (leejongyoung/egovframe-badge, `main`).
Submission branch status: not-applicable-no-upstream; verified own default base preserved.
