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
        self._remaining_symbols = {'src/assets/affricate0.png': pygame.K_a,
                                   'src/assets/approximant0.png': pygame.K_x,
                                   'src/assets/fricative0.png': pygame.K_f,
                                   'src/assets/nasal0.png': pygame.K_n,
                                   'src/assets/plosive0.png': pygame.K_p}
        self._classified_symbols = []
        self._current_symbol_file = None
        self._current_key = None

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
