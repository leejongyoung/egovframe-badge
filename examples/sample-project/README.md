# Sample eGovFrame Project

A Maven project that declares its eGovFrame version. The two blocks below are rewritten by the
[example workflow](../../.github/workflows/example-egovframe-badge.yml); do not edit them by hand.

<!-- egovframe-badge:start -->
[![eGovFrame 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat.svg)](https://www.egovframe.go.kr/)
<!-- egovframe-badge:end -->

## Environment

<!-- egovframe-environment:start -->
| Category | Component | Version | Source |
| --- | --- | --- | --- |
| Runtime environment | eGovFrame | 5.0.2 | `pom.xml` |
| Development environment | Java | 17 | `pom.xml` |
<!-- egovframe-environment:end -->

Where the versions come from, all in `pom.xml`:

- eGovFrame: the `org.egovframe.rte.version` property, the `org.egovframe.boot` parent and the `org.egovframe.rte` dependency
- Java: the `java.version` property
