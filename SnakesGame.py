# Hare Krishna
import pygame
x = pygame.init()

# Creating window
gameWindow = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Hare Krishna')

# Game specific variables
exit_game = False
game_over = False

# Creating a Gameloop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right arrow key.")

pygame.quit()
quit()