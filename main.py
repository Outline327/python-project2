import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of your game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image = pygame.image.load("C:\\Users\\ROG STRIX\\PycharmProjects\\pythonProject\\your_image.png.png")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 0))

    # Blit (draw) the image on the screen at a specific position
    screen.blit(image, (0, 0))  # You can adjust the position as needed

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
