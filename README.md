# IPA Game [![wakatime](https://wakatime.com/badge/github/iosonja/ot-harjoitustyo.svg)](https://wakatime.com/badge/github/iosonja/ot-harjoitustyo)<br>
The app offers a gamified way to learn the International Phonetic Alphabet symbols.

## How to use the app
The app has been built using Python version 3.6.0. Versions below that may not work as expected.

1. Install dependencies with the command:
```
poetry install
```
2. Start the app with the command:
```
poetry run invoke start
```

## Command line operations for developers
Start the app: `poetry run invoke start`<br>
Run tests: `poetry run invoke test`<br>
Create a test coverage report: `poetry run invoke coverage-report`<br>
>The covarage report will be created in a repository called _htmlcov_.
>
Analyze static code quality with pylint: `poetry run invoke lint`<br>
Reformat the code using autopep8: `poetry run invoke format`

## Documentation

[Requirements Document](https://github.com/iosonja/ot-harjoitustyo/blob/main/doc/requirements-document.md)<br>
[Time tracking](https://github.com/iosonja/ot-harjoitustyo/tree/main/doc)<br>

