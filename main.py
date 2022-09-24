## This software is a purpose for a simple text based rpg game in python for POO learning purposes ##
## by Gabriel Mugi @mugiartes

from operator import index
from Dungeon import Dungeon

a : Dungeon = Dungeon()

a.gridGenerator(8)
a.wallDetector()
a.doorSetter()
a.mazeCreator(2)
a.mapPrinter()
