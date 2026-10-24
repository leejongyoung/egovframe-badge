# Sample Gradle Project

A Gradle project that declares its eGovFrame and development environment versions. The two blocks below are rewritten
by the [example workflow](../../.github/workflows/example-egovframe-badge.yml); do not edit them by hand.

<!-- egovframe-badge:start -->
placeholder
<!-- egovframe-badge:end -->

## Environment

<!-- egovframe-environment:start -->
placeholder
<!-- egovframe-environment:end -->

Where the versions come from:

- eGovFrame: `ext { set('egovframeBootParentVersion', ...) }` in `build.gradle`
- Java: `sourceCompatibility` in `build.gradle`
- Spring Boot: the `org.springframework.boot` plugin version in `build.gradle`
- Gradle: `gradle/wrapper/gradle-wrapper.properties`
