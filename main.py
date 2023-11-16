import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Legs")

# Load player images for animation
current_path = os.path.dirname(__file__)
standing_image = pygame.image.load(os.path.join(current_path, '3rd step.png'))
walking_image_1 = pygame.image.load(os.path.join(current_path, '1st Step.png'))
walking_image_2 = pygame.image.load(os.path.join(current_path, '2nd Step.png'))

# Resize images
PLAYER_SIZE = standing_image.get_width(), standing_image.get_height()
standing_image = pygame.transform.scale(standing_image, PLAYER_SIZE)
walking_image_1 = pygame.transform.scale(walking_image_1, PLAYER_SIZE)
walking_image_2 = pygame.transform.scale(walking_image_2, PLAYER_SIZE)

# Set initial player image and position
player_image = standing_image
player_rect = player_image.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT // 2)

# Set initial movement speed
speed = 5

# Animation variables
animate_counter = 0
animate_speed = 24  # Adjust the speed of animation

# Main game loop
clock = pygame.time.Clock()
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Update player position based on keys
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
        player_image = walking_image_1 if animate_counter % (animate_speed * 2) < animate_speed else walking_image_2
    elif keys[pygame.K_RIGHT]:
        player_rect.x += speed
        player_image = walking_image_1 if animate_counter % (animate_speed * 2) < animate_speed else walking_image_2
    else:
        player_image = standing_image

    # Clear the screen
    screen.fill(WHITE)

    # Draw the player
    screen.blit(player_image, player_rect)

    # Update the display
    pygame.display.flip()

    # Increment animation counter
    animate_counter += 1

    # Cap the frame rate
    clock.tick(FPS)
