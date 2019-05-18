import pygame as pyg
from bullet import Bullet


class Ship():
	
	def __init__(self, win):
		self.win = win
		self.live = 5
		self.speed = 10
		self.x = 225
		self.y = 525
		self.img = pyg.image.load("ship.png")
		self.hit_img = pyg.image.load("hit.png")
		self.win.blit(self.img, (self.x, self.y))
		#pyg.draw.rect(self.win, (0, 0, 255), (50, 50, self.weigth, self.height))
	def action(self, key):
		if key[pyg.K_LEFT] and self.x >5:
			self.x -=self.speed
		if key[pyg.K_RIGHT] and self.x < 500 - 37  - 5:
			self.x +=self.speed
		self.win.blit(self.img, (self.x, self.y))
		#pyg.draw.rect(self.win, (0, 0, 255), (self.x, self.y, self.weigth, self.height))
		if key[pyg.K_SPACE]:
			bullet = Bullet(self.x+15, self.y-4, self.win, 15)
			return bullet
	def hit(self):
		self.live -=1
		self.win.blit(self.hit_img, (self.x, self.y))
		if self.live == 0:
			return "game over"
		




