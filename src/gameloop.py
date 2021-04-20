import pygame


class GameLoop:
    def __init__(self, window, width):
        self._WINDOW = window
        self._SCREEN_WIDTH = width


    def start(self):
        BUBBLE_RADIUS = 25
        # Bubble's coordinates:
        x_bubble = 0
        y_bubble = 150
        VELOCITY = 5

        while True:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            #  keys = pygame.key.get_pressed()

            x_bubble += VELOCITY

            if x_bubble >= self._SCREEN_WIDTH + BUBBLE_RADIUS:
                # The bubble has reached the right end. Some punishment will be added here.
                pygame.quit()  # Remove this later

            self._WINDOW.fill((212, 220, 255))
            pygame.draw.circle(self._WINDOW, (144, 122, 214), (x_bubble,
                            y_bubble), BUBBLE_RADIUS)
            pygame.display.update()

        pygame.quit()
