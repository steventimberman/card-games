from dataclasses import dataclass, field
import os
import random

from typing import List

import pygame


from card_games.card import Card
from card_games.builders import display_card, display_card_text
from card_games.utils import (CardIdentity, CardSuit,  
                    WHITE, BLUE_TINT, CARD_PERSONAL_SPACE,
                    CARD_BORDER_X, CARD_BORDER_Y,
                    CARD_WIDTH, CARD_HEIGHT)


@dataclass
class Deck:

    pile: bool = False
    init_shuffle:bool = True
    num_decks: int = 1
    cards: List[Card] = field(default_factory=list)

    def __post_init__(self):
        self.cards = [] if self.pile else [
            Card(identity=identity_i,suit=suit_j, load_image_on_init=True) 
            for identity_i in list(CardIdentity) 
            for suit_j in list(CardSuit) 
            for i in range(self.num_decks)
        ]
        if self.init_shuffle and not self.pile: 
            self.shuffle()
        self.load_image()
        self.set_loc()
        self.font = None

    def load_image(self):
        """ Loads specifically the image of the back of the card """
        
        file = "back.png" if self.pile else "cardBack.png"
        try:
            image = pygame.image.load(os.path.join('card_games/images', file))
        except pygame.error as message:
            print('Cannot load deck images')
            raise SystemExit(message)
        self.image, self.rect = image, image.get_rect()

    def set_font(self, font):
        self.font = font

    def shuffle(self):
        random.shuffle(self.cards)


    def take_from(self, bottom=False) -> Card:
        ''' Removes card from top of deck, unless bottom is true, and returns it '''
        card_to_remove = 0 if bottom else -1
        return self.cards.pop(card_to_remove)

    def place_on(self, new_card, bottom=False) -> None:
        ''' Places new card on top of deck, unless cards  '''
        if bottom:
            self.cards.insert(0, new_card)
        else:
            self.cards.append(new_card)

    def top_card(self):
        ''' Meant for case self.pile=True, view top card '''
        return self.cards[-1]

    def set_loc_pile(self):
        self.rect[0] = CARD_WIDTH + (2 * CARD_PERSONAL_SPACE)
        self.rect[1] = CARD_PERSONAL_SPACE
        
    def set_loc_deck(self):
        self.rect[0] = CARD_PERSONAL_SPACE
        self.rect[1] = CARD_PERSONAL_SPACE

    def set_loc(self):
        if self.pile:
            self.set_loc_pile()
        else:
            self.set_loc_deck()

    def render(self, screen):
        empty_pile = False
        if self.pile and self.cards:
            image = self.top_card().image
            rect = self.rect
        else:
            image = self.image
            rect = self.rect
            empty_pile = self.pile
        display_card(screen, image, rect)
        if empty_pile and self.font:
            empty_pile_message = "Empty Pile"
            display_card_text(screen, self.font, rect, empty_pile_message)

    def __len__(self):
        return len(self.cards)

    def __add__(self, x):
        if isinstance(x, Deck):
            self.cards += x.cards
        else:
            raise Exception("Can only add decks together")
        
