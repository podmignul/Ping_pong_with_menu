import pygame

screen_width = 1000
screen_height = 600
pygame.init()
game_font = pygame.font.Font("freesansbold.ttf", 29)
screen = pygame.display.set_mode((screen_width, screen_height))  
bg_color = pygame.Color('#2F373F')  # Фон
accent_color = (27, 35, 43)  # Остальные объекты