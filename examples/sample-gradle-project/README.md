# Sample Gradle Project

A Gradle project that declares its eGovFrame and development environment versions. The two blocks below are rewritten
by the [example workflow](../../.github/workflows/example-egovframe-badge.yml); do not edit them by hand.

<!-- egovframe-badge:start -->
[![eGovFrame 5.0.0](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.0/flat.svg)](https://www.egovframe.go.kr/)
<!-- egovframe-badge:end -->

## Environment

<!-- egovframe-environment:start -->
| Category | Component | Version | Source |
| --- | --- | --- | --- |
| Runtime environment | eGovFrame | 5.0.0 | `build.gradle` |
| Development environment | Java | 17 | `build.gradle` |
| Development environment | Spring Boot | 3.5.6 | `build.gradle` |
| Development environment | Gradle | 8.5 | `gradle/wrapper/gradle-wrapper.properties` |
<!-- egovframe-environment:end -->

Where the versions come from:

- eGovFrame: `ext { set('egovframeBootParentVersion', ...) }` in `build.gradle`
- Java: `sourceCompatibility` in `build.gradle`
- Spring Boot: the `org.springframework.boot` plugin version in `build.gradle`
- Gradle: `gradle/wrapper/gradle-wrapper.properties`
