from gameplay_interface import Game
from menu import MenuView
from gameplay_info_classes import GameInfo

if __name__ == "__main__":
    Menu = MenuView()
    CurrentGame = Game(GameInfo( 1, [1, 9, 5], 4, ["Pasha", "Sasha", "Nagibator228", "Боб"]))
    CurrentDisplayStatus = "menu"
    while True:
        if CurrentDisplayStatus == "menu":
            CurrentDisplayStatus = Menu.ShowStartMenu()
        elif CurrentDisplayStatus == "gameplay":
            CurrentGame.StartGame()