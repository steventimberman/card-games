from dataclasses import dataclass, field
from typing import List

import pygame

from card_games.card import Card, CardState
from card_games.utils import (
	    CARD_WIDTH, CARD_BUFFER, HAND_START_X, HAND_START_Y,
		FACE_DOWN_START_X, FACE_DOWN_START_Y,
		FACE_UP_START_X, FACE_UP_START_Y
	)

@dataclass
class PlayerCards:
	hand: List[Card] = field(default_factory=list)
	face_up: List[Card] = field(default_factory=list)
	face_down: List[Card] = field(default_factory=list)
	selected_cards: Card = field(default_factory=list)

	def __post_init__(self):
		self.update_hand_flag = False
		self.update_face_up_flag = False
		self.update_face_down_flag = False
		self.location_to_list = {
			CardState.HAND: {"list": self.hand, "flag": self.update_hand_flag},
			CardState.FACE_UP: {"list": self.face_up, "flag": self.update_face_up_flag},
			CardState.FACE_DOWN: {"list": self.face_down, "flag": self.update_face_down_flag}
		}
		
		

#### CARD LOCATION #######################

	def init_card_locations(self, hand_start_x_y, face_up_start_x_y, face_down_start_x_y, buffer):
		start_x_y_list = [hand_start_x_y, face_up_start_x_y, face_down_start_x_y]
		card_states = [CardState.HAND, CardState.FACE_UP, CardState.FACE_DOWN]
		
		for (x, y), state in zip(start_x_y_list, card_states):
			self.update_card_locations(state,x, y, buffer)
				
	def update_card_locations(self, card_state, start_x, start_y, buffer):
		list_to_update = self.get_location_list(card_state)
		for i, card in enumerate(list_to_update):
			x = start_x + (CARD_WIDTH * i) + (buffer * i)
			y = start_y
			card.set_location(x, y)
		self.set_location_flag(card_state, False)

#### SELECTER #######################

	def card_is_selected(self):
		"""
		Checks all cards clicked attribute.
		If one is clicked, remove from that card list,
		set as self.selected_card, set update flag for list as True,
		sets clicked attribute to false and return True.
		"""
		card_states = [CardState.HAND, CardState.FACE_UP, CardState.FACE_DOWN]
		card_lists = [(card_state, self.get_location_list(card_state)) for card_state in card_states]
		for card_state, card_list in card_lists:
			for i, card in enumerate(card_list):
				if card.clicked:
					self.selected_cards.append(card_list.pop(i))
					self.set_location_flag(card_state, True)
					card.clicked = False
					return True
		return False

#### HELPERS ################

	def get_location_list(self, card_state):
		return self.location_to_list[card_state]["list"]

	def get_location_flag(self, card_state):
		return self.location_to_list[card_state]["flag"]

	def set_location_list(self, card_state, set_to):
		if type(set_to) != bool:
			raise Exception("set_to type must be bool")
		self.location_to_list[card_state]["list"] = set_to

	def set_location_flag(self, card_state, set_to):
		if (type(set_to) != bool) or (card_state not in self.location_to_list):
			raise Exception("set_to type must be bool")
		self.location_to_list[card_state]["flag"] = set_to

	def all_cards(self):
		return self.hand + self.face_up + self.face_down

	def count(self):
		return len(self.in_hand + self.ace_up + self.face_down)

@dataclass
class Player:
	player_id: int
	name: str = ""

	def __post_init__(self):
		self.cards = PlayerCards()
		if self.name == "":
			self.name = f"Player{self.player_id}"

##### HELPERS ###############################

	# def has_selected_card(self):
	# 	return len(self.cards.selected_cards) > 0

##### DRAW CARD ###############################
	def draw_to_hand(self, new_card):
		new_card.state = CardState.HAND
		self.cards.hand.append(new_card)

	def draw_face_up(self, new_card):
		new_card.state = CardState.FACE_UP
		self.cards.face_up.append(new_card)

	def draw_face_down(self, new_card):
		new_card.state = CardState.FACE_DOWN
		self.cards.face_down.append(new_card)

##### PLACE CARD ###############################

	def place_selected_card(self):
		if len(self.cards.selected_cards) == 0:
			raise Exception("No card selected")
		card = self.cards.selected_cards.pop()
		return card

	def place_from_hand(self, card_index):
		current_card = self.cards.hand.pop(card_index)
		return current_card

	def place_from_face_up(self, card_index):
		current_card = self.cards.face_up.pop(card_index)
		return current_card

	def place_from_face_down(self, card_index):
		current_card = self.cards.face_down.pop(card_index)
		return current_card

#### DISPLAY ###################################

	def render_cards(self, screen):
		for card in self.cards.all_cards():
			card.render(screen)

