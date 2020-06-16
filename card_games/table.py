from dataclasses import dataclass
import os

import pygame

from card_games.builders import build_exit_button
from card_games.card import Card, CardState
from card_games.deck import Deck
from card_games.player import Player
from card_games.utils import (
        FONT_NEW_YORK, BLACK,
        CARD_BUFFER, HAND_START_X, HAND_START_Y,
        FACE_DOWN_START_X, FACE_DOWN_START_Y,
        FACE_UP_START_X, FACE_UP_START_Y
    )

CLOCK_TICK_RATE = 20

@dataclass
class GameTable:
    """ Used to manage the display of the table """
    screen: pygame.Surface
    deck: Deck
    pile: Deck
    title: str
    width: int
    height: int

    
    def __post_init__(self):
        pygame.display.set_caption(self.title)
        font_path = os.path.join('card_games/fonts', FONT_NEW_YORK)
        small_font = pygame.font.Font(font_path, 20)
        self.screen_size = (self.width, self.height)
        self.screen_center = (self.width/2, self.height/2)
        self.background = pygame.image.load(os.path.join('card_games/images','bkg.jpg')).convert()
        self.clock = pygame.time.Clock()
        self.exit_button = build_exit_button(self.screen, self.screen_size, small_font)
        self.pile.set_font(small_font)

        self.hand_start_x_y = (HAND_START_X, HAND_START_Y)
        self.face_up_start_x_y = (FACE_UP_START_X, FACE_UP_START_Y)
        self.face_down_start_x_y = (FACE_DOWN_START_X, FACE_DOWN_START_Y)
        self.card_buffer = CARD_BUFFER

    def render_common(self):
        """ Renders parts of the screen that remain consistant turn to turn """
        self.screen.fill(BLACK)
        self.screen.blit(self.background, [0,0])
        self.deck.render(self.screen)
        self.pile.render(self.screen)
        self.exit_button.render(self.screen)

    def render_player(self, player):
        player.render(self.screen)

    def render_pile(self, player):
        self.pile.render(self.screen)

    def next(self, player):
        self.render_common()
        self.render_player(player)
        self.refresh()

    def refresh(self):
        pygame.display.flip()       
