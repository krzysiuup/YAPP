import pygame as pg

from src.game import Game
import src.setup

if __name__ == '__main__':
    game = Game()
    game.main()
    pg.quit()
