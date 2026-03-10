from pygame import *
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
racket1 = Player('racket.png', 5, 50, 3, 30, 120)
racket2 = Player('racket.png', 660, 50, 3, 30, 120)
window = display.set_mode((700, 500))
fps = 60
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((0, 170, 255))
    racket1.update_l()
    racket2.update_r()
    racket1.reset()
    racket2.reset()
    display.update()
    clock.tick(fps)