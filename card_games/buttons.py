from dataclasses import dataclass
from enum import Enum
from typing import Tuple, Callable

import pygame

from card_games.helpers import is_hovering, get_location
from card_games.utils import BLACK


class ButtonLocation(Enum):
	TOP_LEFT = 1
	TOP_RIGHT = 2
	BOTTOM_LEFT = 3
	BOTTOM_RIGHT = 4


@dataclass
class Button(pygame.sprite.Sprite):
	button_loc: ButtonLocation
	display_size: Tuple[int, int]
	button_font: pygame.font.Font
	button_text: str
	color: Tuple[int, int, int]
	bright_color: Tuple[int, int, int]
	width: int
	height: int
	border:int = 50

	def __post_init__(self):
		self.display_width, self.display_height = self.display_size
		self.init_location()

		self.text_surface = self.button_font.render(self.button_text, True, BLACK)
		self.text_rect = self.text_surface.get_rect()
		self.text_rect.center = self.center

	def init_location(self):
		loc = self.button_loc
		top = (self.button_loc == ButtonLocation.TOP_LEFT 
				or self.button_loc == ButtonLocation.TOP_RIGHT
			)
		left = (self.button_loc == ButtonLocation.TOP_LEFT 
				or self.button_loc == ButtonLocation.BOTTOM_LEFT
			) 

		self.x_start = self.border if left else (self.display_width - self.width - self.border)
		self.y_start = self.border if top else (self.display_height - self.height - self.border)
		self.location = (self.x_start, self.y_start, self.width, self.height)
		self.center = ( (self.x_start+(self.width/2)), (self.y_start+(self.height/2)) )

	def clicked(self, mouse_point):
		if self.rect.collidepoint(mouse_point):
			return True
		return False

	def render(self, screen):
		color = self.color
		self.rect = pygame.draw.rect(screen, color, self.location) # draw button
		screen.blit(self.text_surface, self.text_rect) # add text
		
