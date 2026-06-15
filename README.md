# Python Playwright Runner Tests

This repo is a spike into re-writing the census-eq-questionnaire runner [functional tests](https://github.com/ONSdigital/census31-eq-questionnaire-runner/tree/main/tests/functional) using Python and Playwright.

## Installation

Run:

```shell
poetry install
poetry run playwright install
```

## Running the tests

To run all the tests:

```shell
poetry run pytest
```

To run a specific test file:

```shell
poetry run pytest tests/test_textfield.py
```

To run with a real browser (slowmo makes it watchable):

```shell
poetry run pytest tests/test_textfield.py --headed --slowmo 1000
```

To specify a browser (chromium, firefox, webkit):

```shell
poetry run pytest --browser webkit
```

See <https://playwright.dev/python/docs/running-tests> and <https://playwright.dev/python/docs/test-runners#cli-arguments> for more options for running tests.
