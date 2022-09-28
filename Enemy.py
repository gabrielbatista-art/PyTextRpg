from Character import Character
from Dungeon import Dungeon
from random import randint

class Enemy(Character):
    def __init__(self, cenario: Dungeon, elemento: str, tipo: str):
        super().__init__(cenario, elemento, tipo)

    def randomMove(self):
        self.moveDir : list = ["up", "down", "left", "right"]
        self.randMove : int = randint(0, 3)

        self.MoveCharacter(self.moveDir[self.randMove])