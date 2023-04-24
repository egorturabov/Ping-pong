from pygame import *
window = display.set_mode((1000,650))
display.set_caption('ЛАМИНААААААТ')
fon = transform.scale(image.load('фон.jpg'),(1000,650))
clock = time.Clock()
class GamesSprite(sprite.Sprite):
    def __init__(self,picture,x,y,w,h,speed):
        super().__init__()
        self.picture = transform.scale(image.load(picture),(w,h))
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.picture,(self.rect.x,self.rect.y))
class Player(GamesSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 600:
            self.rect.y += self.speed
    def move2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 600:
            self.rect.y += self.speed
platform1 = Player('lkz buhs.png',20,300,60,200,10)
platform2 = Player('lkz buhs.png',920,300,60,200,10)
ball = GamesSprite('vh.png',460,340,50,50,5)
font.init()
font1 = font.Font(None,70)
text1 = font1.render('Победа первого игрока',True,(255,50,50))
text2 = font1.render('Победа второго игрока',True,(50,50,250))
s_x = 10
s_y = 10
balls1 = 0
balls2 = 0
game = True
while game:
    clock.tick(60)
    window.blit(fon,(0,0))
    platform1.move2()
    platform1.reset()
    platform2.move()
    platform2.reset()
    if balls1 < 3 and balls2 < 3:
        ball.rect.x += s_x
        ball.rect.y += s_y
    if ball.rect.y >= 600:
        s_y *= -1
    if ball.rect.y <= 0:
        s_y *= -1
    if sprite.collide_rect(ball,platform1):
        s_x *= -1
    if sprite.collide_rect(ball,platform2):
        s_x *= -1
    if ball.rect.x <= 0:
        ball.rect.x = 460
        balls2 += 1
    if ball.rect.x >= 950:
        ball.rect.x = 460
        balls1 += 1
    if balls1 >= 3:
        window.blit(text1,(200,300))
        #game = False
    if balls2 >= 3:
        window.blit(text2,(200,300))
        #game = False
    if balls1 < 3 and balls2 < 3:
        ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()