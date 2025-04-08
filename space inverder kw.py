import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game with Background Image and Music")

# Load background image
background = pygame.image.load("background.jpg")

# Load and play background music
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)  # -1 means loop forever

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background image
    screen.blit(background, (0, 0))

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
