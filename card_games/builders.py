import pygame

from card_games.buttons import Button, ButtonLocation
from card_games.helpers import is_hovering, get_location
from card_games.utils import (BRIGHT_RED, RED, BLACK,
                    WHITE, BLUE_TINT, CARD_PERSONAL_SPACE,
                    CARD_BORDER_X, CARD_BORDER_Y,
                    CARD_WIDTH, CARD_HEIGHT)


WIDTH_EXIT_BUTTON = 70
HEIGHT_EXIT_BUTTON = 50
BORDER_EXIT_BUTTON = 50

def build_exit_button(screen, screen_size, font):
    new_exit_button = Button(
            button_loc=ButtonLocation.TOP_RIGHT,
            display_size=screen_size,
            button_font=font,
            button_text='END',
            color=RED,
            bright_color=BRIGHT_RED,
            width=WIDTH_EXIT_BUTTON,
            height=HEIGHT_EXIT_BUTTON,
            border=BORDER_EXIT_BUTTON
        )
    return new_exit_button

def display_card(screen, image, rect):
    """ 
    Displays a card, highlights the card if the mouse is hovering
    over the card, and returns whether or not it was clicked 
    """
    x_rect = rect[0]
    y_rect = rect[1]
    loc = (x, y, width, height) = get_location(x_rect, y_rect, CARD_WIDTH, CARD_HEIGHT, CARD_BORDER_X, CARD_BORDER_Y)
    color = WHITE
    pygame.draw.rect(screen, color, loc, 0)
    new_image = pygame.transform.scale(image, (CARD_WIDTH, CARD_HEIGHT))
    x_image = x + CARD_BORDER_X
    y_image = y + CARD_BORDER_Y
    screen.blit(new_image, (x_image,y_image))


def display_card_text(screen, font, rect, text):
    x_start, y_start, *_ = rect
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect[0] = x_start
    text_rect[1] = y_start
    text_rect.center = ( (x_start+(CARD_WIDTH/2)), (y_start+(CARD_HEIGHT/2)) )
    screen.blit(text_surface, text_rect)