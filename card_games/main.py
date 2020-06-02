import pygame
import os, sys

from card_games.game import GameManager
from card_games.table import GameTable
from card_games.utils import WHITE

def quit_game():
	pygame.display.quit()
	pygame.quit()


def main():
	pygame.init()
	game = GameManager(name="Palace", width=1120, height=720) #1400x900
	screen = pygame.display.set_mode(game.screen_size)
	table = GameTable(screen=screen, title=game.name, width=game.width, height=game.height)

	game.make_card()
	
	run = True
	while run:
		pygame.time.delay(100)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		table.set_display()
		game.show_one_card(screen)

		run ^= table.end_button_clicked()
		table.update_display()




	pygame.quit()


