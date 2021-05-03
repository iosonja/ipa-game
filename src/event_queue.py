import pygame


class EventQueue:
    """Events from the application are held in an EventQueue object prior to
    being processed by the system.

    Attributes: none
    """

    def get(self):
        return pygame.event.get()
