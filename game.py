import pygame
from ship import *
from barrier import Barrier
from enemy import Enemy


class Game():

	def __init__(self):
		pygame.init()
		self.lifes = [
			pyg.image.load("lifes.png"),
			pyg.image.load("lifes.png"),
			pyg.image.load("lifes.png"),
			pyg.image.load("lifes.png"),
			pyg.image.load("lifes.png")
		]
		self.isgame = True
		self.moving_flag = True
		self.win = pygame.display.set_mode((500, 600))
		pygame.display.set_caption("Space Invadors")
		self.ship = Ship(self.win)
		self.barrier_1 = Barrier(100, 450,self.win)	
		self.barrier_2 = Barrier(300, 450,self.win)	
		self.enemys = [Enemy(self.win, x, 100 ) for x in range(30, 425, 55)]
		self.enemys += [Enemy(self.win, x, 225 ) for x in range(20, 435, 45)]
		self.count = 0

	def get_min_y(self, barrier, xc):
		mas = [(y if xc==x else 700) for x, y in barrier]
		try:
			return min(  mas )
		except Exception as e:
			print(e)

	def find_enemy(self, enemyes):
		mi = 550
		mx = 0
		for enemy in enemyes:
			if enemy.x > mx: mx = enemyes.index(enemy)
			if enemy.x < mi: mi = enemyes.index(enemy)
		return (mx, mi)

	def run(self):
		bullets = []
		ship_bullets = []
		while self.isgame:
			pygame.time.delay(70)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.isgame = False

			keys = pygame.key.get_pressed()
	
			self.win.fill((0,0,0))
			tmp = self.ship.action(keys)
			self.barrier_1.draw()
			self.barrier_2.draw()
			font = pygame.font.SysFont(None, 40)
			text = font.render(f"Score: {self.count}", True, (255, 255, 255))
			self.win.blit(text, (160, 10) )
			i = 0
			for x in range(5, (23+5)*len(self.lifes), 28):
				self.win.blit(self.lifes[i], (x, 2 ))
				i+=1
			max_en, min_en = self.find_enemy( self.enemys )
			if self.enemys[max_en].x + 5 < 450 and self.moving_flag:
				for enemy in self.enemys:
					tmp_2 = enemy.move(5)
					if tmp_2 and len(bullets) < 30:
						bullets.append(tmp_2)
			elif self.enemys[min_en].x - 5 > 10:
				for enemy in self.enemys:
					tmp_2 = enemy.move(-5)
					if tmp_2 and len(bullets) < 30:

						bullets.append(tmp_2)
				self.moving_flag = False
			else:
				self.moving_flag = True
				for enemy in self.enemys:
					tmp_2 = enemy.move(0)
					if tmp_2 and len(bullets) < 30:
						bullets.append(tmp_2)
			if tmp and len(bullets) < 15:
				bullets.append(tmp)
				
			for bullet in bullets:
				try:
					bullets.index(bullet)
				except:
					continue
				bullet.shot(bullet.x, bullet.y)
				matrix = [self.barrier_1.pixels, self.barrier_2.pixels]
				for pix in range( len( matrix[0] ) ):
					min_y_1 = self.get_min_y(matrix[0], matrix[0][pix][0])
					min_y_2 = self.get_min_y(matrix[1], matrix[1][pix][0])
					try:
						bullets.index(bullet)
					except:
						continue
					if matrix[0][pix][0] == bullet.x and bullet.y in range(450, 550) and bullet.speed < 0:
						try:
							bullets.pop(bullets.index(bullet))
							self.barrier_1.pixels[self.barrier_1.pixels.index( (matrix[0][pix][0],  min_y_1) )] = (-10, 650)
						except:
							pass
					elif matrix[1][pix][0] == bullet.x and bullet.y in range(450, 550) and bullet.speed < 0:
						try:
							bullets.pop(bullets.index(bullet))
							self.barrier_2.pixels[self.barrier_2.pixels.index( (matrix[1][pix][0], min_y_1) )] = (-10, 650)
						except:
							pass

				for enemy in self.enemys:
					if bullet.x in range(enemy.x, enemy.x + 26 ) and bullet.y in range(enemy.y, enemy.y + 26):
						try:
							index = bullets.index(bullet)
						except:
							continue
						if bullet.speed > 0:
							enemy.hit()
							if enemy.live <= 0:
								self.enemys.pop( self.enemys.index(enemy) )
								self.count+=1
							bullets.pop( bullets.index(bullet) )

				if self.count == 18:
					self.end()
							
				if bullet.x in range(self.ship.x, self.ship.x + 37 ) and bullet.y in range(self.ship.y, self.ship.y + 52):
					try:
						index = bullets.index(bullet)
					except:
						continue
					tmp = self.ship.hit()
					self.lifes.pop(-1)
					bullets.pop( bullets.index(bullet) )
					if tmp == "game over":
						self.end()

				if bullet.y < 600 and bullet.y > 0:
					bullet.y -=bullet.speed
				else:
					bullets.pop(bullets.index(bullet))

			
			pygame.display.update()



	def end(self):
		self.win.fill((0,0,0))
		font = pygame.font.SysFont(None, 40)
		text = font.render("GAME OVER", True, (255, 50, 50))
		self.win.blit(text, (160, 300) )
		pygame.display.update()
		pygame.time.wait(2000)
		pygame.quit()




if __name__ == "__main__":
	game = Game()
	game.run()
	pygame.quit()