## This software is a purpose for a simple text based rpg game in python for POO learning purposes ##
## by Gabriel Mugi @mugiartes

from operator import index
from Character import Character
from Dungeon import Dungeon
import Elementos as el

a : Dungeon = Dungeon(8, 1)
p : Character = Character(a, el.elementoEnemy)

p.setStartPosition()

while True:
    move : str = str(input("Direcao: "))
    p.MoveCharacter(a.mapa, move)
    print(p.getPosition())
    a.mapPrinter()
    saida : str = str(input("Sair?: "))
    if saida in ["sim", "1"]:
        break
    elif saida in [" "]:
        pass
    else:
        pass
