import pygame, sys, time
from pygame.locals import *

def normalSmash(watchLimit, watchCount, Display):
	animation = (pygame.image.load('normalsmash1.png'), pygame.image.load('normalsmash2.png'))
	for i in range(0,2,1) :
		Display.blit(animation[i], (0,0))
		pygame.display.update()
		time.sleep(0.15)

	if watchCount >= watchLimit :
		pass
	else :
		return (10, -3, 3, 20)		# (money, anger, damage, watchCount)

def strongSmash(watchLimit, watchCount, Display):
	animation = (pygame.image.load('strongsmash1.png'), pygame.image.load('strongsmash2.png'))
	for i in range(0,6,1) :
		Display.blit(animation[i % 2], (0,0))
		pygame.display.update()
		time.sleep(0.1)

	if watchCount >= watchLimit :
		pass
	else :
		return (30, -8, 10, 45)		# (money, anger, damage, watchCount)

def compensate(money, damage):
	pass

def Play(Display):
	score = 0			# Total score
	money = 0			# You can get some score on a smash
	anger = 0			# If you don't smash your anger gets greater and greater
	damage = 0			# Damage of the arcade machine

	watchLimit = 90
	watchCount = 0		# The clerk would watch

	bg = pygame.image.load('gamebg.png')
	player = pygame.image.load('player.png')
	clerk = (pygame.image.load('clerk.png'), pygame.image.load('clerkwatching.png'))

	while True:
		for Event in pygame.event.get():
			if Event.type == QUIT:
				pygame.quit()
				sys.exit()

		if watchCount >= watchLimit :
			status = 1
		else :
			status = 0

		Display.fill(0x000000)
		Display.blit(bg, (0,0))
		Display.blit(player, (0,0))
		Display.blit(clerk[status], (510,0))

		#score += 1

		Key = pygame.key.get_pressed()

		if Key[pygame.constants.K_RETURN]:
			print 'smash normal'
			result = normalSmash(watchLimit, watchCount, Display)
			if type(result) == tuple :
				pass
			elif type(result) == bool :
				pass
		elif Key[pygame.constants.K_LSHIFT]:
			print 'smash strong'
			result = strongSmash(watchLimit, watchCount, Display)
			if type(result) == tuple :
				pass
			elif type(result) == bool :
				pass
		elif Key[pygame.constants.K_ESCAPE]:
			print 'quit'
			time.sleep(1)
			return

		pygame.display.update()