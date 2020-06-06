from dataclasses import dataclass, field
from typing import List

from card_games.card import Card, CardState
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
        self.total_turns = 0
        self.screen_size = (self.width, self.height)
        self.turn_jump = 1

    def deal_cards(self, to_hand, face_up=0, face_down=0):
        for _ in range(to_hand):
            for player in self.players:
                player.draw_to_hand(self.deck.take_from())
        for _ in range(face_up):
            for player in self.players:
                player.draw_face_up(self.deck.take_from())
        for _ in range(face_down):
            for player in self.players:
                player.draw_face_down(self.deck.take_from())

    def card_to_pile(self):
        player = self.current_player()
        if player.cards.card_is_selected():
            card = player.place_selected_card()
            card.state = CardState.PILE
            self.pile.place_on(card)
            return True
        return False

    ### TURNS #################################
    def next_turn(self, same_player=False):
        if not same_player:
            self.turn = (self.turn + self.turn_jump) % self.num_players
        self.total_turns += 1
        
    def reverse_direction(self):
        self.turn_jump *= -1

    def current_player(self):
        return self.players[self.turn]

    def make_card(self):
        self.test_card = Card(CardIdentity.KING, CardSuit.SPADES, load_image_on_init=True, state=CardState.FACE_DOWN)

    def show_one_card(self, screen):    
        self.test_card.set_loc(500, 300)
        self.test_card.render(screen)


