import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0
bool = False
fails = 0
hasJumped = False
background_color = "black"
pygame.display.set_caption("Jeffrey's epic Game of epicness")




class player:

    def __init__(self, x, y, acc, onGround):
        self.x = x
        self.y = y
        self.acc = 0
        self.onGround = onGround

    def draw(self):
        pygame.draw.circle(screen, "yellow", (self.x, self.y), 40)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.y -= 1200 * dt
        if keys[pygame.K_j]:
            self.y += 300 * dt
        if keys[pygame.K_h]:
            self.x -= 300 * dt
        if keys[pygame.K_k]:
            self.x += 300 * dt
        #if keys[pygame.K_SPACE] and self.onGround:
            #self.acc += 15
        #if self.y >= 1040:
            #self.onGround = True     

    def logic(self):
        if self.x <= 40:
            self.x = 40
        if self.x >= 1880:
            self.x = 1880
        if self.y >= 1040:  
            self.y = 1040
        if self.y <= 40:
            self.y = 40
        self.y -= self.acc
        if self.onGround:
            self.acc = 0
        else: 
            self.acc -= 0.85
        

class block:

    def __init__ (self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self):
        pygame.draw.rect(screen,self.color, pygame.Rect(self.x, self.y, self.width, self.height),100)

    def collide(self):
        #dont fall through blocks and stand on top of them :)
        if player1.x >= self.x and player1.x - 20 <= self.x + 120 and player1.y <= self.y and player1.y >= self.y - 40:
            player1.onGround = True
            #player1.y = self.y - 40
            player1.acc = 0
            player1.onGround = True
            #delay(1)
        elif player1.y >= 1040:
            player1.onGround = True
            
        elif (player1.x >= self.x and player1.x <= self.x + 100 and player1.y <= self.y and player1.y >= self.y - 40) == False and player1.y <= 1040:
            player1.onGround = False
        

text_font = pygame.font.SysFont("Times New Roman", 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

        

player1 = player(0, 1080, 0, False)
blockx = 200
blocky = 1000
block1 = block(900, 500, 150, 5, "yellow")
block2 = block(900, 400, 150, 5, "yellow")
block3 = block(1280, 400, 150, 5, "yellow")
block4 = block(1700, 650, 150, 5, "black")
list_of_blocks = []
list_of_blocks.append(block1)
list_of_blocks.append(block2)
list_of_blocks.append(block3)
list_of_blocks.append(block4)

showText = False



for i in range(4):
    obj = block(blockx + 120*i, blocky - 280*i, 100, 100, "yellow")
    list_of_blocks.append(obj)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)


    draw_text("Welcome to Jeff's Game... all are welcome... even Aiden LOL", text_font, (255, 255, 255), 100, 900 )

    if player1.x >= 320 and player1.x - 20 <= 200 + 120 +120 and player1.y <= 1000 -280 and player1.y >= 1000 - 40 -280:
        draw_text("Press hjk and space to do the normal stuff it'll just do the expected stuff... oh wait I was supposed to put this before the jump so you could actually jump oops ,_, ", text_font, (255, 255, 255), 50, 600 )

    if player1.x >= 320 and player1.x - 20 <= 200 + 120 + 120 +120 and player1.y <= 1000 -280 -280 and player1.y >= 1000 - 40 -280 -280 :
        draw_text("I hope you didn't quit before you reached here, if you did then you probably lack grit or you spent so long its time for dinner, I'm looking at you Jason", text_font, (255, 255, 255), 50, 300)
        
    if player1.x >= 320 and player1.x - 20 <= 200 + 120 + 120 +120 + 120 and player1.y <= 1000 -280 -280 - 280 and player1.y >= 1000 - 40 -280 -280 -280:
        draw_text("Ok, legit after coding for the whole day, test playing this game has been more enraging than coding the game itself. I think I'm gonna flip out", text_font, (255, 255, 255), 50, 100)

    if player1.x >= 900 and player1.x - 20 <= 900 + 120 and player1.y <= 500 and player1.y >= 500 - 40:
        draw_text("Remember when I said it took me a long time? This jump was what I was talking about KEKW", text_font, (255, 255, 255), 750, 250)

    if player1.x >= 1280 and player1.x - 20 <= 1280 + 120 and player1.y <= 400 and player1.y >= 400 - 40:
        draw_text("Hope you had fun cause I was joking cause that wasn't the JUMP", text_font, (255, 255, 255), 750, 250)
    
    if player1.x >= 1280 and player1.x - 20 <= 1280 + 120 and player1.y <= 400 and player1.y >= 400 - 40:
        draw_text("THIS IS", text_font, (255, 0, 0), 1720, 650)
        block4.color = "yellow"
    else:
        block4.color = "black"

    if player1.x >= 1780 and player1.x - 20 <= 1700 + 120 and player1.y <= 650 and player1.y >= 650 - 40 or showText:
        draw_text("CONGRADULATIONSSS!!! :D If you beat the game, email me at noveltyscript@gmail.com and let me know lol", text_font, (255, 0, 0), 200, 600)
        background_color = "white"
        showText = True





    for obj in list_of_blocks:
        obj.collide()
        obj.draw()


    player1.logic()
    player1.move() 
    player1.draw()
    
    if (player1.y >= 1040 and hasJumped) and showText != True:
        fails += 1
        hasJumped = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        hasJumped = True

    draw_text(f"Your fails are: {fails}", text_font, (255, 0, 0), 800, 100)
    

    pygame.display.flip()

    dt = clock.tick(60) / 1000

    #print(player1.onGround)
 


pygame.quit()
