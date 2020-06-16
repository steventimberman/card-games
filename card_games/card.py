from dataclasses import dataclass
from enum import Enum
import os

import pygame
from pygame import Surface, RLEACCEL

from card_games.builders import display_card
from card_games.helpers import is_hovering, get_location
from card_games.utils import (CardIdentity, CardSuit, 
                    CARD_IMAGE_FILE_NAMES, 
                    WHITE, BLUE_TINT,
                    CARD_BORDER_X, CARD_BORDER_Y,
                    CARD_WIDTH, CARD_HEIGHT)

class CardState(Enum):
    DECK = "deck"
    PILE = "pile"
    HAND = "hand"
    FACE_DOWN = "face_down"
    FACE_UP = "face_up"
    ARCHIVED = "achived"


@dataclass
class Card():
    identity: CardIdentity
    suit: CardSuit
    load_image_on_init: bool = True
    state: CardState = CardState.DECK
    
    
    def __post_init__(self) -> None:
        if self.load_image_on_init:
            self.load_image()
        self.value = self.identity.value
        self.hovered = False
    
    def load_image(self):
        file_name = CARD_IMAGE_FILE_NAMES[(self.identity, self.suit)]
        full_path = os.path.join('card_games/images', file_name)
        try:
            image = pygame.image.load(full_path)
            image_back = pygame.image.load(os.path.join('card_games/images', "cardBack.png"))
        except pygame.error as message:
            print('Cannot load image:', name)
            raise SystemExit(message)
        self.image = image
        self.rect = image.get_rect()
        self.image_back = image_back
        self.rect_back = image_back.get_rect()

    ############ Sprite Methods ############

    def set_location(self, x, y): 
        self.rect = pygame.Rect(x,y, CARD_WIDTH, CARD_HEIGHT)
        self.rect_back = pygame.Rect(x,y, CARD_WIDTH, CARD_HEIGHT)


    def render(self, screen):
        image, rect = self.get_image_rect()
        display_card(screen, image, rect)


    def get_image_rect(self):
        if self.state == CardState.FACE_DOWN:
            image = self.image_back
            rect = self.rect_back
        else:
            image = self.image
            rect = self.rect
        return image, rect


    def __repr__(self):
        return f"{self.identity.value} of {self.suit.name}"

    def __str__(self):
        return f"{self.identity.value} of {self.suit.name}"
        

