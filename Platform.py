import pygame

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super(Platform, self).__init__()
        self.image = pygame.image.load("images/pad.png")
        self.moving = 0
        self.reset_position()

    # resetting position
    def reset_position(self):
        self.position = pygame.Rect(
            SCREEN_WIDTH/2-70, SCREEN_HEIGHT-100, 140, 30)

    # moving the platform
    def move_platform(self, value):
        speed = 10
        self.position.move_ip(value*speed, 0)
        self.moving = value
        if self.position.left <= 0:
            self.position.x = 0
        if self.position.right >= SCREEN_WIDTH:
            self.position.x = SCREEN_HEIGHT-140

    # update
    def update(self):
        self.moving = 0
