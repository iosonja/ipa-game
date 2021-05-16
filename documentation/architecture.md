## User Interface

The user interface has three views:
- Playing view
<img width="1312" alt="Screenshot 2021-05-16 at 15 30 40" src="https://user-images.githubusercontent.com/40118812/118407653-6ae3fb00-b68a-11eb-8165-bf3492875217.png">

- Game over -view
<img width="1312" alt="Screenshot 2021-05-16 at 15 43 06" src="https://user-images.githubusercontent.com/40118812/118407668-76372680-b68a-11eb-90b8-2df7d8560025.png">

- Top Scores -view
<img width="1312" alt="Screenshot 2021-05-16 at 15 43 17" src="https://user-images.githubusercontent.com/40118812/118407673-79caad80-b68a-11eb-87e3-bed499ebf3e2.png">


The views are handled by instances of Renderer and TextDisplayer. The displayed view depends on the methods of Renderer and TextDisplayer being called in the game loop.
The UI is separated from the logic and the code in the src/ui/ folder is independent of code outside of it.

## Game Logic

The main loop is placed in the Gameloop class. New instances of Bubble are created and the Renderer is called to update inside the main loop. There is another loop for the Game over -view and a third one for Top scores -view. The loops are separated because the tasks for each part of the game are very different. When switching from the main loop to the second loop, bubble and button elements are dropped and name typing is handled and shown on the screen instead. Switching to the third loop and Top Scores -view stops rerendering and the loop is there only for handling user input, waiting for the program to be closed.

As one can see based on the class diagram below, the game is full of unidirectional dependencies. The diagram shows both the logic and UI parts and their folder structure.<br><br>

### Class Diagram
#### NB: The image may not be displayed correctly on a screen using dark mode.
![IPAgame_class_diagram](https://user-images.githubusercontent.com/40118812/118409526-84d60b80-b693-11eb-9c01-eb056031cab7.png)


### Creation of the main loop
![Sequence Diagram_ Creating the main loop](https://user-images.githubusercontent.com/40118812/118408053-5ef93880-b68c-11eb-8dfb-53b40952ec34.png)


## Database

The program utilizes an SQLite3 database for storing nicknames and scores. It's connected to the program via a DatabaseConnection object. The database file is defined in the `.env` file that's situated in the project root.
