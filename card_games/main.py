import pygame
import os, sys

from card_games.game import GameManager
from card_games.rules import RuleSet, ClickType, Order
from card_games.utils import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, EventType

def main():

    pygame.init()

    try:        
        run()

    except pygame.error as message:
        raise SystemExit(message)
        pygame.display.quit()
        pygame.quit()

    if pygame.get_init():
        pygame.display.quit()
        pygame.quit()

def run():
    
    rules = RuleSet(allow_all=True)
    game = GameManager(title="Palace", rules=rules, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

    game.deal(5,5,5)
    

    game.table.render_common()
    game.table.render_player(game.current_player)

    game.table.refresh()

    while (game.run == True):
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                click_event = game.click(mouse_pos)
                if click_event == EventType.EXIT:
                    break

                elif click_event == EventType.PLAY_CARD:
                    game.next()
                    game.table.next(game.current_player)
                    break


            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

