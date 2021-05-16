# Product Requirements Document

## Purpose of the app
The app offers a gamified way to learn to classify the International Phonetic Alphabet symbols used in consonants that appear in the English language.

## Users
The app has one user type, a basic user, who can play the game and not modify the contents.

## User Interface
#### There are three views: a playing view, a Game Over -view and a top scores -view.

- Playing view
<img width="1312" alt="Screenshot 2021-05-16 at 15 30 40" src="https://user-images.githubusercontent.com/40118812/118407653-6ae3fb00-b68a-11eb-8165-bf3492875217.png">

- Game over -view
<img width="1312" alt="Screenshot 2021-05-16 at 15 43 06" src="https://user-images.githubusercontent.com/40118812/118407668-76372680-b68a-11eb-90b8-2df7d8560025.png">

- Top Scores -view
<img width="1312" alt="Screenshot 2021-05-16 at 15 43 17" src="https://user-images.githubusercontent.com/40118812/118407673-79caad80-b68a-11eb-87e3-bed499ebf3e2.png">

- [x] In the playing view, there are bubbles appearing from the left side of the screen and floating towards the right edge.
- [x] There is a classifiable item displayed on each bubble.
- [x] There is a score counter in the upper left corner.
- [x] At the bottom there is a **text bar**.
- [x] At the bottom, there are buttons with names of the categories the items are members of.

## Functionality
The user is expected to try and make the character bubbles disappear before they reach the right edge. This happens by categorizing the bubble correctly.
- [x] The bubble can be classified by dragging buttons with a mouse.
- [x] If the category is correct, the bubble disappears.
- [x] If the category is correct, a new bubble appears from the left side.
- [x] If the category is correct, scores increase.
- [x] If the category is incorrect, the bubble continues floating.
- [x] If the category is incorrect, scores decrease.
- [x] Scores can't go below zero.
- [x] The user is allowed to retry as many times as the bubble is in sight.

- [x] The bubbles move at a steady pace. 
- [x] There is only a certain number of classifiable items and after all of them have been correctly classified, the game ends.
- [x] There are symbols of consonants in the bubbles, and categorization happens based on IPA symbols and their manner of articulation.

- [x] After the game is over, nickname is asked and added to a database with the scores.
- [x] Top scores view at the end. 

## Further development
After the most basic version, here are some features to be added to the game:
- Place of articulation added to the classification requirements
- More varied types of IPA characters: in addition to consonants, there are also 
  - vowels
  - diacritics
  - suprasegmentals.
