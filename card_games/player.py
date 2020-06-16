from dataclasses import dataclass, field
from typing import List, Callable

import pygame

from card_games.card import Card, CardState
from card_games.utils import (
	    CARD_WIDTH, CARD_BUFFER, HAND_START_X, HAND_START_Y,
		FACE_DOWN_START_X, FACE_DOWN_START_Y,
		FACE_UP_START_X, FACE_UP_START_Y
	)

@dataclass
class CardGroup:
	start_x: int
	start_y: int
	state: CardState

	num_cards: int = 0
	updated: bool = True
	cards: List[Card] = field(default_factory=list)

	def add(self, card):
		self.cards.append(card)
		card.state = self.state
		x = self.start_x + self.num_cards * CARD_WIDTH + self.num_cards * CARD_BUFFER
		y = self.start_y
		card.set_location(x, y)
		self.num_cards += 1

	def give(self, card):
		for i, card_i in enumerate(self.cards):
			if card == card_i:
				self.num_cards -= 1
				self.updated = False
				return self.cards.pop(i)
		return None

	def render(self, screen):
		for card in self.cards:
			card.render(screen)

	def update(self):
		for i, card in enumerate(self.cards):
			x = self.start_x + i * CARD_WIDTH + i * CARD_BUFFER
			y = self.start_y
			card.set_location(x,y)
		self.updated = True

@dataclass
class Player:
	"""
	class to represent player of game

	"""
	player_id: int
	name: str = ""

	def __post_init__(self):
		self.hand = CardGroup(HAND_START_X, HAND_START_Y, CardState.HAND)
		self.face_up = CardGroup(FACE_UP_START_X, FACE_UP_START_Y, CardState.FACE_UP)
		self.face_down = CardGroup(FACE_DOWN_START_X, FACE_DOWN_START_Y, CardState.FACE_DOWN)

		self.groups = [self.hand, self.face_up, self.face_down]

		if self.name == "":
			self.name = f"Player{self.player_id}"

	##### GENERAL ###############################

	def add(self, card, state):
		if state == CardState.HAND:
			self.hand.add(card)
		elif state == CardState.FACE_UP:
			self.face_up.add(card)
		elif state == CardState.FACE_DOWN:
			self.face_down.add(card)
		else:
			raise Exception("Invalid card state")

	def give(self, card):
		group = self.get_group(card)
		return group.give(card)

	def get_group(self, state):
		if state == CardState.HAND:
			return self.hand
		elif state == CardState.FACE_UP:
			return self.face_up
		elif state == CardState.FACE_DOWN:
			return self.face_down
		else:
			raise Exception("Invalid card state")

	def update_group(self, card_state):
		self.get_group(card_state)
		group.update()

	#### DISPLAY ###################################

	def render(self, screen):
		for group in self.groups:
			group.update()
			group.render(screen)

	def clicked(self, mouse_point):
		for group in self.groups:
			for card in group.cards:
				if card.rect.collidepoint(mouse_point):
					return_card = group.give(card)
					return return_card
		return None

