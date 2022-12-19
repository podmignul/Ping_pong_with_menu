import pygame, sys, random
sys.path.append(".")
from model.logic import MyPlayer, Opponent, Ball, GameManager


class View:
    # Общая настройка
    pygame.init()
    clock = pygame.time.Clock()

    # Настройка в окне приложения
    screen_width = 1000
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))  # Создаём основной дисплей
    pygame.display.set_caption('Пинг-понг')  # заголовок

    # Задаём цвета
    bg_color = pygame.Color('#2F373F')  # Фон
    accent_color = (27, 35, 43)  # Остальные объекты
    game_color = (212, 78, 58)

    middle_strip = pygame.Rect(screen_width / 2 - 2, 0, 4, screen_height)  # Линия в центре

    # Создадим шрифт
    game_font = pygame.font.Font("freesansbold.ttf", 29)

    # Определяем игровые объекты
    player = MyPlayer('resurs\Paddle.png', screen_width - 20, screen_height / 2, 4)  # Игрок
    opponent = Opponent('resurs\Paddle.png', 20, screen_width / 2, 4)  # Противник
    # Создаём группу
    paddle_group = pygame.sprite.Group()
    # Объявляем игрока и противника
    paddle_group.add(player)
    paddle_group.add(opponent)

    # Определяем игровой объект
    ball = Ball('resurs\Ball.png', screen_width / 2, screen_height / 2, 4, 4, paddle_group)  # Мяч
    # Создаём группу
    ball_sprite = pygame.sprite.GroupSingle()
    # Объявляем мяч
    ball_sprite.add(ball)

    game_manager = GameManager(ball_sprite, paddle_group)