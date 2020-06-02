import pygame

from card_games import __version__
from card_games.card import Card, CardState
from card_games.deck import Deck
from card_games.game import GameManager
from card_games.player import Player
from card_games.utils import CardIdentity, CardSuit
from card_games.buttons import Button, ButtonLocation

def test_version():
    assert __version__ == '0.1.0'

def test_init():
	assert 0 == 0

####### TEST MODULES ######################

def test_card():
	
	mockCard = Card(CardIdentity.ACE, CardSuit.HEARTS)
	assert mockCard.suit == CardSuit.HEARTS
	assert mockCard.identity == CardIdentity.ACE
	assert mockCard.identity_value() == 1
	assert mockCard.state == CardState.IN_DECK
	assert mockCard.load_image_on_init == False

def test_player():
	p1 = Player(1)
	assert (p1.name == "Player1")
	assert (p1.player_id == 1)
	assert (type(p1.cards) == pygame.sprite.Group)


