import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the game window
width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake settings
snake_size = 20
snake_speed = 15

# Initial snake position and direction
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = (1, 0)

# Initial food position
food = (random.randrange(1, (width // snake_size)) * snake_size,
        random.randrange(1, (height // snake_size)) * snake_size)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Move the snake
    new_head = ((snake[0][0] + snake_direction[0] * snake_size) % width,
                (snake[0][1] + snake_direction[1] * snake_size) % height)
    snake.insert(0, new_head)

    # Check for collisions
    if new_head == food:
        food = (random.randrange(1, (width // snake_size)) * snake_size,
                random.randrange(1, (height // snake_size)) * snake_size)
    else:
        snake.pop()

    # Check for self-collision
    if new_head in snake[1:]:
        pygame.quit()
        sys.exit()

    # Draw the background
    window.fill(white)

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(window, green, (segment[0], segment[1], snake_size, snake_size))

    # Draw the food
    pygame.draw.rect(window, red, (food[0], food[1], snake_size, snake_size))

    # Update the display
    pygame.display.flip()

    # Control the snake's speed
    pygame.time.Clock().tick(snake_speed)
