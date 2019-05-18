import pygame as pyg

class Barrier():
	def __init__(self, x, y, win):
		self.pixels = []
		self.win = win
		self.h = 5
		self.w = 5
		prev = x
		for i in range(100):
			pyg.draw.rect(win, (0, 255, 0), (x, y, self.w, self.h))
			x += self.w
			if i%20 == 0:
				y+= self.h
				x = prev
			self.pixels.append((x, y))

	def draw(self):
		for i in range(100):
			if self.pixels[i][0] != -10: 
				pyg.draw.rect(self.win, (0, 255, 0), (self.pixels[i][0],self.pixels[i][1] , self.w, self.h))
