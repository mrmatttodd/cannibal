import sys, pygame, os

import config

screen = None
clock  = None
def init():
	global screen, clock
	pygame.init()
	clock = pygame.time.Clock()
	size = (config.width, config.height)
	screen = pygame.display.set_mode(size)


#Lets have a game
def main():
	width = config.width
	height = config.height
	speed = config.speed
	frame_rate = config.frame_rate

	try:
		ball = pygame.image.load(os.path.join("images", "ball.jpeg"))
		ballrect = ball.get_rect()
	except:
		raise UserWarning, "Unable to find images in specified folder"

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		ballrect = ballrect.move(speed)
		if ballrect.left < 0 or ballrect.right > width:
			speed[0] = -speed[0]
		if ballrect.top < 0 or ballrect.bottom > height:
			speed[1] = -speed[1]

		screen.fill((0, 0, 0))
		screen.blit(ball, ballrect)
		pygame.display.flip()
		clock.tick(frame_rate)

if __name__ == '__main__':
	init()	
	main()
