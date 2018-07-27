import pygame, sys
from pygame.locals import *

# Set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# Set constants
screenWidth = 512
screenHeight = 256
paddleWidth = 10
paddleOffset = 20
userPaddleHeight = 40
comPaddleHeight = 80
comPaddleSpeed = 25
ballSize = 6
ballSpeed = 7
FPS = 30
fpsClock = pygame.time.Clock()
WHITE = (255,255,255)
BLACK = (0,0,0)

# game flow variables
userScore = 0
comScore = 0
win = 3
goal = False

# Create window
DISPLAYSURF = pygame.display.set_mode((screenWidth,screenHeight), 0, 32)
pygame.display.set_caption("Pong     0  -  0")

# Create Paddles
userPaddle = pygame.Rect(paddleOffset, screenHeight//2 - userPaddleHeight//2, paddleWidth, userPaddleHeight)
comPaddleMove = "up"
comPaddle = pygame.Rect(screenWidth-paddleWidth - paddleOffset, screenHeight//2 - comPaddleHeight//2, paddleWidth, comPaddleHeight)
pygame.draw.rect(DISPLAYSURF, WHITE, userPaddle)
pygame.draw.rect(DISPLAYSURF,WHITE, comPaddle)

# Create Ball
ballUpward = int(0)
ballMove = "left"
ball = pygame.Rect(screenWidth//2 - ballSize//2 , screenHeight//2 - ballSize//2, ballSize, ballSize)
pygame.draw.rect(DISPLAYSURF, WHITE, ball)

def display_end_game():
	fontObj = pygame.font.Font("freesansbold.ttf", 12)
	if userScore == win:
		textSurfaceObj1 = fontObj.render("Winner!!", True, WHITE)
		textSurfaceObj2 = fontObj.render("%d  -  %d" % (userScore, comScore), True, WHITE)
	else:
		textSurfaceObj1 = fontObj.render("Loser stinky poo poo head!", True, WHITE)
		textSurfaceObj2 = fontObj.render("%d  -  %d" % (userScore, comScore), True, WHITE)
	textRectObj1 = textSurfaceObj1.get_rect()
	textRectObj2 = textSurfaceObj2.get_rect()
	textRectObj1.center = (screenWidth//2, screenHeight//2)
	textRectObj2.center = (screenWidth//2, screenHeight//2 + 20)
	DISPLAYSURF.fill(BLACK)
	DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)
	DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
	pygame.display.update()
	pygame.time.wait(6000)

def calc_upward(paddle):
	if paddle == "user":
		ballUpward = int(ball.centery - userPaddle.centery)
	else:
		ballUpward = int(ball.centery - comPaddle.centery)//2
	return ballUpward

def flip_upward(ballUpward):
	return ballUpward * -1

pygame.display.update()
pygame.time.wait(3000)

# Game loop
while True:
	DISPLAYSURF.fill(BLACK)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == MOUSEMOTION:
			# Move user paddle
			userPaddle.centery = event.pos[1]

	# Move computer paddle
	if comPaddleMove == "up":
		comPaddle.top -= comPaddleSpeed
		if comPaddle.top <= 0:
			comPaddleMove = "down"
	else:
		comPaddle.top += comPaddleSpeed
		if comPaddle.bottom >= screenHeight:
			comPaddleMove = "up"

	# Move ball
	if ballMove == "left":
		ball.left -= ballSpeed
		ball.top += ballUpward
		if ball.colliderect(userPaddle):
			ballMove = "right"
			ballUpward = calc_upward("user")
		elif ball.top <= 0 or ball.bottom >= screenHeight:
			ballUpward = flip_upward(ballUpward)
	else:
		ball.left += ballSpeed
		ball.top += ballUpward
		if ball.colliderect(comPaddle):
			comPaddleSpeed = 25
			ballMove = "left"
			ballUpward = calc_upward("com")
		elif ball.top <= 0 or ball.bottom >= screenHeight:
			ballUpward = flip_upward(ballUpward)

	# Test for goal
	if ball.right <= 0:
		comScore += 1
		pygame.display.set_caption("Pong     %d  -  %d" % (userScore, comScore))
		goal = True
	elif ball.left >= screenWidth:
		userScore += 1
		pygame.display.set_caption("Pong     %d  -  %d" % (userScore, comScore))
		goal = True
		comPaddleSpeed = 0

	# Test for end of game
	if userScore == win or comScore == win:
		display_end_game()
		pygame.quit()
		sys.exit()

	# Reset objects to starting position
	if goal:
		ball.centery = screenHeight//2
		ball.centerx = screenWidth//2
		ballUpward = 0
		userPaddle.centery = screenHeight//2
		comPaddle.centery = screenHeight//2
		goal = False
		pygame.draw.rect(DISPLAYSURF, WHITE, userPaddle)
		pygame.draw.rect(DISPLAYSURF, WHITE, comPaddle)
		pygame.draw.rect(DISPLAYSURF, WHITE, ball)		
		pygame.display.update()
		pygame.time.wait(3000)

	pygame.draw.rect(DISPLAYSURF, WHITE, userPaddle)
	pygame.draw.rect(DISPLAYSURF, WHITE, comPaddle)
	pygame.draw.rect(DISPLAYSURF, WHITE, ball)
	pygame.display.update()
	fpsClock.tick(FPS)