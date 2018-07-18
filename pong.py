import pygame, sys
from pygame.locals import *

# Set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# Create window
screenWidth = 512
screenHeight = 256
DISPLAYSURF = pygame.display.set_mode((screenWidth,screenHeight), 0, 32)
pygame.display.set_caption("Pong")

# Set constants
FPS = 30
fpsClock = pygame.time.Clock()
WHITE = (255,255,255)
BLACK = (0,0,0)

# Create Paddles
paddleWidth = 10
paddleHeight = 40
leftPaddlex = 20
leftPaddley = screenHeight/2 - paddleHeight/2
rightPaddlex = screenWidth-paddleWidth - 20
rightPaddley = screenHeight/2 - paddleHeight/2
leftPaddle = pygame.Rect(leftPaddlex, leftPaddley, paddleWidth, paddleHeight)
rightPaddle = pygame.Rect(rightPaddlex, rightPaddley, paddleWidth, paddleHeight)
pygame.draw.rect(DISPLAYSURF, WHITE, leftPaddle)
pygame.draw.rect(DISPLAYSURF,WHITE, rightPaddle)

# Create Ball
ballSize = 6
ballx = screenWidth/2 - ballSize/2
bally = screenHeight/2 - ballSize/2
ball = pygame.Rect(ballx, bally, ballSize, ballSize)
pygame.draw.rect(DISPLAYSURF, WHITE, ball)

# Game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == MOUSEMOTION:
			leftPaddle.move(leftPaddlex, event.pos[1])
	ballx -= 1
	pygame.draw.rect(DISPLAYSURF, WHITE, leftPaddle)
	pygame.draw.rect(DISPLAYSURF, WHITE, rightPaddle)
	pygame.draw.rect(DISPLAYSURF, WHITE, ball)
	pygame.display.update()
	fpsClock.tick(FPS)
