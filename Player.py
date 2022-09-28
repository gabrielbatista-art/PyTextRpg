from Character import Character
from Dungeon import Dungeon
import Elementos as el

class Player(Character):
    def __init__(self, cenario : Dungeon, tipo : str = "Player" ,elemento : str = el.elementoPlayer):
        super().__init__(cenario = cenario, tipo = tipo, elemento = elemento)

    def fight(self):
        print(self.aroundElementsDetector(self.mapa, self.charPos[0], self.charPos[1]))
        if el.elementoEnemy in self.aroundElementsDetector(self.mapa, self.charPos[0], self.charPos[1]).values():
            print("LUTA")


