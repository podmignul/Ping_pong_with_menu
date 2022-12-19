import pygame, sys
sys.path.append(".")
from view.view import View
from view.menu_level import menu_level
from view.main_menu import main_menu


view = View

class Input:
    
    play_one_menu = False
    level_one_play = False

    while True:
        # Проверяем действия пользователя
        for event in pygame.event.get():
            # нажал ли он на крестик чтобы закрыть игру
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # нажатие клавиш
            if event.type == pygame.KEYDOWN:  # событие типа "клавиша нажата"
                # нажатие клавиши вниз
                if event.key == pygame.K_DOWN:  # проверка нажата ли клавиша вниз
                    view.player.movement += view.player.speed
                # нажатие клавиши вверх
                if event.key == pygame.K_UP:  # проверка нажата ли клавиша вверх
                    view.player.movement -= view.player.speed
            if event.type == pygame.KEYUP:  # событие типа "клавиша отпущена"
                # нажатие клавиши вниз
                if event.key == pygame.K_DOWN:  # проверка нажата ли клавиша вниз
                    view.player.movement -= view.player.speed
                # нажатие клавиши вверх
                if event.key == pygame.K_UP:  # проверка нажата ли клавиша вверх
                    view.player.movement += view.player.speed
        
        if level_one_play == True:
            # Заполняем экран цветом
            view.screen.fill(view.bg_color)
            # Рисуем элементы
            pygame.draw.rect(view.screen, view.accent_color, view.middle_strip)
            # Запускаем игру
            view.game_manager.run_game()
            # Отрисовка окна
            pygame.display.flip()
            # Ограничеваем скорость выполнения цикла
            view.clock.tick(120) 
        elif play_one_menu == True:
            menu_level()
            level_one_play = menu_level()
            pygame.display.update()
        
        else:
            main_menu()
            play_one_menu = main_menu()
            pygame.display.update()

        

    