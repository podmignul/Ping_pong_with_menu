import pygame, sys, random
sys.path.append(".")
from model.object import *

class Block(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

# Класс анимации игрока(логика)
class MyPlayer(Block):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__(path, x_pos, y_pos)
        self.speed = speed
        self.movement = 0

    # Ограничиваем действие игрока, чтобы он не выходил за пределы поля
    def screen_constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

    # Обновляем скорость игрока
    def update(self, ball_group):
        self.rect.y += self.movement
        self.screen_constrain()

# Класс анимации мяча
class Ball(Block):
    def __init__(self, path, x_pos, y_pos, speed_x, speed_y, paddles):
        super().__init__(path, x_pos, y_pos)
        self.speed_x = speed_x * random.choice((-1, 1))  # При старте отправление мяча в рандомную сторону
        self.speed_y = speed_y * random.choice((-1, 1))  # При старте отправление мяча в рандомную сторону
        self.paddles = paddles  # Группа ракеток
        self.active = False  # Определение движется мяч или нет
        self.score_time = 0

    # Обновляем данные, если мяч движется перемещаем его и проверяем наличие столкновений
    def update(self):
        if self.active:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.collisions()
        else:
            self.restart_counter()  # Запускаем счётчик перезапуска

    # Определим проверку столкновения мяча 	
    def collisions(self):
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:  # Вертикально
            self.speed_y *= -1

        # Сделаем отталкивание от игрока и противника со всех сторон
        if pygame.sprite.spritecollide(self, self.paddles, False):
            collision_paddle = pygame.sprite.spritecollide(self, self.paddles, False)[0].rect
            if abs(self.rect.right - collision_paddle.left) < 10 and self.speed_x > 0:
                self.speed_x *= -1
            if abs(self.rect.left - collision_paddle.right) < 10 and self.speed_x < 0:
                self.speed_x *= -1
            if abs(self.rect.top - collision_paddle.bottom) < 10 and self.speed_y < 0:
                self.rect.top = collision_paddle.bottom
                self.speed_y *= -1
            if abs(self.rect.bottom - collision_paddle.top) < 10 and self.speed_y > 0:
                self.rect.bottom = collision_paddle.top
                self.speed_y *= -1

    # Определяем метод сброса мяча
    def reset_ball(self):
        self.active = False
        self.speed_x *= random.choice((-1, 1))
        self.speed_y *= random.choice((-1, 1))
        self.score_time = pygame.time.get_ticks()  # Начало отсчёта по таймеру, устанавливается время подсчёта очков
        self.rect.center = (screen_width / 2, screen_height / 2)  # Рестарт мяча в центр

     # Определяем метод сброса мяча
    def restart_counter(self):
            current_time = pygame.time.get_ticks()
            countdown_number = 3

            if current_time - self.score_time <= 700:
                countdown_number = 3
            if 700 < current_time - self.score_time <= 1400:
                countdown_number = 2
            if 1400 < current_time - self.score_time <= 2100:
                countdown_number = 1
            if current_time - self.score_time >= 2100:
                self.active = True

            time_counter = game_font.render(str(countdown_number), True, accent_color)
            time_counter_rect = time_counter.get_rect(center=(screen_width / 2, screen_height / 2 + 50))
            pygame.draw.rect(screen, bg_color, time_counter_rect)
            screen.blit(time_counter, time_counter_rect)

# Класс анимации противника(логика)
class Opponent(Block):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__(path, x_pos, y_pos)
        self.speed = speed

    # Меняем положение противника в зависимости от того где находиться мяч
    def update(self, ball_group):
        if self.rect.top < ball_group.sprite.rect.y:
            self.rect.y += self.speed
        if self.rect.bottom > ball_group.sprite.rect.y:
            self.rect.y -= self.speed
        self.constrain()

    # Ограничиваем действие противника, чтобы он не выходил за пределы поля
    def constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

# Класс остальных фишек игры
class GameManager:
    def __init__(self, ball_group, paddle_group):
        self.player_score = 0
        self.opponent_score = 0
        self.ball_group = ball_group
        self.paddle_group = paddle_group

    def run_game(self):
        # Рисуем игровые объекты
        self.paddle_group.draw(screen)
        self.ball_group.draw(screen)

        # Обновляем игровые объекты
        self.paddle_group.update(self.ball_group)
        self.ball_group.update()
        self.reset_ball()  # Сбросим мяч
        self.draw_score()  # Сравняем счёт

    # Определяем метод сброса мяча
    def reset_ball(self):
        if self.ball_group.sprite.rect.right >= screen_width:
            self.opponent_score += 1  # Добавляем очко противнику за гол
            self.ball_group.sprite.reset_ball()
        if self.ball_group.sprite.rect.left <= 0:
            self.player_score += 1  # Добавляем очко игроку за гол
            self.ball_group.sprite.reset_ball()

    # Рисуем счёт
    def draw_score(self):
        # Создадим поверхность с текстом для очков игрока и противника
        player_score = game_font.render(str(self.player_score), True, accent_color)
        opponent_score = game_font.render(str(self.opponent_score), True, accent_color)

        player_score_rect = player_score.get_rect(midleft=(screen_width / 2 + 40, screen_height / 2))
        opponent_score_rect = opponent_score.get_rect(midright=(screen_width / 2 - 40, screen_height / 2))

        # Наложим поверхность с текстом для очков игрока и противника на основную поверхность
        screen.blit(player_score, player_score_rect)
        screen.blit(opponent_score, opponent_score_rect)