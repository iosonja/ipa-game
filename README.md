# IPA Game
IPA Game is a desktop-based game where the player needs to classify items that appear on bubbles floating in a window view.
The player needs to classify symbols of the International Phonetic Alphabet (IPA).
The symbols that appear in the game will describe consonants that appear in the English language.

[Final Release](https://github.com/iosonja/ot-harjoitustyo/releases/tag/1.0)

## Documentation

[Instruction Manual](https://github.com/iosonja/ot-harjoitustyo/blob/main/documentation/manual.md)<br>
[Requirements Document](https://github.com/iosonja/ot-harjoitustyo/blob/main/documentation/requirements-document.md)<br>
[Architecture Document](https://github.com/iosonja/ot-harjoitustyo/blob/main/documentation/architecture.md)<br>
[Testing Document](https://github.com/iosonja/ot-harjoitustyo/blob/main/documentation/testing_document.md)<br>
[Time Tracking](https://github.com/iosonja/ot-harjoitustyo/blob/main/documentation/time-tracking.md)<br>

## Start using the app
The app has been built using Python version 3.6.0. Versions below that may not work as expected.

1. Install dependencies with the command:
```
poetry install
```
2. To use the existing mock database, keep the `.env` database filename intact. To use a different database, change the value of DATABASE_FILENAME.
3. Start the app with the command:
```
poetry run invoke start
```
>Starting the game may take several seconds in the current version.
>

## Play the game
Try to stop each bubble from reaching the right edge of the screen. The bubble disappears when the symbol displayed
on it has been classified correctly by dragging its corresponding class button until it reaches the bubble. Each correct
collision awards 10 points and each wrong collision results in a 2 point penalty. The player can try again after a
failed attempt.

<img width="500" alt="Screenshot 2021-05-16 at 15 30 40" src="https://user-images.githubusercontent.com/40118812/118397512-0494b380-b65d-11eb-9e38-9a454709d709.png">

After each symbol has been correctly classified, the game ends with a banner displaying the final score
and asking for a nickname.

<img width="500" alt="Screenshot 2021-05-16 at 15 43 06" src="https://user-images.githubusercontent.com/40118812/118397598-81c02880-b65d-11eb-9e18-dcdaf6923679.png">

After entering the nickname, top 5 scores are shown. The game has 24 rounds.

<img width="500" alt="Screenshot 2021-05-16 at 15 43 17" src="https://user-images.githubusercontent.com/40118812/118397600-84bb1900-b65d-11eb-8b94-d135cbbb7320.png">

In order to make testing the application easier, there is a button in the top right corner that displays the correct
answer when clicked.


## Command line operations
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
