import pygame
import copy


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        super(Brick, self).__init__()
        self.original_image = pygame.image.load("images/brick.png")
        self.position = pygame.Rect(x, y, 96, 48)
        self.health = health

    # refresh
    def refresh(self):
        color_mask = 0
        if self.health == 3:
            color_mask = (128, 0, 0)
        if self.health == 2:
            color_mask = (0, 0, 128)
        if self.health == 1:
            color_mask = (0, 128, 0)
        self.image = copy.copy(self.original_image)
        self.image.fill(color_mask, special_flags=pygame.BLEND_ADD)

    def update(self):
        self.refresh()

    # method used when colliding with a ball
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()
