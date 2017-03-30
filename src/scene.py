import pygame as pg

import src.constants as c
import src.platform as platform
import src.ball as ball

class Scene:
    def __init__(self):
        self.screen = pg.display.set_mode(c.WINDOW_SIZE)
        self._setup_objects()

    def _setup_objects(self):
        leftPlatform = platform.Platform()
        rightPlatform = platform.Platform(c.WINDOW_WIDTH - c.PLATFORM_WIDTH)
        self.platofrms = pg.sprite.Group(leftPlatform, rightPlatform)
        self.balls = pg.sprite.GroupSingle(ball.Ball())

    def draw(self):
        self.screen.fill(c.COLORS['BLACK'])
        self.horizontalPlatforms.draw(self.screen)
        self.balls.draw(self.screen)
        for ball in self.balls:
            ball.move()
            ball.bounce_from_platforms(self.horizontalPlatforms)

    def movePlatforms(self, offset):
        for platform in self.platforms:
            platform.move(offset)
