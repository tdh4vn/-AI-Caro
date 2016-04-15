from abc import abstractmethod

import game_config as GameManager
class GameScene(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def draw(self, screen):
        return