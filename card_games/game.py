from dataclasses import dataclass, field
from typing import List

from card_games.card import Card
from card_games.deck import Deck
from card_games.player import Player
from card_games.utils import CardIdentity, CardSuit

@dataclass
class GameManager:
	name: str = "Palace"
	num_decks: int = 1
	num_players: int = 2
	players: List[Player] = field(default_factory=list)
	width: int = 1120
	height: int = 720

	
	def __post_init__(self):
		self.deck = Deck(num_decks=self.num_decks)
		self.pile = Deck(pile=True)
		self.players = [Player(name=f'Player {i}', player_id=(i)) for i in range(self.num_players)]
		self.turn = 0
		total_turns = 0
		self.screen_size = (self.width, self.height)
		self.turn_jump = 1

	def deal_cards(self, cards_per_player):
		for _ in range(cards_per_player):
			for player in self.players:
				player.draw_card(self.deck.take())

	### TURNS #################################
	def next_turn(self, same_player=False):
		if not same_player:
			self.turn = (self.turn + self.turn_jump) % self.num_players
		total_turns += 1
		
	def reverse_direction(self):
		self.turn_jump *= -1

	def current_player(self):
		return self.players[self.turn]

	def make_card(self):
		self.test_card = Card(CardIdentity.KING, CardSuit.SPADES, load_image_on_init=True)

	def show_one_card(self, screen):	
		self.test_card.set_loc(500, 300)
		self.test_card.render(screen)


	######## Display ########################
	def display_players_cards(self):
		player = self.current_player()


	def display_pile(self):
		pass





