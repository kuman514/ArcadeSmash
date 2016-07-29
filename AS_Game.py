import pygame, sys, time
from pygame.locals import *

def normalSmash(watching):
	return (10, -1, 3, 20)		# (money, anger, damage, watchCount)

def strongSmash(watching):
	return (30, -3, 10, 45)	# (money, anger, damage, watchCount)

def compensate(money):
	pass

def Play(Display):
	score = 0			# Total score
	money = 0			# You can get some score on a smash
	anger = 0			# If you don't smash your anger gets greater and greater
	damage = 0			# Damage of the arcade machine

	watchLimit = 90
	watchCount = 0		# The clerk would watch
	watching = False	# If the clerk is seeing you...

	while True:
		for Event in pygame.event.get():
			if Event.type == QUIT:
				pygame.quit()
				sys.exit()

		Display.fill(0x000000)
		score += 1

		Key = pygame.key.get_pressed()

		if Key[pygame.constants.K_RETURN]:
			print 'smash normal'
			result = normalSmash()
			if type(result) == tuple :
				pass
			elif type(result) == bool :
				pass

		elif Key[pygame.constants.K_LSHIFT]:
			print 'smash strong'
			result = strongSmash()
			if type(result) == tuple :
				pass
			elif type(result) == bool :
				pass

		elif Key[pygame.constants.K_ESCAPE]:
			print 'quit'
			time.sleep(1)
			return

	pygame.display.update()