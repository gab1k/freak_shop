import sys

from gameplay_interface import Game
from menu import *
from gameplay_info_classes import GameInfo
from facade import ClientRequests
from view_model import ViewModel
from view_model import ViewWindows
from menu import ReturnStatus

if __name__ == "__main__":
    CurrentGame = Game(GameInfo(1, [1, 9, 5], 4, ["Pasha", "Sasha", "Nagibator228", "Боб"]))
    ViewModelEntity = ViewModel()
    Menu = MenuView()
    LastWindow = ViewWindows.initial_menu
    while True:
        CurrentWindow = ViewModelEntity.window
        if CurrentWindow != LastWindow:
            LastWindow = CurrentWindow
            Menu.reset_menu_info()

        if CurrentWindow == ViewWindows.initial_menu:
            Return = Menu.show_start_menu()
            if Return[0] == ReturnStatus.quit:
                sys.exit()
            elif Return[0] == ReturnStatus.go_to_login:
                ViewModelEntity.go_to_login_window()
            elif Return[0] == ReturnStatus.go_to_register:
                ViewModelEntity.go_to_registration_window()

        elif CurrentWindow == ViewWindows.login:
            Return = Menu.show_login_menu()
            if Return[0] == ReturnStatus.login:
                ViewModelEntity.login_user(Return[1][0], Return[1][1])
                if ViewModelEntity.info_window is None:
                    Menu.reset_menu_info()
                # ViewModelEntity.go_to_initial_window()
            elif Return[0] == ReturnStatus.quit:
                time.sleep(0.1)
                # ViewModelEntity.go_to_initial_window()

        elif CurrentWindow == ViewWindows.registration:
            Return = Menu.show_resgistration_menu()
            if Return[0] == ReturnStatus.register:
                ViewModelEntity.register_user(Return[1][0], Return[1][1], Return[1][2], Return[1][3])
                # ViewModelEntity.go_to_initial_window()
                if ViewModelEntity.info_window is None:
                    Menu.reset_menu_info()
            elif Return[0] == ReturnStatus.quit:
                time.sleep(0.1)
                # ViewModelEntity.go_to_initial_window()

        elif CurrentWindow == ViewWindows.main_menu:
            Return = Menu.show_main_menu()
            if Return[0] == ReturnStatus.quit:
                sys.exit()

        # Show messages
        Message = ViewModelEntity.info_window
        if Message is not None:
            Menu.show_message(Message)
        pygame.display.update()


