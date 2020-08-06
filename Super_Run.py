import pygame
import random
import math
pygame.init()

DisplayWidth = 960
DisplayHeight = 540
black = (0, 0, 0)
white = (255, 255, 255)
GameDisplay = pygame.display.set_mode((960, 540))
pygame.display.set_caption("Super Run")
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
level = 1
WinLevel = 10
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
Jumping = False
JumpTime = 0
MarioFrames = -1.001
"""
Set Basic Images
"""
DynBackground = pygame.image.load("DynBackground.jpg")
CoinCount = pygame.image.load("Coin.png")
Background = pygame.image.load('BackgroundMario.jpg')
MarioImg = [pygame.image.load('Mario3.png'),pygame.image.load('Mario2.png'),pygame.image.load('Mario1.png')]
Pipe = [(pygame.image.load("pipe.png"),340),(pygame.image.load("pipe1.png"),397)]
WinPage = pygame.image.load("WinPage.jpg")
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Level{}'.format(level), True, black,white)
background_x = 200
def Mario(s, x, y):
    if math.ceil(s)==3 or math.ceil(s)==-1:
        s = -1.05
    GameDisplay.blit(MarioImg[math.ceil(s)], (x, y))
    pygame.draw.rect(GameDisplay,white,(x,y,67,100),2)
def drawpipe(x):
    RandPipe = Pipe[random.randint(0,1)]
    GameDisplay.blit(RandPipe[0],[x,RandPipe[1]])

x = int(DisplayWidth * 0.1)
y = int(DisplayHeight * 0.68)
x_change = 0
y_change = 0
pipe_x_change = 0

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True  # Quit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Jumping = True
    if JumpTime > 5:
        y_change = 0
        JumpTime = 0
        Jumping = False
    elif Jumping:
        JumpTime += 0.1
        y_change = -150
    counting_time = pygame.time.get_ticks() - start_time
    counting_minutes = str(counting_time // 60000).zfill(1)
    counting_seconds = str((counting_time % 60000) / 1000).zfill(1)[:-2]
    counting_string = "%s:%s" % (counting_minutes, counting_seconds)
    counting_text = font.render(str(counting_string), 1, (255, 255, 255))
    level_text = font.render("Level:{}".format(str(int(level))), 1, (255, 255, 255))
    y += y_change
    GameDisplay.blit(Background, [0, 0])

    """
    Move the Background
    """
    background_x -= 1+int(level)
    if background_x <= -960: background_x = 900
    #GameDisplay.blit(counting_text, counting_rect)
    GameDisplay.blit(DynBackground, [background_x, 0])
    GameDisplay.blit(counting_text,[DisplayWidth-200,30])
    GameDisplay.blit(level_text,[DisplayWidth-400,30])
    """
    Move Pipe
    """
    pipe_x_change += 1+int(level)
    drawpipe(600-pipe_x_change)
    Mario(MarioFrames, x, y)
    if level >= WinLevel:
        GameDisplay.blit(WinPage, [0,0])
    if level >= WinLevel+0.5:
        crashed = True
    pygame.display.update()
    if MarioFrames >= 2:
        MarioFrames = -1.05
    else:
        MarioFrames += 0.1 + level // 7  # Max Speed: 0.5
    clock.tick(120)  # FPS
    y = int(DisplayHeight * 0.68)
    level+=0.0005
pygame.quit()
quit()
