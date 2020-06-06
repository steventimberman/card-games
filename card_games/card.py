from dataclasses import dataclass
from enum import Enum
import os

import pygame
from pygame import Surface, RLEACCEL

from card_games.builders import display_card
from card_games.helpers import track_mouse, get_location
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


@dataclass
class Card(pygame.sprite.Sprite):
    identity: CardIdentity
    suit: CardSuit
    load_image_on_init: bool = False
    state: CardState = CardState.DECK
    
    
    def __post_init__(self) -> None:
        if self.load_image_on_init:
            self.load_image()
        self.clicked = False
        
    
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

    def identity_value(self) -> int:
        return self.identity.value

    ############ Sprite Methods ############

    def set_location(self, x, y):
        self.rect[0] = self.rect_back[0] = x
        self.rect[1] = self.rect_back[1] = y

    def update(self):
        pass

    def render(self, screen):
        if self.state == CardState.FACE_DOWN:
            image = self.image_back
            rect = self.rect_back
        else:
            image = self.image
            rect = self.rect
        self.clicked = display_card(screen, image, rect)
        
        

