import pygame

pygame.init()

screen_width = 1000
screen_height = 500

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("IPA game")

bubble_radius = 25
x = 0
y = 150
velocity = 5

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
        x += velocity
    if x >= screen_width + bubble_radius:
        pygame.quit()

    win.fill((212, 220, 255))
    pygame.draw.circle(win, (144, 122, 214), (x, y), bubble_radius)
    pygame.display.update()


pygame.quit()