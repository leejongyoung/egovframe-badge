# Maven declaration scope

## Definition and purpose

A detected Maven version is a declaration in one scanned pom.xml, attributed to that file. A sibling module's properties cannot supply that declaration's value or source. This keeps the highest-version badge and README environment table traceable.

## Existing model and evidence

- Public issue: https://github.com/leejongyoung/egovframe-badge/issues/11.
- Current detector: `scripts/detect_version.py`, `read_project`, `maven_candidates`, `development_candidates`, `detect`, `detect_development`, and CLI `main`.
- README contract: highest declared module version wins, and the declaring file is shown.
- Observed before fix: two added consumer-level tests fail with three failures. A module declaring 5.0.2 can be reported as 4.3.0; with reversed ordering the version is attributed to the wrong file; an unresolved placeholder borrows a sibling's value.
- Follow the existing [constitution](../memory/constitution.md) for verification and submission policy.

## Synthetic data and behavior

- `a/pom.xml` declares `org.egovframe.rte.version=5.0.2`; `b/pom.xml` declares the same property as 4.3.0. Both candidates survive, with their own sources. Highest is 5.0.2 from a regardless of traversal order.
- An empty third pom has no candidate.
- Each module's `${rte.release}` resolves only against properties declared in that pom. An unresolved reference stays unresolved rather than borrowing an unrelated module value.
- Java and Spring Boot placeholders follow the same file-local boundary.

## Non-goals and assumptions

This is a static declaration scanner, not Maven's effective-POM evaluator. It does not resolve downloaded parents, profiles, settings or arbitrary property interpolation. This fix does not introduce parent resolution; a parent-derived unresolved placeholder must not be guessed from sibling declarations. Parent pom files within the scan still contribute their own direct declarations and sources.

## Verification and submission

Keep this card on work only. Reproduce cross-module leakage before the fix; run focused and existing behavior checks once after implementation; exercise the real detector CLI on synthetic sibling modules and observe both JSON and rewritten README. Submit only detector code, meaningful regression cases and necessary consumer documentation from a clean main-based Orca worktree.

## Open questions

A future effective-parent resolution feature would need explicit local parent-coordinate validation, bounded traversal and source semantics. It is not necessary to fix sibling contamination and is not represented as an agreed feature here.
