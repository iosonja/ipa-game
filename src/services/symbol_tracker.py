from random import randrange
import pygame


class SymbolTracker:
    """This class works as a temporary database for symbols and their keys

    Attributes:
        _remaining_symbols: Symbols and keys that haven't yet been classified.
        _classified_symbols: Symbols and keys that have been classified.
        _current_symbol_file: The most recently randomized symbol.
        _current_key: The key that corresponds to the current symbol.
    """

    def __init__(self):
        self._remaining_symbols = self._make_symbol_dict()
        self._classified_symbols = []
        self._current_symbol_file = None
        self._current_key = None

    def _make_symbol_dict(self):
        return {
            'src/assets/symbol_images/affricate0.png': pygame.K_a,
            'src/assets/symbol_images/affricate1.png': pygame.K_a,
            'src/assets/symbol_images/approximant0.png': pygame.K_x,
            'src/assets/symbol_images/approximant1.png': pygame.K_x,
            'src/assets/symbol_images/approximant2.png': pygame.K_x,
            'src/assets/symbol_images/approximant3.png': pygame.K_x,
            'src/assets/symbol_images/approximant4.png': pygame.K_x,
            'src/assets/symbol_images/fricative0.png': pygame.K_f,
            'src/assets/symbol_images/fricative1.png': pygame.K_f,
            'src/assets/symbol_images/fricative2.png': pygame.K_f,
            'src/assets/symbol_images/fricative3.png': pygame.K_f,
            'src/assets/symbol_images/fricative4.png': pygame.K_f,
            'src/assets/symbol_images/fricative5.png': pygame.K_f,
            'src/assets/symbol_images/fricative6.png': pygame.K_f,
            'src/assets/symbol_images/fricative7.png': pygame.K_f,
            'src/assets/symbol_images/nasal0.png': pygame.K_n,
            'src/assets/symbol_images/nasal1.png': pygame.K_n,
            'src/assets/symbol_images/nasal2.png': pygame.K_n,
            'src/assets/symbol_images/plosive0.png': pygame.K_p,
            'src/assets/symbol_images/plosive1.png': pygame.K_p,
            'src/assets/symbol_images/plosive2.png': pygame.K_p,
            'src/assets/symbol_images/plosive3.png': pygame.K_p,
            'src/assets/symbol_images/plosive4.png': pygame.K_p,
            'src/assets/symbol_images/plosive5.png': pygame.K_p
        }

    def correctly_classified(self, file_path):
        """Move a symbol from remaining to classified symbols.

        Args:
            file_path (str): Path to the symbol that has just been classified.
        """

        self._classified_symbols.append(file_path)
        del self._remaining_symbols[file_path]

    def give_random_symbol_file(self):
        """Randomize one symbol from the remaining ones and reset object
        attributes accordingly.

        Returns:
            str: File path to a symbol that hasn't been classified yet.
        """

        self._current_symbol_file = list(self._remaining_symbols.keys())[
            randrange(len(self._remaining_symbols))]
        self._current_key = self._remaining_symbols.get(
            self._current_symbol_file)
        return self._current_symbol_file

    def give_key(self):
        """Give the current symbol's key value.

        Returns:
            int: The current symbol's key value.
        """

        return self._current_key

    def get_nbr_of_remaining_symbols(self):
        """Tell how many symbols there are left to classify.

        Returns:
            int: The number of remaining symbols.
        """

        return len(self._remaining_symbols)
