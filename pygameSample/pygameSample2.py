import sys
from math import sin
from random import randrange

import pygame
from pygame.locals import *

displaySize = (640,640)

pygame.init()	# pygameの初期化
screen = pygame.display.set_mode(displaySize)
pygame.display.set_caption("Test")

bubbles = list()

# Bubbleクラス
class Bubble(object):
	def __init__(self,r,g,b,x,y,size):
		self.r, self.g, self.b = r, g, b
		self.x, self.y = x, y
		self.size = size
		self.f = randrange(0,1)

	# パラメータをセット
	def setParams(self,flag=False):
		self.r = randrange(48,255)
		self.g = randrange(48,255)
		self.b = randrange(48,255)
		self.x = randrange(0,displaySize[0])
		if not flag:
			self.y = randrange(0,displaySize[1])
		else:
			self.y = displaySize[1]
		self.size = randrange(10,40)

	# 描画メソッド
	def draw(self):
		pygame.draw.ellipse(screen,
							(self.r,self.g,self.b,128),
							(self.x,self.y,self.size,self.size)
							)
	
	# パラメータ更新メソッド
	def update(self):
		self.y -= randrange(1, 3)
		self.x += sin(self.f)
		self.f += randrange(10)
		if self.y < -self.size // 2 or self.x < -self.size or self.x > displaySize[0] + self.size:
			self.setParams(True)

# 一括して描画
def drawAll():
	for bubble in bubbles:
		bubble.draw()

# 一括して更新
def updateAll():
	for bubble in bubbles:
		bubble.update()

# ランダムなインスタンスの取得
def getInstance():
	return Bubble(randrange(48,255),
				  randrange(48,255),
				  randrange(48,255),
				  randrange(0,displaySize[0]),
				  randrange(0,displaySize[1]),
				  randrange(10,50))

# 指定数分Bubbleを追加
def getBubble(num):
	for i in range(num):
		bubbles.append(getInstance())


getBubble(150)

while True:
	screen.fill((32,32,32,32))
	drawAll()
	pygame.time.wait(1)	# 更新間隔の設定
	pygame.display.update()
	updateAll()

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
