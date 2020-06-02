from dataclasses import dataclass
from utils import DirectionChange, Specialty
from typing import Dict

@dataclass
class Rules:
	"""
	A class for defining the rules of the game. 

	This class should be accessed by the Game class.

	Methods
	-------
	process(Card)
		takes in a card, returns RulesResponse object.

	define_rules(CardIdentity, *Specialty)
		defines a specialty for a given card identity
	"""
	specialties: Dict[CardIdentity, Specialty] = field(default_factory=dict)
	four_straight: Specialty = Specialty.REGULAR

	def process(self, card, pile_of_cards):
		card_identity = card.identity
		specialty = self.specialties.get(card_identity, Specialty.REGULAR)


def is_four_straight(card, pile_of_cards):
	if len(pile_of_cards) < 3:
		return False
	for pile_card in pile_of_cards[-3:]:
		if card.identity != pile_card.identity:
			return False
	return True







