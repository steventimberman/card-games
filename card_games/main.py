import pygame
import os, sys

from card_games.game import GameManager
from card_games.table import GameTable
from card_games.utils import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE

def quit_game():
	pygame.display.quit()
	pygame.quit()


def main():
	pygame.init()
	game = GameManager(name="Palace", width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
	screen = pygame.display.set_mode(game.screen_size)
	table = GameTable(
		screen=screen, title=game.name, 
		width=game.width, height=game.height,
		deck=game.deck, pile=game.pile,
	)

	game.deal_cards(5,5, 5)
	table.init_players(game.players)
	
	run = True
	while run:
		pygame.time.delay(100)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		current_player = game.current_player()

		table.set()
		table.display_player_cards(current_player)
		next_turn = game.card_to_pile()
		if next_turn:
			game.next_turn()

		run ^= table.end_button_clicked()
		table.update()




	pygame.quit()


