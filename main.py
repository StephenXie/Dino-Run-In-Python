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
def main():
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    level = 1
    WinLevel = 10
    isOver = -1
    pygame.mixer.music.load('music.mp3')

    Jumping = False
    Gravity = 0
    MarioFrames = -1.001
    WelcomePage = pygame.image.load("welcome.jpg")
    GameDisplay.blit(WelcomePage, [0, 0])
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    break
        else:
            continue
        break
    """
    Set Basic Images
    """
    pygame.mixer.music.play(-1)
    DynBackground = pygame.image.load("DynBackground.jpg")
    CoinCount = pygame.image.load("Coin.png")
    Background = pygame.image.load('BackgroundMario.jpg')
    MarioImg = [pygame.image.load('Mario3.png'), pygame.image.load('Mario2.png'), pygame.image.load('Mario1.png')]
    Pipe = [(pygame.image.load("pipe.png"), 340, 70, 130), (pygame.image.load("pipe1.png"), 397, 68, 70),
            (pygame.image.load("pipe2.png"), 397, 130, 70)]
    WinPage = pygame.image.load("WinPage.jpg")
    LostPage = pygame.image.load("LostPage.jpg")
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render('Level{}'.format(level), True, black, white)
    typeA = 0
    typeB = 0
    pipe_x = 0
    background_x = 200


    def Mario(s, x, y):
        if math.ceil(s) == 3 or math.ceil(s) == -1:
            s = -1.05
        GameDisplay.blit(MarioImg[math.ceil(s)], (x, y))
        #pygame.draw.rect(GameDisplay, white, (x, y, 67, 100), 2)


    def drawpipe(type, x):
        RandPipe = Pipe[type]
        GameDisplay.blit(RandPipe[0], [x, RandPipe[1]])
        #pygame.draw.rect(GameDisplay, white, (x, RandPipe[1], RandPipe[2], RandPipe[3]), 2)

    def OverTest(x,y,pipe_x,pipe_y,pipe_width):
        if (x+67 >= pipe_x) and not(y+100 < pipe_y) and not(x>pipe_x+pipe_width):
            return True
        if (y+100 > pipe_y) and not (x+67 < pipe_x) and not (x>pipe_x+pipe_width):
            return True

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
        if Gravity > 10-(level // 2):
            y_change = 0
            Gravity = 0
            Jumping = False
        elif Jumping:
            Gravity += 0.1
            y_change = -150
            MarioFrames = 2
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
        background_x -= 1 + int(level)
        if background_x <= -960: background_x = 900
        # GameDisplay.blit(counting_text, counting_rect)
        GameDisplay.blit(DynBackground, [background_x, 0])
        GameDisplay.blit(counting_text, [DisplayWidth - 200, 30])
        GameDisplay.blit(level_text, [DisplayWidth - 400, 30])
        """
        Move Pipe
        """
        if pipe_x - pipe_x_change <= 0:
            typeA = random.randint(0, 2)
            typeB = random.randint(0, 2)
            pipe_x = random.randint(400, DisplayWidth - 1)
            pipe_x_distance = random.randint(250, 300)
            pipe_x_change = 0
        pipe_x_change += 1 + int(level)
        drawpipe(typeA, pipe_x - pipe_x_change)
        drawpipe(typeB, pipe_x - pipe_x_distance - pipe_x_change)
        Mario(MarioFrames, x, y)
        if OverTest(x,y,pipe_x-pipe_x_change,Pipe[typeA][1],Pipe[typeA][2]) or OverTest(x,y,pipe_x-pipe_x_distance-pipe_x_change,Pipe[typeB][1],Pipe[typeB][2]):
            isOver = 0

        if isOver >= 0:
            GameDisplay.blit(LostPage, [0, 0])
        if isOver >= 10:
            crashed = True
        if level >= WinLevel:
            GameDisplay.blit(WinPage, [0, 0])
        if level >= WinLevel + 0.5:
            crashed = True

        pygame.display.update()
        if MarioFrames >= 2:
            MarioFrames = -1.05
        else:
            MarioFrames += 0.1 + level // 7  # Max Speed: 0.5
        clock.tick(120)  # FPS
        if isOver >= 0:
            isOver += 1
        y = int(DisplayHeight * 0.68)
        level += 0.0005
main()
for i in range(5):
    if input("play again?") == "y":
        main()
    else:
        break
pygame.quit()
quit()
