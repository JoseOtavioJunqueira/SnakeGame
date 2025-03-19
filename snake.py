import pygame
import random
from pygame.locals import *

def pos_decimal():
    x = random.randint(0, 59)
    y = random.randint(0, 59)
    return x * 10, y * 10


def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('SnakeGame')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

apple_pos = pos_decimal()
apple_pos1 = pos_decimal()
apple_pos2 = pos_decimal()
apple_pos3 = pos_decimal()
apple_pos4 = pos_decimal()

apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

direcao = LEFT

clock = pygame.time.Clock()

fonte = pygame.font.Font('freesansbold.ttf', 18)
pontos = 0

game_over = False
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and direcao != DOWN:
                direcao = UP
            if event.key == K_DOWN and direcao != UP:
                direcao = DOWN
            if event.key == K_LEFT and direcao != RIGHT:
                direcao = LEFT
            if event.key == K_RIGHT and direcao != LEFT:
                direcao = RIGHT

    if colisao(snake[0], apple_pos):
        apple_pos = pos_decimal()
        snake.append((0, 0))
        pontos += 1
    if colisao(snake[0], apple_pos1):
        apple_pos1 = pos_decimal()
        snake.append((0, 0))
        pontos += 1
    if colisao(snake[0], apple_pos2):
        apple_pos2 = pos_decimal()
        snake.append((0, 0))
        pontos += 1
    if colisao(snake[0], apple_pos3):
        apple_pos3 = pos_decimal()
        snake.append((0, 0))
        pontos += 1
    if colisao(snake[0], apple_pos4):
        apple_pos4 = pos_decimal()
        snake.append((0, 0))
        pontos += 1

    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if direcao == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direcao == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direcao == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direcao == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    tela.fill((0, 0, 0))
    tela.blit(apple, apple_pos)
    tela.blit(apple, apple_pos1)
    tela.blit(apple, apple_pos2)
    tela.blit(apple, apple_pos3)
    tela.blit(apple, apple_pos4)

    for x in range(0, 600, 10):
        pygame.draw.line(tela, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10):
        pygame.draw.line(tela, (40, 40, 40), (0, y), (600, y))

    score_font = fonte.render(f'Score: {pontos}', True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    tela.blit(score_font, score_rect)

    for pos in snake:
        tela.blit(snake_skin, pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    tela.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
