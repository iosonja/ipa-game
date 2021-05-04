# IPA Game [![wakatime](https://wakatime.com/badge/github/iosonja/ot-harjoitustyo.svg)](https://wakatime.com/badge/github/iosonja/ot-harjoitustyo)<br>
IPA Game is a desktop-based game where the player needs to classify items that appear on bubbles floating in a window view.
In the current version of the game, the classification is done for colors.
When the app has been finalized, the player needs to classify symbols of the International Phonetic Alphabet (IPA).
The symbols that appear in the game will describe consonants that appear in the English language.

[Release for week 5](https://github.com/iosonja/ot-harjoitustyo/releases/tag/viikko5)

## Start using the app
The app has been built using Python version 3.6.0. Versions below that may not work as expected.

1. Install dependencies with the command:
```
poetry install
```
2. Start the app with the command:
```
poetry run invoke start
```
>Starting the game may take several seconds in the current version.
>

## Play the game
Try to stop each bubble from reaching the right edge of the screen. The bubble disappears when the symbol displayed
on it has been classified correctly with a keystroke. Each correct keystroke awards 10 points and each wrong keystroke
results in a 2 point penalty. After each symbol has been correctly classified, the game ends with a banner displaying
the final score. Currently the game only goes through 5 of the 24 symbols so that testing the game doesn't take too long.
#### Correct answers (symbol on the left, keystroke on the right):
```
f => F (stands for fricative)
p => P (stands for plosive)
ʈʃ => A (stands for affricate)
m => N (stands for nasal)
r => X (stands for approximant)
```



## Command line operations for developers
Start the app:
```
poetry run invoke start
```
Run tests:
```
poetry run invoke test
```
Create a test coverage report:
```
poetry run invoke coverage-report
```
>The covarage report will be created in a repository called _htmlcov_.
>
Analyze static code quality with pylint:
```
poetry run invoke lint
```
Reformat the code using autopep8:
```
poetry run invoke format
```

## Documentation

[Instruction Manual](https://github.com/iosonja/ot-harjoitustyo/blob/main/documentation/manual.md)<br>
[Requirements Document](https://github.com/iosonja/ot-harjoitustyo/blob/main/documentation/requirements-document.md)<br>
[Architecture Document](https://github.com/iosonja/ot-harjoitustyo/blob/main/documentation/architecture.md)<br>
[Time Tracking](https://github.com/iosonja/ot-harjoitustyo/blob/main/documentation/time-tracking.md)<br>
