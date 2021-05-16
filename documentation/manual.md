# Manual

## Start using the app

1. Install dependencies with the command:
```
poetry install
```
2. Start the app with the command:
```
poetry run invoke start
```
>Starting the game may take several seconds.
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

In order to make trying the application easier, there is a button in the top right corner that displays the correct
answer when clicked.
