import pygame as pyg
from bullet import Bullet	
from random import randint, shuffle

class Enemy():
	def __init__(self, win, x, y):
		self.crutch = [(i if i%7 != 0 else 1) for i in range(100)]
		self.crutch.append(7)
		shuffle( self.crutch )
		self.x = x
		self.y = y
		self.win = win 
		self.w = 25
		self.h = 25
		self.live = 5
		self.img = pyg.image.load("invador.png")
		self.img_hit = pyg.image.load("invador_hit.png")
		self.win.blit(self.img, (self.x, self.y) )
	
	def move(self, bias):
		self.x += bias
		shot_or_not = randint(0, len(self.crutch)-1)
		if self.crutch[shot_or_not]%7 == 0 and self.live > 0:
			bullet = self.shot()
		if self.live > 0:
			self.win.blit(self.img, (self.x, self.y) )
		try:
			return bullet
		except:
			pass
	
	def shot(self):
		return Bullet(self.x, self.y+30, self.win, -10)
	
	def hit(self):
		self.live -= 1
		if self.live > 0:
			self.win.blit(self.img_hit, (self.x, self.y) )
