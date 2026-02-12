import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("The Brick Breakout Game")
running = True
FPS = 45
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None, 36)
gamestate = "serve"

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
        self.lives = 20
    def update(self):
        global gamestate
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        if self.rect.x > 900 or self.rect.x < 0:
            self.velocity_x *= -1
        if self.rect.y > 700:
            self.rect.y = 450
            self.rect.x = 450
            self.velocity_x = 0
            self.velocity_y = 0
            self.lives -= 1
            gamestate = "serve"
        if self.rect.y < 0:
            self.velocity_y *= -1
class Bricks(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((70, 25))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (x, y))
    def update(self):
        pass
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 18))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (450, 675)
        self.speed = 0.7
        self.image.fill('white')
    def update(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect.x -= self.speed
            if event.key == pygame.K_RIGHT:
                self.rect.x += self.speed
        
ball = Ball()
paddle = Paddle()
brickgroup = pygame.sprite.Group()
colors = ['red', 'blue', 'gold', 'green', 'pink', 'brown']
for row in range(5):
    for col in range(10):
        x = 20+100 * col
        y = 20+50 * row
        color = random.choice(colors)

        brick = Bricks(x, y, color)
        brickgroup.add(brick)
        


allsprites = pygame.sprite.Group()
allsprites.add(ball, paddle)


while running:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gamestate == "serve":
                ball.velocity_x = 0.7
                ball.velocity_y = -0.8
                gamestate = "play"
    if ball.rect.colliderect(paddle.rect):
        ball.velocity_y *= -1 

    if pygame.sprite.spritecollide(ball, brickgroup, True):
        ball.velocity_y *= -1
        print(len(brickgroup))
        score += 1

    if ball.lives <= 0:
        gamestate = "end"
    if len(brickgroup) == 0:
        gamestate = "finish"
    if gamestate == "finish":
        gamewin = font.render(f"You Won!", True, 'white')
        gamewin1 = gameover.get_rect(centerx = 500, centery = 350)
        screen.blit(gamewin, gamewin1)
        pygame.display.update()
        time.sleep(5)
        running = False

    if gamestate == "end":
        gameover = font.render(f"You Lost! Game Over!", True, 'white')
        game_rect = gameover.get_rect(centerx = 500, centery = 350)
        screen.blit(gameover, game_rect)
        pygame.display.update()
        time.sleep(5)
        running = False
       
    if gamestate == "serve":
        start = font.render(f"Press SPACE to start!", True, 'white')
        start_rect = start.get_rect(centerx = 500, centery = 500)
        screen.blit(start, start_rect)

    allsprites.draw(screen)
    allsprites.update()
    brickgroup.draw(screen)

    score_text = font.render(f"Score: {score}", True, 'white')
    score_rect = score_text.get_rect(centerx = 100, centery = 300)
    screen.blit(score_text, score_rect)

    lives_text = font.render(f"Lives: {ball.lives}", True, 'white')
    lives_rect = lives_text.get_rect(centerx = 900, centery = 300)
    screen.blit(lives_text, lives_rect) 

    
    pygame.display.update()

pygame.quit()