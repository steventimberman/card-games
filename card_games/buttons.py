from dataclasses import dataclass
from enum import Enum
from typing import Tuple, Callable
import pygame
from .utils import RED, BRIGHT_RED, BLACK



class ButtonLocation(Enum):
	TOP_LEFT = 1
	TOP_RIGHT = 2
	BOTTOM_LEFT = 3
	BOTTOM_RIGHT = 4


@dataclass
class Button:
	screen: pygame.Surface
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
		self.clicked = False
		self.display_width, self.display_height = self.display_size
		self.init_location()

		self.text_surface = self.button_font.render(self.button_text, True, BLACK)
		self.text_rect = self.text_surface.get_rect()
		self.text_rect.center = self.center

	def init_location(self):
		loc = self.button_loc

		if loc == ButtonLocation.TOP_LEFT:
			self.location = (
				self.border, self.border,
				self.width, self.height
				)
		elif loc == ButtonLocation.TOP_RIGHT:
			self.location = (
				(self.display_width - self.width - self.border), self.border,
				self.width, self.height
				)
		elif loc == ButtonLocation.BOTTOM_LEFT:
			self.location = (
				self.border, (self.display_height - self.height - self.border),
				self.width, self.height
				)
		elif loc == ButtonLocation.BOTTOM_RIGHT:
			self.location = (
				self.border, (self.display_height - self.height - self.border),
				self.width, self.height
				)
		else:
			raise Exception("Button doesn't have a defined location")

		self.width_start = self.location[0]
		self.height_start = self.location[1]
		self.width_end = self.width_start + self.width
		self.height_end = self.height_start + self.height
		self.center = ( (self.width_start+(self.width/2)), (self.height_start+(self.height/2)) )

	def draw(self, mouse_location):
		color = self.color
		mouse_w, mouse_h = mouse_location
		if (self.width_start <= mouse_w <= self.width_end and self.height_start <= mouse_h <= self.height_end):
			color = self.bright_color
			self.clicked = pygame.mouse.get_pressed()[0] == 1
		pygame.draw.rect(self.screen, color, self.location) # draw button
		self.screen.blit(self.text_surface, self.text_rect) # add text
		


def create_end_button(screen, screen_size, font):
	new_end_button = Button(
			screen=screen,
			button_loc=ButtonLocation.TOP_RIGHT,
			display_size=screen_size,
			button_font=font,
			button_text='END',
			color=RED,
			bright_color=BRIGHT_RED,
			width=70,
			height=50,
			border=50
		)
	return new_end_button





