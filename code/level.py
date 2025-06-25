#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:

    # game_mode == menu_return
    def __init__(self, window, name, game_mode):
        self.window = window
        self.windows = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                # chamando movimento da classe background
                ent.move()
            pygame.display.flip()
        pass
