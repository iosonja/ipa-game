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
The user is expected to try and make the character bubbles disappear before they reach the right edge. This happens by categorizing the bubble correctly.
- [Done] The bubble can be classified with a keystroke in the early versions.
- In later versions, classification happens with mouse dragging.
- [Done] If the category is correct, the bubble stops.
- [Done] If the category is incorrect, the bubble continues floating.
- [Done] The user is allowed to retry as many times as the bubble is in sight.

- [Done] The bubbles move at a steady pace. 
- There is only a certain number of characters and after all of them have been correctly classified, the game ends.
- [Done] In the first versions of the game, classification happens according to bubble color, which is randomized.
- In the next versions of the game there are symbols of pulmonic consonants in the bubbles, and categorization only happens for the manner of articulation (leaving out the place of articulation).

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
