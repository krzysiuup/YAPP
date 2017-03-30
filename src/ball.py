import pygame as pg

import src.constants as c

class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.height = self.width = c.BALL_HEIGHT
        self.image = pg.Surface((self.height, self.width))
        self.image.fill(c.COLORS['GREEN'])
        self.rect = self.image.get_rect()
        self.direction = {'x': 1, 'y': 1}
        self.speed = 5

    def bounce_off_platforms(self, platforms_group):
        collided_platforms = pg.sprite.groupcollide(platforms_group, self.groups()[0], False, False)

        for collision in collided_platforms:
            if (self.direction['x'] > 0 and collision.rect.x == c.WINDOW_WIDTH - c.PLATFORM_WIDTH) or \
            (self.direction['x'] < 0 and collision.rect.x < c.PLATFORM_WIDTH):
                self.direction['x'] *= -1

    def is_outside(self):
        return self.rect.x > c.WINDOW_WIDTH or self.rect.x < 0 - self.width

    def move(self):
        self.rect = self.rect.move(self.speed * self.direction['x'], self.speed * self.direction['y'])
        self._bounce()

    def _bounce(self):
        if self.rect.y > c.WINDOW_HEIGHT - self.height:
            self.direction['y'] = -1
        if self.rect.y < 0:
            self.direction['y'] = 1
