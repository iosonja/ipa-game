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
