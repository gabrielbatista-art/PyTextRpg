## This software is a purpose for a simple text based rpg game made in python for POO learning purposes ##
## by Gabriel Mugi @mugiartes ##

from operator import index
from Character import Character
from Player import Player
from Enemy import Enemy
from Dungeon import Dungeon
import Elementos as el

a : Dungeon = Dungeon(8, 1)

p : Player = Player(a)
e : Enemy = Enemy(a, el.elementoEnemy, "Enemy")
f : Character = Character(a, el.elementoEnemy, "Enemy")


while True:
    move : str = str(input("Direcao: "))
    p.MoveCharacter(move)
    e.randomMove()
    print(p.getPosition())
    a.mapPrinter()
    p.fight()
    saida : str = str(input("Sair?: "))
    if saida in ["sim", "1"]:
        break
    elif saida in [" "]:
        pass
    else:
        pass
