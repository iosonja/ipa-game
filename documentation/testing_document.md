# Testing Document

The program has been tested with automated unit tests and manual testing on a higher level.

## Unit- and Integration tests

### Database Connection

The DatabaseConnection class is tested with a mock database defined in a file called `.env.test`. The default test database is `test.db`.

### Test Coverage

The coverage report leaves out index-py, files in the ui-folder and gameloop.py as it mostly handles user input.
When the files above are left out, testing coverage is 98%.
<img width="870" alt="Screenshot 2021-05-16 at 22 47 31" src="https://user-images.githubusercontent.com/40118812/118410625-11cf9380-b699-11eb-9c78-0d7103b3ed4e.png">


## System Testing

System testing has been done manually.

### Functionalities

All functionalities defined in the requirements document have been tested either automatically or manually.

## Remaining Quality Issues
- There is currently no animation for returning a button back to its starting position.
- There are parts in gameloop.py that could be separated to a file that wouldn't need to be left out of coverage report.
