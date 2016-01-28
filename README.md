[![Circle CI](https://circleci.com/gh/pantheon-systems/test_coverage_example.svg?style=shield&circle-token=:fccbb1a2b24d20deedd2bf8178ba8aacab19e2af)](https://circleci.com/gh/pantheon-systems/test_coverage_example)
[![Coverage Status](https://coveralls.io/repos/github/pantheon-systems/test_coverage_example/badge.svg?branch=master)](https://coveralls.io/github/pantheon-systems/test_coverage_example?branch=master)

fibonacci
===============

An example of linting, behavior driven development, unit testing, test coverage reporting, and continuous integration using an implementation of a fibonacci sequence generator.

## Requirements

'make prep'

## Testing packages

autopep8==1.2.1

behave==1.2.5

pytest==2.8.5

pytest-cov==2.2.0

coveralls==1.1

## Testing services

[Circle CI](https://circleci.com)

[Coveralls](https://coveralls.io)

## How to Run Tests

It's highly suggested that you run on a virtual machine like vagrant. If you have vagrant installed you can start with

`make vagrant`

If your vagrant box is a fedora

`make setupfedora; source /usr/bin/virtualenvwrapper.sh; mkvirtualenv testcovex; make prep; make test`

If you are on a mac

`make setupmac; source /usr/bin/virtualenvwrapper.sh; mkvirtualenv testcovex; make prep; make test`

To run tests by themselves

`make test`