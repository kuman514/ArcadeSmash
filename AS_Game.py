import pygame, sys, time
from pygame.locals import *




bg = pygame.image.load('gamebg.png')
player = pygame.image.load('player.png')
clerk = (pygame.image.load('clerk.png'), pygame.image.load('clerkwatching.png'))

angerGauge = pygame.image.load('gauge_anger.png')
watchGauge = pygame.image.load('gauge_watch.png')
gaugePoint = pygame.image.load('gauge_point.png')
watchMeter = pygame.image.load('watch_meter.png')

n_animation = (pygame.image.load('normalsmash1.png'), pygame.image.load('normalsmash2.png'))
s_animation = (pygame.image.load('strongsmash1.png'), pygame.image.load('strongsmash2.png'))
watched = pygame.image.load('clerkwatched.png')

cps = pygame.image.load('compensate.png')
gameover = pygame.image.load('gameover.png')



def normalSmash(watchLimit, watchCount, Display):
	for i in range(0,2,1) :
		Display.blit(n_animation[i], (0,0))
		pygame.display.update()
		time.sleep(0.18)

	if watchCount >= watchLimit :
		Display.blit(watched, (510,0))
		pygame.display.update()
		return
	else :
		return (100, -5, 8, 100)		# (money, anger, watchCount, score)



def strongSmash(watchLimit, watchCount, Display):
	for i in range(0,6,1) :
		Display.blit(s_animation[i % 2], (0,0))
		pygame.display.update()
		time.sleep(0.1)

	if watchCount >= watchLimit :
		Display.blit(watched, (510,0))
		pygame.display.update()
		return
	else :
		return (300, -10, 24, 200)		# (money, anger, watchCount, score)



def compensate(money, watchLimit, watchCount, Display):
	price = (1000, 5000, 10000, 30000)
	satisfy = (2, 12, 25, 80)
	cursor = 0

	# If you made the clerk mad, you should satisfy him by compensating.

	while True:
		for Event in pygame.event.get():
			if Event.type == QUIT:
				pygame.quit()
				sys.exit()

		Display.blit(cps, (0,0))
		pygame.draw.rect(Display, 0x0000ff, (50+(220*cursor),100,200,340), 4)

		Display.blit(watchGauge, (535,470))
		for i in range(0,watchCount,1) :
			Display.blit(gaugePoint, (535 + (4 * i), 491))

		Display.blit(watchMeter, (535 + (4 * watchLimit), 491))

		Key = pygame.key.get_pressed()

		if Key[pygame.constants.K_RETURN]:
			if money >= price[cursor] :
				money -= price[cursor]
				watchCount -= satisfy[cursor]
				if watchCount < 0 :
					watchCount = 0
			else :
				print 'not enough money!'

		elif Key[pygame.constants.K_LEFT]:
			cursor -= 1
			cursor %= 4

		elif Key[pygame.constants.K_RIGHT]:
			cursor += 1
			cursor %= 4

		elif Key[pygame.constants.K_ESCAPE]:
			return (watchCount >= watchLimit)

		pygame.display.update()



def Play(Display):
	score = 0			# Total score
	money = 0			# You can get some score on a smash
	anger = 0			# If you don't smash, your anger gets greater and greater (limit 100)

	watchLimit = 80
	watchCount = 0		# The clerk would watch
	status = 0

	font = pygame.font.Font(None, 30)

	S = time.time()
	while True:
		for Event in pygame.event.get():
			if Event.type == QUIT:
				pygame.quit()
				sys.exit()

		if watchCount >= watchLimit :
			status = 1
		else :
			if status == 1 :
				watchLimit -= 1
			status = 0

		E = time.time()
		if E - S >= 1 :
			S = time.time()
			score += 10
			anger += 2
			if watchCount > 0 :
				watchCount -= 2

		Display.fill(0x000000)
		Display.blit(bg, (0,0))
		Display.blit(player, (0,0))
		Display.blit(clerk[status], (510,0))

		text = font.render('Score : %5s' % str(score) + '    Money : %5s' % str(money), True, (0,0,0))
		textRect = text.get_rect()
		textRect.topright = [860,355]
		Display.blit(text, textRect)

		Display.blit(angerGauge, (535,460))
		for i in range(0,anger,1) :
			Display.blit(gaugePoint, (535 + (4 * i), 481))

		Display.blit(watchGauge, (535,380))
		for i in range(0,watchCount,1) :
			Display.blit(gaugePoint, (535 + (4 * i), 401))

		Display.blit(watchMeter, (535 + (4 * watchLimit), 401))

		Key = pygame.key.get_pressed()

		if Key[pygame.constants.K_RETURN]:
			print 'smash normal'
			result = normalSmash(watchLimit, watchCount, Display)
			if type(result) == tuple :
				print 'success'
				money += result[0]
				anger += result[1]
				watchCount += result[2]
				score += result[3]
			else :
				print 'oh no!'
				time.sleep(1)
				if compensate(money, watchLimit, watchCount, Display) :
					print 'game over'
					Display.blit(gameover, (0,0))
					pygame.display.update()
					time.sleep(3)
					return
				else :
					watchCount = 0
					anger = 0

		elif Key[pygame.constants.K_LSHIFT]:
			print 'smash strong'
			result = strongSmash(watchLimit, watchCount, Display)
			if type(result) == tuple :
				print 'success'
				money += result[0]
				anger += result[1]
				watchCount += result[2]
				score += result[3]
			else :
				print 'oh no!'
				time.sleep(1)
				if compensate(money, watchLimit, watchCount, Display) :
					print 'game over'
					Display.blit(gameover, (0,0))
					pygame.display.update()
					time.sleep(3)
					return
				else :
					watchCount = 0
					anger = 0

		elif Key[pygame.constants.K_q]:
			print 'quit'
			return

		if(anger < 0) :
			anger = 0

		if(anger > 100) :
			print 'game over'
			Display.blit(gameover, (0,0))
			pygame.display.update()
			time.sleep(3)
			return

		pygame.display.update()