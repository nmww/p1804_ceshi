import pygame
from plane_sprites import *

class PlaneGame(object):
	def __init__(self):
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)	
		self.clock = pygame.time.Clock()
		self.__create_sprites()
		


	def __create_sprites(self):
		bg1 = Background()
		bg2 = Background(True)
		self.back_group = pygame.sprite.Group(bg1,bg2)

		

	def start_game(self):
		print("游戏开始...")
		while  True:
			self.clock.tick(60)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()
			pygame.display.update()	
		

	def __event_handler(self):

		pass


	def __check_collide(self):
		pass
		
	
	def __update_sprites(self):
		self.back_group.update()
		self.back_group.draw(self.screen)

		
		

	@staticmethod		
	def game_over():
		pygame.quit
		exit()

if __name__ == '__main__':
	game = PlaneGame()
	game.start_game()		
