
from snake import Snake
import time
import pygame

#Define the size of map
SIZE = 300

#Speed of the game
SPEED = 0.09

#Start a pygame
pygame.init()

#Create a new snake
snake = Snake(SIZE,SIZE)

#Global condition of the main loop
game_running = True

#create a window for the game
screen = pygame.display.set_mode((SIZE, SIZE))

#init the food then place it
rect = pygame.rect.Rect((snake.foodX,snake.foodY,10,10))
pygame.draw.rect(screen, (0,150,0), rect)

#init the head of the snake then place it
rect = pygame.rect.Rect( (snake.headX,snake.headY) , (10,10) )
pygame.draw.rect(screen, (255,255,255), rect)

#Refresh the screen
pygame.display.update()

#main loop
while game_running:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				snake.setDirection(3)
			if event.key == pygame.K_UP:
				snake.setDirection(2)
			if event.key == pygame.K_RIGHT:
				snake.setDirection(1)
			if event.key == pygame.K_DOWN:
				snake.setDirection(0)
		if event.type == pygame.QUIT:
			game_running = False

	#update the snake and return the action and a score or a graph
	action,graph = snake.update()

	if action=='end':

		#If the game is over, we print the score (size of the snake)
		print("Score :",graph)
		game_running = False

	elif action=='eat':

		#If the snake ate something,
		#draw a rect on the food and draw the new food
		rect = pygame.rect.Rect( graph[0] , (10,10) )
		pygame.draw.rect(screen, (255,255,255), rect)
		rect = pygame.rect.Rect( graph[1] , (10,10))
		pygame.draw.rect(screen, (0,150,0), rect)

	else:

		#If the snake do nothing special,
		#draw the head on the direction and remove the end of the tail
		rect = pygame.rect.Rect(graph[0],(10,10))
		pygame.draw.rect(screen, (0,0,0), rect)
		rect = pygame.rect.Rect(graph[1],(10,10))
		pygame.draw.rect(screen, (255,255,255), rect)

	#loop will make a pause or it'll run too fast
	time.sleep(SPEED)

	#Refresh the screen
	pygame.display.update()


