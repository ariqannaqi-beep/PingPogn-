from pygame import *

window_Width = 800
window_Height = 650
window = display.set_mode((window_Width, window_Height))
display.set_caption("Ping pogn!")

#connditions
Run = True

#Classes
class GameSprite(sprite.Sprite):
    #class constructor
    def __init__(self, imageFile, x, y, width, height, speed):
        #Call for the class (Sprite) constructor:
        sprite.Sprite.__init__(self)

        #every sprite must store the image property
        self.image = transform.scale(image.load(imageFile), (width, height))
        self.width = width
        self.height = height
        self.speed = speed

        #every sprite must have the rect property that represents the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    #method drawing the character on the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def Update_Left(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < window_Height - self.height:
            self.rect.y += self.speed
            
    def Update_Right(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_Height - self.height:
            self.rect.y += self.speed

player1 = Player("racket.png", 50, window_Height/2, 50, 75, 5)
player2 = Player("racket.png", window_Width - 100, window_Height/2, 50, 75, 5)

#Main loop ------------------------------------------------------------------------------------------------------------------------
GameTime = time.Clock()
while Run:
    for e in event.get():
        if e.type == QUIT:
            Run = False

    window.fill((0, 0, 0))

    player1.reset()
    player1.Update_Left()

    player2.reset()
    player2.Update_Right()
    display.update()
    GameTime.tick(60)
