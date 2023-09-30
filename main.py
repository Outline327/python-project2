import time

import pygame
import sys

pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Image Example")

# Load your image
image = pygame.image.load("C:\\Users\\ROG STRIX\\PycharmProjects\\team_forest_3\\pixil-frame-0 (1).png")
image_rect = image.get_rect()

# Set the initial position
x, y = 100, 100
image_rect.topleft = (x, y)




# Define some variables
speed = 5
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Update the image's position based on user input
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed

    # Clear the screen
    screen.fill((0, 0, 0))

    # Blit the image onto the screen
    screen.blit(image, (x, y))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
