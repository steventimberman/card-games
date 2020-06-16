import pygame
from dataclasses import dataclass
from enum import Enum
import os

#### SCREEN #####
SCREEN_WIDTH = 1120  #1400x900
SCREEN_HEIGHT = 720

#### CARDS #####
CARD_WIDTH = 110
CARD_HEIGHT = 160
CARD_BORDER_X = 5
CARD_BORDER_Y = 4
CARD_PERSONAL_SPACE = 50

CARD_BUFFER = 60
HAND_START_X = 200
HAND_START_Y = SCREEN_HEIGHT/2
FACE_DOWN_START_X = 200
FACE_DOWN_START_Y = SCREEN_HEIGHT - ( (CARD_HEIGHT*2)/3 )
FACE_UP_START_X = FACE_DOWN_START_X + (CARD_BUFFER/4)
FACE_UP_START_Y = FACE_DOWN_START_Y - (CARD_HEIGHT/3)

# Font file names
FONT_NEW_YORK = "NewYork.ttf"

#### COLORS #####
GREEN = (0,200,0)
RED = (255,10,10)
BRIGHT_RED = (255, 100, 100)
BRIGHT_GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE_TINT = (215, 215, 255)

RULES_DICT_PALACE = {}

class EventType(Enum):
    EXIT = 1
    PLAY_CARD = 2
    NOT_ALLOWED = 3
    NO_EVENT = 4

class CardIdentity(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class CardSuit(Enum):
    CLUBS = 1
    SPADES = 2
    DIAMONDS = 3
    HEARTS = 4

CARD_IMAGE_FILE_NAMES = {
        (CardIdentity.TWO, CardSuit.CLUBS) : '2_of_clubs.png',
        (CardIdentity.TWO, CardSuit.SPADES) : '2_of_spades.png',
        (CardIdentity.TWO, CardSuit.DIAMONDS) : '2_of_diamonds.png',
        (CardIdentity.TWO, CardSuit.HEARTS) : '2_of_hearts.png',
        (CardIdentity.THREE, CardSuit.CLUBS) : '3_of_clubs.png',
        (CardIdentity.THREE, CardSuit.SPADES) : '3_of_spades.png',
        (CardIdentity.THREE, CardSuit.DIAMONDS) : '3_of_diamonds.png',
        (CardIdentity.THREE, CardSuit.HEARTS) : '3_of_hearts.png',
        (CardIdentity.FOUR, CardSuit.CLUBS) : '4_of_clubs.png',
        (CardIdentity.FOUR, CardSuit.SPADES) : '4_of_spades.png',
        (CardIdentity.FOUR, CardSuit.DIAMONDS) : '4_of_diamonds.png',
        (CardIdentity.FOUR, CardSuit.HEARTS) : '4_of_hearts.png',
        (CardIdentity.FIVE, CardSuit.CLUBS) : '5_of_clubs.png',
        (CardIdentity.FIVE, CardSuit.SPADES) : '5_of_spades.png',
        (CardIdentity.FIVE, CardSuit.DIAMONDS) : '5_of_diamonds.png',
        (CardIdentity.FIVE, CardSuit.HEARTS) : '5_of_hearts.png',
        (CardIdentity.SIX, CardSuit.CLUBS) : '6_of_clubs.png',
        (CardIdentity.SIX, CardSuit.SPADES) : '6_of_spades.png',
        (CardIdentity.SIX, CardSuit.DIAMONDS) : '6_of_diamonds.png',
        (CardIdentity.SIX, CardSuit.HEARTS) : '6_of_hearts.png',
        (CardIdentity.SEVEN, CardSuit.CLUBS) : '7_of_clubs.png',
        (CardIdentity.SEVEN, CardSuit.SPADES) : '7_of_spades.png',
        (CardIdentity.SEVEN, CardSuit.DIAMONDS) : '7_of_diamonds.png',
        (CardIdentity.SEVEN, CardSuit.HEARTS) : '7_of_hearts.png',
        (CardIdentity.EIGHT, CardSuit.CLUBS) : '8_of_clubs.png',
        (CardIdentity.EIGHT, CardSuit.SPADES) : '8_of_spades.png',
        (CardIdentity.EIGHT, CardSuit.DIAMONDS) : '8_of_diamonds.png',
        (CardIdentity.EIGHT, CardSuit.HEARTS) : '8_of_hearts.png',
        (CardIdentity.NINE, CardSuit.CLUBS) : '9_of_clubs.png',
        (CardIdentity.NINE, CardSuit.SPADES) : '9_of_spades.png',
        (CardIdentity.NINE, CardSuit.DIAMONDS) : '9_of_diamonds.png',
        (CardIdentity.NINE, CardSuit.HEARTS) : '9_of_hearts.png',
        (CardIdentity.TEN, CardSuit.CLUBS) : '10_of_clubs.png',
        (CardIdentity.TEN, CardSuit.DIAMONDS) : '10_of_diamonds.png',
        (CardIdentity.TEN, CardSuit.HEARTS) : '10_of_hearts.png',
        (CardIdentity.TEN, CardSuit.SPADES) : '10_of_spades.png',
        (CardIdentity.JACK, CardSuit.CLUBS) : 'jack_of_clubs.png',
        (CardIdentity.JACK, CardSuit.SPADES) : 'jack_of_spades.png',
        (CardIdentity.JACK, CardSuit.DIAMONDS) : 'jack_of_diamonds.png',
        (CardIdentity.JACK, CardSuit.HEARTS) : 'jack_of_hearts.png',
        (CardIdentity.QUEEN, CardSuit.CLUBS) : 'queen_of_clubs.png',
        (CardIdentity.QUEEN, CardSuit.SPADES) : 'queen_of_spades.png',
        (CardIdentity.QUEEN, CardSuit.DIAMONDS) : 'queen_of_diamonds.png',
        (CardIdentity.QUEEN, CardSuit.HEARTS) : 'queen_of_hearts.png',
        (CardIdentity.KING, CardSuit.CLUBS) : 'king_of_clubs.png',
        (CardIdentity.KING, CardSuit.SPADES) : 'king_of_spades.png',
        (CardIdentity.KING, CardSuit.DIAMONDS) : 'king_of_diamonds.png',
        (CardIdentity.KING, CardSuit.HEARTS) : 'king_of_hearts.png',
        (CardIdentity.ACE, CardSuit.CLUBS) : 'ace_of_clubs.png',
        (CardIdentity.ACE, CardSuit.SPADES) : 'ace_of_spades.png',
        (CardIdentity.ACE, CardSuit.DIAMONDS) : 'ace_of_diamonds.png',
        (CardIdentity.ACE, CardSuit.HEARTS) : 'ace_of_hearts.png'
    }


