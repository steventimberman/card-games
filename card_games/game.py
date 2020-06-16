from dataclasses import dataclass, field
import os
from typing import List, Tuple

import pygame

from card_games.card import Card, CardState
from card_games.deck import Deck
from card_games.player import Player
from card_games.table import GameTable
from card_games.rules import RuleSet, ClickType
from card_games.utils import (CardIdentity, CardSuit, EventType,
        FONT_NEW_YORK, 
        CARD_BUFFER, HAND_START_X, HAND_START_Y,
        FACE_DOWN_START_X, FACE_DOWN_START_Y,
        FACE_UP_START_X, FACE_UP_START_Y, BLACK
    )


@dataclass
class GameManager:
    title: str
    rules: RuleSet
    num_decks: int = 1
    num_players: int = 2
    players: List[Player] = field(default_factory=list)
    width: int = 1120
    height: int = 720

    
    def __post_init__(self):
        self.run = True
        self.deck = Deck(num_decks=self.num_decks)
        self.pile = Deck(pile=True)
        self.players = [Player(name=f'Player {i}', player_id=(i)) for i in range(self.num_players)]
        self.turn = 0
        self.total_turns = 0
        self.turn_jump = 1
        self.next_turn = False
        self.current_player = self.players[self.turn]
        self.screen_size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption(self.title)

        self.table = GameTable(
                    screen=self.screen, title=self.title, 
                    width=self.width, height=self.height,
                    deck=self.deck, pile=self.pile,
                )

    def click(self, mouse_pos):
        """ Returns tuple (was_clicked, click_type) """
        clicked_card = self.current_player.clicked(mouse_pos)
        if clicked_card:
            if self.process_card(clicked_card):
                return EventType.PLAY_CARD
            return EventType.NOT_ALLOWED
            

        exit_button_clicked = self.table.exit_button.clicked(mouse_pos)
        if exit_button_clicked:
            self.run = False
            return EventType.EXIT

        return EventType.NO_EVENT

    def process_card(self, card):
        player = self.current_player
        if self.rules.is_allowed(card, self.pile):
            card.state = CardState.PILE
            self.pile.add(card)
            return True
        else:
            player.add(card, card.state)
            return False

#### Move Cards ####################

    def deal(self, to_hand=0, face_up=0, face_down=0):
        for _ in range(to_hand):
            for player in self.players:
                player.hand.add(self.deck.give())
        for _ in range(face_up):
            for player in self.players:
                player.face_up.add(self.deck.give())
        for _ in range(face_down):
            for player in self.players:
                player.face_down.add(self.deck.give())

    ### TURNS #################################

    def next(self, same_player=False):
        if not same_player:
            self.turn = (self.turn + self.turn_jump) % self.num_players
        self.total_turns += 1
        self.current_player = self.players[self.turn]
        
    def reverse_direction(self):
        self.turn_jump *= -1
