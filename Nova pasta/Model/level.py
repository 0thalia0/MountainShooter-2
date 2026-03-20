#!/usr/bin/python
# -*- coding: utf-8 -*-

from EntityFactory import EntityFactory
from Game import Game


class Level(EntityFactory, Game):
    def __init__(self):
        self.window = None
        self.name = None
        self.entity_list = None

    def run(self, ):
        pass
