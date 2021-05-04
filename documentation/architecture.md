## User Interface

Currently the user interface has two views:
- playing view
- Game over -view

The views are handled by the the same class, Renderer. The displayed view depends on the method of Renderer being called in the game loop.
The UI is separated from the logic and the code in the src/ui/ folder is independent of code outside of it.

## Game Logic

The main loop that runs the game is placed in the Gameloop class. New instances of Bubble are created and the Renderer is called to update inside the main loop.
As one can see based on the class diagram below, the game is full of unidirectional dependencies. The diagram shows both the logic and UI parts and their folder structure.<br><br>
![IPAgame_class_diagram](https://user-images.githubusercontent.com/40118812/117043838-66c4ee80-ad16-11eb-9aaf-591023a523bd.jpg)

### Life cycle of the main loop
![IPA_seqdiagram](https://user-images.githubusercontent.com/40118812/117045123-d5567c00-ad17-11eb-90fd-d744b1b67c77.png)
