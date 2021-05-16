#Создай собственный Шутер!

from pygame import*
import time as tm
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.size_x = size_x
        self.size_y = size_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x  
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_left(self):
        keys = key.get+pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        elif keys[K_s] and self.rect.y < 500 - self.size_y - 5:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        pass
player1 =Player('shpagat.png.png',100,80,100,100,0)
player2 =Player('shpagat2.png',400,80,80,80,0)
ball =Enemy('ball.png.png',250,250,150,150,0)
        
window = display.set_mode((500,500))
display.set_caption("Ping-POOOOOOOOOOOOONG!")

game = True
finish = False
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if not finish:
        window.fill((83,15,173))
        player1.update()
        player1.reset()
        player2.update()
        player2.reset()
        ball.update()
        ball.reset()
        display.update()
   