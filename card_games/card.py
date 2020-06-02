from dataclasses import dataclass
from enum import Enum
import os

import pygame
from pygame import Surface, RLEACCEL

from .utils import CardIdentity, CardSuit, CARD_IMAGE_FILE_NAMES, WHITE


class CardState(Enum):
    IN_DECK = 1
    IN_PILE = 2
    IN_HAND = 3
    ON_TABLE_FACE_DOWN = 4
    ON_TABLE_FACE_UP = 5


@dataclass
class Card(pygame.sprite.Sprite):
    identity: CardIdentity
    suit: CardSuit
    load_image_on_init: bool = False
    state: CardState = CardState.IN_DECK
    
    
    def __post_init__(self) -> None:
        if self.load_image_on_init:
            self.load_image()
        
    
    def load_image(self):
        file_name = CARD_IMAGE_FILE_NAMES[(self.identity, self.suit)]
        full_path = os.path.join('card_games/images', file_name)
        try:
            image = pygame.image.load(full_path)
        except pygame.error as message:
            print('Cannot load image:', name)
            raise SystemExit(message)
        self.image = image
        self.rect = image.get_rect()

    def identity_value(self) -> int:
        return self.identity.value

    def flip_card(self) -> None:
        ''' Flips the boolean self.face_up '''
        self.face_up ^= True

    ############ Sprite Methods ############

    def set_loc(self, x, y):
        self.rect[0] = x
        self.rect[1] = y

    def update(self):
        pass

    def render(self, screen):
        w = 130
        h = 181
        x = self.rect[0]
        y = self.rect[1]
        pygame.draw.rect(screen, WHITE, (x - 5, y - 4, w + 10, h + 8), 0)
        newIMG = pygame.transform.scale(self.image, (w, h))
        screen.blit(newIMG, (x,y))
        # screen.blit(self.image, (self.rect[0], self.rect[1]))

        

