from pygame import *

init()

window_Width = 600
window_Height = 500
window = display.set_mode((window_Width, window_Height))
display.set_caption("Ping pogn!")

#connditions & fonts
Run = True
is_Playing = True
Player_1_score = 0
Player_2_score = 0

FontStyle = font.SysFont("Arimo", 40)
FontStyle2 = font.SysFont("Arimo", 50)

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

class Ball(GameSprite):
    def __init__(self, imageFile, x, y, width, height, speed):
        super().__init__(imageFile, x, y, width, height, speed)

        self.ball_speed_x = self.speed
        self.ball_speed_y = self.speed

    def Update(self):
        self.rect.x += self.ball_speed_x
        self.rect.y += self.ball_speed_y

        HitUp = self.rect.y <= 0
        HitDown = self.rect.y >= window_Height - self.height

        if HitUp or HitDown:
            self.ball_speed_y *= -1

        if self.rect.colliderect(player1.rect) or self.rect.colliderect(player2.rect):
            self.ball_speed_x *= -1



player1 = Player("racket.png", 65, window_Height/2, 50, 100, 5)
player2 = Player("racket.png", window_Width - 65, window_Height/2, 50, 100, 5)
ball = Ball("tenis_ball.png", window_Width/2, window_Height/2, 50, 50, 3)

#Main loop ------------------------------------------------------------------------------------------------------------------------

GameTime = time.Clock()
while Run:
    for e in event.get():
        if e.type == QUIT:
            Run = False


    if is_Playing:
        window.fill((0, 0, 0))

        player1.reset()
        player2.reset()
        ball.reset()

        player2.Update_Right()
        player1.Update_Left()
        ball.Update()

        # Conditions & Statistics
        # Player 1 Score
        if ball.rect.x <= 0:
            Player_2_score += 1
            ball.ball_speed_x *= -1

        # Player 2 Score
        if ball.rect.x >= window_Width - ball.width:
            Player_1_score += 1
            ball.ball_speed_x *= -1

        #Win conditions
        if Player_1_score >= 5:
            WinText = FontStyle2.render("Player 1 Wins!", 1, (255, 255, 255))
            window.blit(WinText, (window_Width/3.2, window_Height/2.2))
            is_Playing = False

        if Player_2_score >= 5:
            WinText = FontStyle2.render("Player 2 Wins!", 1, (255, 255, 255))
            window.blit(WinText, (window_Width/3.2, window_Height/2.2))
            is_Playing = False
        

        #Rendering
        ScoreStr = str(Player_1_score) + " | " + str(Player_2_score)
        textScore = FontStyle.render(ScoreStr, 1, (255, 255, 255))
        window.blit(textScore, (window_Width/2.2, 10))

    display.update()
    GameTime.tick(60)
