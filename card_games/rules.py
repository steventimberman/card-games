from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List

from card_games.card import Card, CardIdentity, CardSuit
from card_games.helpers import check_type, check_type_many

class ClickType(Enum):
	NO_CLICK = 1
	EXIT_GAME = 2
	CARD_SELECT = 3

class Order(Enum):
	GREATER = 1
	EQUAL = 2
	LESS = 3

class RuleType(Enum):
	DEFAULT = 1
	CARD_IDENTITY = 2
	CARD_SUIT = 3
	ALL_CARDS = 5

@dataclass
class RuleAction:
	""" Stores rule attributes. Used to keep track of rules """
	follow_up: List[Order]
	turn_incr: int
	archive: bool
	alt_value: int
	substitude_card: bool = False


@dataclass
class RuleSet:
	"""
	A class for defining the rules of the game. 

	This class should be accessed by the Game class.

	Methods
	-------
	is_allowed(Card, Deck)
		Based on the rules, is a card allowed to be played when 
		pile is in the state given
	process(Card)
		takes in a card, returns RulesResponse object.

	"""
	follow_up: List[Order] = field(default_factory=list)
	turn_incr: int = 1
	allow_all: bool = False

	def __post_init__(self):

		self.default = RuleAction(
				follow_up=self.follow_up if self.follow_up else [Order.GREATER, Order.EQUAL], 
				turn_incr=self.turn_incr,
				archive=False,
				alt_value=None,
				substitude_card=False

			)
		self.identity_rules = dict()
		self.suit_rules = dict()
		self.all_cards_rules = dict()


	def new_rule(self, rule_type, key, follow_up=None,
				 turn_incr=None, achive_pile=False, 
				 alt_value=None, substitude_card=False, in_a_row=None):

		rule_dict = None

		if rule_type == RuleType.CARD_IDENTITY:
			check_type(key, CardIdentity)
			rule_dict = self.identity_rules

		elif rule_type == RuleType.CARD_SUIT:
			check_type(key, CardSuit)
			rule_dict = self.suit_rules

		elif rule_type == RuleType.ALL_CARDS:
			check_type_many(key, [CardIdentity, CardSuit], var_is_type=True)
			rule_dict = self.all_cards_rules

		else:
			raise Exception("RuleType is invalid: {rule_type}")

		rule_dict[key] = RuleAction(
				follow_up=follow_up, 
				turn_incr=turn_incr,
				archive=archive,
				alt_value=alt_value,
				sub_card=sub_card,
				in_a_row=in_a_row
			)

	def is_allowed(self, card, pile):
		if self.allow_all or len(self.pile) == 0:
			return True
		top_card = pile.get_top_card()
		actions = self.actions

		return False

	def check_order(self):
		pass



	def process(self, card, pile):
		if self.allow_all:
			return True

	def actions(self, card):
		actions_card = [fn(card) for fn in [get_identity_action, get_suit_action] if fn(card)]
		actions_all = [fn() for fn in [get_all_identity_action, get_all_suit_action] if fn()]

		actions = actions_card + actions_all

		return actions

	def get_identity_action(self, card):
		identity = card.identity
		action = self.identity_rules.get(identity, None)
		return action

	def get_suit_action(self, card):
		suit = card.suit
		action = self.suit_rules.get(suit, None)
		return action

	def get_all_identity_action(self):
		action = self.all_cards_rules.get(CardIdentity, None)
		return action

	def get_all_suit_action(self):
		action = self.all_cards_rules.get(CardSuit, None)
		return action


def is_n_straight(card_identity, pile, n):
	if not pile or pile[-1].identity != card_identity:
		return False
	if n == 1:
		return True
	return is_n_straight(card_identity, pile[:-1], n-1)


