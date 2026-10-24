# Sample eGovFrame Project

A minimal eGovFrame project demonstrating automatic badge version detection.

<!-- egovframe-badge:start -->
[![eGovFrame](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/unversioned/flat.svg)](https://www.egovframe.go.kr/)
<!-- egovframe-badge:end -->

This project declares its eGovFrame version via `<org.egovframe.rte.version>5.0.7</org.egovframe.rte.version>` in `pom.xml`.

## Structure

- `pom.xml` — declares the eGovFrame version via `org.egovframe.rte.version` property and uses the boot starter parent
- `src/main/java/...` — application code (omitted for brevity)

## Automatic badge update

The badge in this README is automatically kept in sync with the declared eGovFrame version by the [example workflow](../.github/workflows/example-egovframe-badge.yml).