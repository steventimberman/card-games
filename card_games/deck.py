from dataclasses import dataclass, field
from typing import List
import random
from .card import Card
from .utils import CardIdentity, CardSuit


@dataclass
class Deck:
    cards: List[Card] = field(default_factory=list)
    init_shuffle = True
    pile: bool = False
    num_decks: int = 1

    def __post_init__(self):
        self.cards = [] if self.pile else [
            Card(identity=identity_i,suit=suit_j) 
            for identity_i in list(CardIdentity) 
            for suit_j in list(CardSuit) 
            for i in range(self.num_decks)
        ]
        if self.init_shuffle: 
            self.shuffle()

    def take(self, bottom=False) -> Card:
        ''' Removes card from top of deck, unless bottom is true, and returns it '''
        card_to_remove = 0 if bottom else -1
        return cards.pop(card_to_remove)

    def put(self, new_card, bottom=False) -> None:
        ''' Places new card on top of deck, unless cards  '''
        if bottom:
            cards.insert(0, new_card)
        else:
            cards.append(new_card)

    def see_top_card(self):
        ''' Meant for case pile=True, view top card '''
        return self.cards[-1]

    def shuffle(self):
        self.cards = random.shuffle(self.cards)

    def __len__(self):
        return len(cards)

    def __add__(self, x):
        if isinstance(x, Deck):
            self.cards += x.cards
        else:
            raise Exception("Can only add decks together")
        
