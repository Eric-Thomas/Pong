import pygame, sys
from pygame.locals import *

# Set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# Create window
screenWidth = 512
screenHeight = 256
DISPLAYSURF = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Pong")

# Set color constants
WHITE = (255,255,255)
BLACK = (0,0,0)

# Create Paddles
paddleWidth = 10
paddleHeight = 40
leftPaddle = pygame.Rect(20, screenHeight/2 - paddleHeight/2, paddleWidth, paddleHeight)
rightPaddle = pygame.Rect(screenWidth-paddleWidth - 20, screenHeight/2 - paddleHeight/2, paddleWidth, paddleHeight)
pygame.draw.rect(DISPLAYSURF, WHITE, leftPaddle)
pygame.draw.rect(DISPLAYSURF,WHITE, rightPaddle)

# Game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		pygame.display.update()

