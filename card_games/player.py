import pygame
from dataclasses import dataclass, field
from typing import List
from card_games.card import Card

@dataclass
class Player:
	player_id: int
	name: str = ""

	def __post_init__(self):
		self.cards = []
		if self.name == "":
			self.name = f"Player{self.player_id}"

	def draw_card(self, new_card):
		self.cards.append(new_card)

	def draw_multiple_cards(self, new_cards):
		self.cards += new_cards

	def place_card(self, card_index):
		current_card = self.cards.pop(card_index)
		return current_card




