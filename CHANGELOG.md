# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## 0.0.5 (2025-01-26)
### Fixes
- Handle the no-parameter call of the const decorator.
- Add more tests.

## 0.0.4 (2025-01-23)
### Fixes
- Detect reassignment in instance methods (`self.__class__.CONST`).

## 0.0.3 (2025-01-22)
### Fixes
- Remove coverage in publish on pypi GitHub action.

## 0.0.2 (2025-01-22)
### Fixes
- GitHub actions now publish the package in pypi.

## 0.0.1 (2025-01-20)
### Fixes
- First commit.
- const decorator to convert function variables to constants.
