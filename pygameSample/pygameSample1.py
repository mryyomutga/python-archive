import sys

import pygame
from pygame.locals import *

pygame.init()	# pygameの初期化
screen = pygame.display.set_mode((300,400))
pygame.display.set_caption("Test")
bg = pygame.image.load("./../img/Lyn.png").convert_alpha()
rect_bg = bg.get_rect()

def main():
	while True:
		screen.fill((32,32,32,0))
		screen.blit(bg,rect_bg)
		pygame.time.wait(30)
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
if __name__ == "__main__":
	main()
