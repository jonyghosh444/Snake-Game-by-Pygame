# Hare Krishna
import pygame
import random
import os

pygame.init()
pygame.mixer.init()


# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = "#4b7a47"
powderBlue = "#b0e0e6"

# Creating window
screen_width = 1200
screen_height = 800
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Background Image
bgimg = pygame.image.load("snakebg.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
hmimg = pygame.image.load("snake home.jpg")
hmimg = pygame.transform.scale(hmimg, (screen_width, screen_height)).convert_alpha()
goimg = pygame.image.load("snakegameover.jpg")
goimg = pygame.transform.scale(goimg, (screen_width, screen_height)).convert_alpha()

# Game title
pygame.display.set_caption("Snakes")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_width, snake_height):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_width, snake_height])


def welcome():
    pygame.mixer.music.load('bakgroundmusic.mp3')
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:
        gameWindow.fill(black)
        gameWindow.blit(hmimg, (0, 0))
        text_screen("Welcome to Snakes", red, 430, 230)
        text_screen("Press space to play...", red, 430, 650)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameLoop()

        pygame.display.update()
        clock.tick(60)


# Game loop
def gameLoop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55

    initial_velocity = 5
    velocity_x = 10
    velocity_y = 0

    food_x = random.randint(30, int(screen_width / 2))
    food_y = random.randint(50, int(screen_height / 2))
    score = 0

    if not os.path.exists('highscorerec.txt'):
        with open('highscorerec.txt', 'w') as f:
            f.write('0')

    with open('highscorerec.txt', 'r') as f:
        highScore = f.read()

    snake_width = 20
    snake_height = 20
    food_width = 15
    food_height = 15
    fps = 60
    snk_list = []
    snk_length = 1

    while not exit_game:
        if game_over:
            gameWindow.fill(black)
            gameWindow.blit(goimg, (0, 0))
            text_screen("Press Enter To continue....", red, 380, 600)
            with open('highscorerec.txt', 'w') as f:
                f.write(str(highScore))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = initial_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -initial_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -initial_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = initial_velocity
                        velocity_x = 0

                    if event.key == pygame.K_t:
                        score = score + 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 12 and abs(snake_y - food_y) < 12:
                score = score + 10
                food_x = random.randint(30, int(screen_width / 2))
                food_y = random.randint(50, int(screen_height / 2))
                snk_length = snk_length + 5
                pygame.mixer.music.load('snakebite.mp3')
                pygame.mixer.music.play()
                if score > int(highScore):
                    highScore = score

            gameWindow.fill(black)
            gameWindow.blit(bgimg, (0, 0))
            text_screen('Score:' + str(score) + '  HighScore:'+str(highScore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, food_width, food_height])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            plot_snake(gameWindow, green, snk_list, snake_width, snake_height)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
# gameLoop()