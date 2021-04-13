import pygame
from button import Button

pygame.init()

screen_width = 1000
screen_height = 500

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("IPA game")

bubble_radius = 25
# Bubble's coordinates:
x_bubble = 0
y_bubble = 150
velocity = 5


# ----- Button creation -----
button_width  = 60
button_height = 25
x_button = 10
y_button = screen_height - button_height

button = Button(x_button, y_button, False)
# ----- End Button creation -----

# ----- Scores section ------
# when this reaches the number of alphabets in the game, the player wins.
score = 0
NBR_OF_ALPHABETS = 20 # Change later

# ----- End scores section -----

run = True
bubble_is_stopped = False

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        bubble_is_stopped = not bubble_is_stopped
        
    if not bubble_is_stopped:
        x_bubble += velocity

    if x_bubble >= screen_width + bubble_radius:
        # The bubble has reached the right end. Some punishment will be added here.
        pygame.quit() # Remove this later

    if score >= NBR_OF_ALPHABETS:
        # The player has won. Add a banner asking if the player wants to play again.
        pygame.quit() # Remove this later

    win.fill((212, 220, 255))
    pygame.draw.circle(win, (144, 122, 214), (x_bubble, y_bubble), bubble_radius) # bubble
    pygame.draw.rect(win, (79, 81, 140), (x_button, y_button, button_width, button_height), 3) # button
    pygame.display.update()


pygame.quit()