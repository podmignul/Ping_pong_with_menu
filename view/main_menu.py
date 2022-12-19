import pygame, sys
sys.path.append(".")
from .view import View
from model.button import Button

view = View

def main_menu():
    view.screen.fill(view.bg_color)

    menu_mouse_pos = pygame.mouse.get_pos()

    menu_text = pygame.font.Font("freesansbold.ttf", 130).render("Пинг-понг", True, view.game_color)
    menu_rect = menu_text.get_rect(center = (500, 175))

    play_button = Button(image = pygame.image.load("resurs/Play Rect.png"), pos = (500, 350),
                        text_input = "Играть", font = pygame.font.Font("freesansbold.ttf", 75), base_color = view.accent_color,
                        hovering_color = view.game_color)
    quit_button = Button(image = pygame.image.load("resurs/Quit Rect.png"), pos = (500, 525),
                        text_input = "Выйти", font = pygame.font.Font("freesansbold.ttf", 75), base_color = view.accent_color,
                        hovering_color = view.game_color)

    view.screen.blit(menu_text, menu_rect)

    for button in [play_button, quit_button]:
        button.changeColor(menu_mouse_pos)
        button.update(view.screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.checkForInput(menu_mouse_pos):
                return True
            if quit_button.checkForInput(menu_mouse_pos):
                pygame.quit()
                exit()
