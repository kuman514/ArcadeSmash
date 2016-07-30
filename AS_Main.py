import pygame, sys
import AS_Game
from pygame.locals import *

width = 960
height = 540

pygame.init()

Display = pygame.display.set_mode((width,height))
Title = pygame.image.load('maintitle.png')
pygame.display.set_caption('Arcade Smash')

pygame.mixer.music.load("maintheme.mp3")	# "Random Battle" by controllerhead
pygame.mixer.music.play(-1,0)

while True:
	for Event in pygame.event.get():
		if Event.type == QUIT:
			pygame.quit()
			sys.exit()

	Display.fill(0x000000)
	Display.blit(Title, (0,0))
	## Rect Tuple -> (start x, start y, width, height)

	Key = pygame.key.get_pressed()

	if Key[pygame.constants.K_RETURN] :
		print 'game start'
		pygame.mixer.music.stop()
		AS_Game.Play(Display)
		pygame.mixer.music.play(-1,0)
	elif Key[pygame.constants.K_ESCAPE] :
		print 'exit to windows'
		pygame.quit()
		sys.exit()

	pygame.display.update()
