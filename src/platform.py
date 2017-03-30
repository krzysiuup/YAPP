import pygame as pg

import src.constants as c

class Platform(pg.sprite.Sprite):
    def __init__(self, start_x=0):
        super().__init__()
        self.size = c.PLATFORM_WIDTH, c.PLATFORM_HEIGHT
        self.image = pg.Surface(self.size)
        self.image.fill(c.COLORS['WHITE'])
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.speed = 5

    def move(self, direction):
        self.rect = self.rect.move(0, self.speed * direction)
        self._prevent_move_outside_boundaries()

    def _prevent_move_outside_boundaries(self):
        if self._collides_with_top_boundary():
            self.rect.y = 0
        elif self._collides_with_bottom_boundary():
            self.rect.y = c.WINDOW_HEIGHT - c.PLATFORM_HEIGHT

    def _collides_with_top_boundary(self):
        return self.rect.y < 0

    def _collides_with_bottom_boundary(self):
        return self.rect.y + c.PLATFORM_HEIGHT > c.WINDOW_HEIGHT
