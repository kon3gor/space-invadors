import pygame as pyg

class Bullet():

    def __init__(self, x, y, win, speed):
        self.win = win
        self.speed = speed
        self.h = 5
        self.w = 5
        self.x = x
        self.y = y
        pyg.draw.rect(win, (0,0,255), (x, y, self.w, self.h) )

    def shot(self, x, y):
        pyg.draw.rect(self.win, (0,0,255), (x, y, self.w, self.h))
        
            


