import pygame
import random
pygame.init()
screen = pygame.display.set_mode((900, 700))
screen.fill('black')
pygame.display.set_caption("The Brick Breakout Game")
running = True
FPS = 60
clock = pygame.time.Clock()


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15,15))
        self.image.fill('white')
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 450
        self.width = 10
        self.length = 10
        self.velocity_x = 0
        self.velocity_y = 0
    def update(self):
        if self.rect.x > 900 or self.rect.x < 0:
            self.velocity_x *= -1
        if self.rect.y > 700:
            self.rect.y = 450
            self.rect.x = 450
        if self.rect.y < 0:
            self.velocity_y *= -1
class Bricks(pygame.sprite.Sprite):
    def _init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 25))
        self.image.fill('red')
        self.rect = self.image.get_rect()
    def update(self):
        pass
                
ball = Ball()
brickgroup = pygame.sprite.Group()
brick = Bricks()
# brickgroup.add(brick)
colors = ['red', 'blue', 'gold', 'green', 'pink', 'brown']
# for row in range(5):
#     for col in range(10):
#         x = 100 * row
#         y = 50 * col
#         color = random.choice(colors)

#         brick = Bricks(x, y, color)
#         brickgroup.add(brick)
        

allsprites = pygame.sprite.Group()
allsprites.add(ball, brick)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         ball.velocity_x = 1
        #         ball.velocity_y = -2
            
    # allsprites.draw(screen)
    # brickgroup.draw(screen)
    pygame.display.update()

pygame.quit()