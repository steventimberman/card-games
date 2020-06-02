from dataclasses import dataclass
import os

import pygame

from card_games.buttons import create_end_button
from card_games.card import Card

CLOCK_TICK_RATE = 20

@dataclass
class GameTable:
	""" Used to manage the display of the table """
	screen: pygame.Surface
	title: str
	width: int
	height: int
	
	def __post_init__(self):
		pygame.display.set_caption(self.title)
		small_font = pygame.font.Font("freesansbold.ttf", 20)
		self.screen_size = (self.width, self.height)
		self.background = pygame.image.load(os.path.join('card_games/images','bkg.jpg')).convert()
		self.clock = pygame.time.Clock()
		self.end_button = create_end_button(self.screen, self.screen_size, small_font)


	def set_display(self):
		self.screen.fill((0,128,0))
		self.screen.blit(self.background, [0,0])
		self.end_button.draw(pygame.mouse.get_pos())

	def end_button_clicked(self):
		return self.end_button.clicked

	def update_display(self):
		pygame.display.update()
		pygame.display.flip()
