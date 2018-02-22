import sys
import math
import pygame
from pygame.locals import *

displaySize = (640,640)

pygame.init()	# pygameの初期化
screen = pygame.display.set_mode(displaySize)
pygame.display.set_caption("Test")
x,y = 1,1
r,theta = 0,0

while True:
	screen.fill((32,32,32,32))
	pygame.time.wait(5)	# 更新間隔の設定
	pygame.draw.ellipse(screen,(32,150,255),(displaySize[0]/2+x, displaySize[1]/2+y, 20,20),0)
	r += 0.5
	theta += 0.05
	if r > 300:
		r = 0
	if theta > 360:
		theta = 0
	x = r * math.cos(theta)
	y = r * math.sin(theta)
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
