import pygame
from random import randrange

RES = 800
SIZE = 40

# обозначим переменные
x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
dict = {"W": True, "S": True, "A": True, "D": True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
score = 0
fps = 40

speed_count, snake_speed = 0, 10

pygame.init()
surface = pygame.display.set_mode([RES, RES])  # устанавливаем размеры поверхности
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
img = pygame.image.load('1.jpg').convert()

def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

while True:

    surface.blit(img, (0, 0))
    # нарисуем змейку и яблоко
    [pygame.draw.rect(surface, pygame.Color('green'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
    pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))
    # очки
    render_score = font_score.render(f'ОЧКИ: {score}', 1, pygame.Color('Orange'))
    surface.blit(render_score,(5,5))

    # шаг змейки
    speed_count += 1
    if not speed_count % snake_speed:
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]

    # съедание яблока
    if snake[-1] == apple:
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length += 1
        score += 1
        snake_speed -= 1
        snake_speed = max(snake_speed, 4)

    # конец игры
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('Конец игры', 1, pygame.Color('orange'))
            surface.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            close_game()

    pygame.display.flip()
    clock.tick(fps)
    close_game()



    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dict['W']:
        dx, dy = 0, -1
        dict = {"W": True, "S": False, "A": True, "D": True}
    if key[pygame.K_a] and dict['A']:
        dx, dy = -1, 0
        dict = {"W": True, "S": True, "A": True, "D": False}
    if key[pygame.K_d] and dict['D']:
        dx, dy = 1, 0
        dict = {"W": True, "S": True, "A": False, "D": True}
    if key[pygame.K_s] and dict['S']:
        dx, dy = 0, 1
        dict = {"W": False, "S": True, "A": True, "D": True}
