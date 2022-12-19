import pygame, sys
sys.path.append(".")
from .view import View
from model.button import Button

view = View

def menu_level_two():
    view.screen.fill(view.bg_color)

    menu_mouse_pos = pygame.mouse.get_pos()

    level_one_button = Button(image = pygame.image.load("resurs/Play Rect.png"), pos = (500, 200),
                        text_input = "Уровень 2", font = pygame.font.Font("freesansbold.ttf", 65), base_color = view.accent_color,
                        hovering_color = view.game_color)
    quit_button = Button(image = pygame.image.load("resurs/Quit Rect.png"), pos = (500, 400),
                        text_input = "Выйти", font = pygame.font.Font("freesansbold.ttf", 65), base_color = view.accent_color,
                        hovering_color = view.game_color)

    for button in [level_one_button, quit_button]:
        button.changeColor(menu_mouse_pos)
        button.update(view.screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if level_one_button.checkForInput(menu_mouse_pos):
                return True
            if quit_button.checkForInput(menu_mouse_pos):
                pygame.quit()
                exit()
