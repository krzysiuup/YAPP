import pygame as pg

import src.constants as c
import src.scene as scene

class Game:
    def __init__(self):
        self.running = True
        self.fps = 60
        self.clock = pg.time.Clock()
        self.scene = scene.Scene()

    def main(self):
        while self.running:
            self.event_loop()
            self.scene.draw()
            pg.display.update()
            self.clock.tick(self.fps)

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    self.scene.movePlatforms(c.MOVE_DOWN)
                elif event.key == pg.K_UP:
                    self.scene.movePlatforms(c.MOVE_UP)

        for ball in self.scene.balls:
            if ball.is_outside():
                self.running = False
