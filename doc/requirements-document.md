# Product Requirements Document

## Purpose of the app
The app is a game for learning and revising the classification of International Phonetic Alphabets (IPA).

## Users
The app has one user type, a basic user, who can play the game and not modify the contents.

## User Interface
At least for the initial version of the game, there is only one view for the game: the playig view.

![IPA-game_ui](https://user-images.githubusercontent.com/40118812/112819372-3346d280-908d-11eb-8f7b-9a0442a7f18c.png)

In the playing view, there are bubbles with IPA characters appearing from the left side of the screen and floating towards the right edge. At the bottom there is a **classification bar** with names of the categories the characters are members of.

## Functionality
The user is expected to try and make the character bubbles disappear before they reach the right edge. This happens by dragging the corresponding category item from the classification bar to the bubble.
- If the category is correct, the bubble disappears.
- If the category is incorrect, the bubble continues floating.
- The user is allowed to retry as many times as the bubble is in sight.

- The game doesn't speed up. 
- There is only a certain number of characters and after all of them have been correctly classified, the game ends.
- In the first version of the game there are only pulmonic consonants in the bubbles, and categorization only happens for the manner of articulation (leaving out the place of articulation).

## Further development
After the most basic version, here are some features to be added to the game:
- Place of articulation added to the classification requirements
- More varied types of IPA characters: in addition to pulmonic consonants, there are also 
  - non-pulmonic consonants
  - vowels
  - diacritics
  - suprasegmentals.
- Scoring system
- Top scores list
