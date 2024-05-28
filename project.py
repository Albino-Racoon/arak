import pygame

from Platform import Platform
from Ball import Ball
from Brick import Brick

# height and width of the screen
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800
level = 0
lives = 3

# pygame settings
pygame.init()
pygame.font.init()

# font, display, clock and background objects
font = pygame.font.SysFont('Comic Sans MS', 24)
display = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
background_image = pygame.image.load('images/background.png')

# game levels
level1 = [
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
level2 = [
    [0, 0, 1, 2, 3, 3, 2, 1, 0, 0],
    [0, 1, 1, 1, 2, 2, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 2, 0, 0, 2, 0, 2, 0]
]
level3 = [
    [2, 3, 2, 2, 2, 2, 2, 2, 3, 2],
    [2, 1, 3, 1, 1, 1, 1, 3, 1, 2],
    [2, 3, 1, 3, 1, 1, 3, 1, 3, 2],
    [3, 2, 2, 2, 3, 3, 2, 2, 2, 3],
    [0, 0, 2, 2, 3, 3, 2, 2, 0, 0],
    [0, 0, 2, 0, 3, 3, 0, 2, 0, 0],
    [0, 0, 3, 0, 3, 3, 0, 3, 0, 0]
]

bricks = pygame.sprite.Group()


def add_bricks():
    loaded_level = None
    if level == 0:
        loaded_level = level1
    if level == 1:
        loaded_level = level2
    if level == 2:
        loaded_level = level3

    for i in range(10):
        for j in range(7):
            if loaded_level[j][i] != 0:
                brick = Brick(32+i*96, 32+j*48, loaded_level[j][i])
                bricks.add(brick)


add_bricks()

platform = Platform()
ball = Ball()

# main game loop
game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False
        elif event.type == pygame.QUIT:
            game_on = False

    # platform controls
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_a]:
        platform.move_platform(-1)
    if pressed_keys[pygame.K_d]:
        platform.move_platform(1)

    # checking if all bricks have been destroyed
    if len(bricks.sprites()) == 0:
        level += 1
        if level >= 3:
            break
        ball.reset_position()
        platform.reset_position()
        add_bricks()

    # ball update
    ball.update(platform, bricks)

    # checking if ball has touched the lower edge of the screen
    if ball.lost:
        lives -= 1
        if lives <= 0:
            break
        ball.reset_position()
        platform.reset_position()

    # updating bricks and the platform
    bricks.update()
    platform.update()

    # display background
    display.blit(background_image, (0, 0))

    # display bricks
    for brick in bricks:
        display.blit(brick.image, brick.position)

    # display the player and the ball
    display.blit(platform.image, platform.position)
    display.blit(ball.image, ball.position)

    # render score
    text = font.render(
        f'level: {level+1}, Lives: {lives}', False, (255, 0, 255))
    display.blit(text, (16, 16))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
