## This software is a purpose for a simple text based rpg game in python for POO learning purposes ##
## by Gabriel Mugi @mugiartes

from operator import index
from Character import Character
from Dungeon import Dungeon

a : Dungeon = Dungeon(8, 1)
p : Character = Character()

p.getPosition(a)
while True:
    move : str = str(input("Direcao: "))
    print(p.charPos)
    p.MoveCharacter(a.mapa, move)
    a.mapPrinter()
    saida : str = str(input("Sair?: "))
    if saida in ["sim", "1"]:
        break
    elif saida in [" "]:
        pass
    else:
        pass

