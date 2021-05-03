from random import randrange
import pygame


class SymbolTracker:
    def __init__(self):
        self._remaining_symbols = {'src/assets/affricate0.png': pygame.K_a,
                                   'src/assets/approximant0.png': pygame.K_m,
                                   'src/assets/fricative0.png': pygame.K_f,
                                   'src/assets/nasal0.png': pygame.K_n,
                                   'src/assets/plosive0.png': pygame.K_p}
        self._classified_symbols = []
        self._current_symbol_file = None
        self._current_key = None

    def correctly_classified(self, file_path):
        self._classified_symbols.append(file_path)
        del self._remaining_symbols[file_path]

    def give_random_symbol_file(self):
        self._current_symbol_file = list(self._remaining_symbols.keys())[randrange(len(self._remaining_symbols))]
        self._current_key = self._remaining_symbols.get(self._current_symbol_file)
        return self._current_symbol_file

    def give_key(self):
        return self._current_key

    def get_nbr_of_remaining_symbols(self):
        return len(self._remaining_symbols)
