# Product Requirements Document

## Purpose of the app
The app offers a gamified way to learn to classify the International Phonetic Alphabet symbols used in consonants that appear in the English language.

## Users
The app has one user type, a basic user, who can play the game and not modify the contents.

## User Interface
- [x] [Done] There is one view for the game: the playing view.

![IPA-game_ui](https://user-images.githubusercontent.com/40118812/112819372-3346d280-908d-11eb-8f7b-9a0442a7f18c.png)

- [x] [Done] In the playing view, there are bubbles appearing from the left side of the screen and floating towards the right edge.
- [x] [Done] There is a classifiable item displayed on each bubble.
- [x] [Done] There is a score counter in the upper left corner.
- [x] [Done] At the bottom there is a **text bar**.
- [ ] In the text bar, there are buttons with names of the categories the items are members of.

## Functionality
The user is expected to try and make the character bubbles disappear before they reach the right edge. This happens by categorizing the bubble correctly.
- [x] [Done] The bubble can be classified with a keystroke in the early versions.
- [ ] In later versions, classification happens with mouse dragging.
- [x] [Done] If the category is correct, the bubble disappears.
- [x] [Done] If the category is correct, scores increase by 10.
- [x] [Done] If the category is incorrect, the bubble continues floating.
- [x] [Done] If the category is incorrect, scores decrease by 2.
- [x] [Done] Scores can't go below zero.
- [x] [Done] The user is allowed to retry as many times as the bubble is in sight.

- [x] [Done] The bubbles move at a steady pace. 
- [ ] There is only a certain number of classifiable items and after all of them have been correctly classified, the game ends.
- [x] [Done] In the first versions of the game, classification happens according to bubble color, which is randomized.
- [ ] In the next versions of the game there are symbols of consonants in the bubbles, and categorization happens based on IPA symbols and their manner of articulation.

## Further development
After the most basic version, here are some features to be added to the game:
- Place of articulation added to the classification requirements
- More varied types of IPA characters: in addition to consonants, there are also 
  - vowels
  - diacritics
  - suprasegmentals.
- Top scores list
