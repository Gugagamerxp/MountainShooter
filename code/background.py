#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import WIN_WIDTH, ENTITY_SPEED
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    # Movimento do background.
    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        # quando a tela chegar no final ela voltara para a esquerda
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
