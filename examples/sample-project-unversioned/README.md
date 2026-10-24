# Sample Project Without an eGovFrame Version

A project whose build files declare no eGovFrame version, so it gets the name-only badge and its environment table
has no runtime row. It still declares Java and Spring Boot itself, so those development rows are listed. The blocks
below are rewritten by the [example workflow](../../.github/workflows/example-egovframe-badge.yml).

<!-- egovframe-badge:start -->
[![eGovFrame](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/unversioned/flat.svg)](https://www.egovframe.go.kr/)
<!-- egovframe-badge:end -->

## Environment

<!-- egovframe-environment:start -->
| Category | Component | Version | Source |
| --- | --- | --- | --- |
| Development environment | Java | 17 | `pom.xml` |
| Development environment | Spring Boot | 3.2.0 | `pom.xml` |
<!-- egovframe-environment:end -->
