from pygame import *
from random import *
class gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.size_x = size_x
        self.size_y = size_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(gamesprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 15:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 390:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 15:
            self.rect.y-= self.speed
        if keys[K_s] and self.rect.y < 390:
            self.rect.y += self.speed
variotin = [-1, 1]
font.init()
font = font.Font(None, 35)
lose1 = font.render('LOSE LEFT PLAYER', True, (180, 0, 0))
lose2 = font.render('LOSE RIGHT PLAYER', True, (180, 0, 0))
racket1 = Player('racket.png', 5, 50, 3, 30, 120)
racket2 = Player('racket.png', 660, 300, 3, 30, 120)
ball = gamesprite('tenis_ball.png', 350, 250, 3, 60, 60)
window = display.set_mode((700, 500))
fps = 60
clock = time.Clock()
game = True
speed_x = 5
speed_y = 3
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= variotin[randint(0,1)]
        window.fill((0, 170, 255))
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (350, 250))
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (350, 250))
        ball.reset()
        racket1.update_l()
        racket2.update_r()
        racket1.reset()
        racket2.reset()
    display.update()
    clock.tick(fps)