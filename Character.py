from distutils.archive_util import make_archive
from random import randint
from Dungeon import Dungeon
import Elementos

class Character:
    def __init__(self):
        self.nome : str
        self.tipo : str
        self.str : int
        self.lck : int
        self.defe : int
        self.xp : int
        self.lvl : int
        self.items : dict = {"arma" : None, "for" : None}

        self.charPos : list

    def getPosition(self, mapa : Dungeon):
        self.charPos = mapa.getPlayerPos()

    def collisionDetector(self, mapa: list, destino : str):
        charPosX : int = self.charPos[0]
        charPosY : int= self.charPos[1]

        aroundElements : dict = self.aroundElementsDetector(mapa, charPosX, charPosY)

        if destino == "up":
            if aroundElements["top"] in [Elementos.elementoParede, Elementos.elementoTeto, None]:
                return False
            else:
                return True
        
        if destino == "down":
            if aroundElements["bottom"] in [Elementos.elementoParede, Elementos.elementoTeto, None]:
                return False
            else:
                return True

        if destino == "left":
            if aroundElements["left"] in [Elementos.elementoParede, Elementos.elementoTeto, None]:
                return False
            else:
                return True

        if destino == "right":
            if aroundElements["right"] in [Elementos.elementoParede, Elementos.elementoTeto, None]:
                return False
            else:
                return True      
       
    def aroundElementsDetector(self, mapa : list, posX : int, posY : int):
        elementos : dict = {"top" : None, "right" : None, "bottom" : None, "left" : None}

        for linha in range(len(mapa)):
            if posY - 1 >= 0:
                elementos["top"] = mapa[posY - 1][posX]

            if posY + 1 < len(mapa):
                elementos["bottom"] = mapa[posY + 1][posX]

            if posX - 1 > 0:
                elementos["left"] = mapa[posY][posX - 1]

            if posX + 1 < len(mapa[posY]):
                elementos["right"] = mapa[posY][posX + 1]

        return elementos

    def MoveCharacter(self, mapa : list, destino : str):
        charPosX = self.charPos[0]
        charPosY = self.charPos[1]
        posMove = self.collisionDetector(mapa, destino)

        if posMove:
            if destino == "up":
                mapa[charPosY - 1][charPosX] = Elementos.elementoPlayer
                mapa[charPosY][charPosX] = Elementos.elementoLivre
                self.charPos[1] = charPosY - 1

            if destino == "down":
                mapa[charPosY + 1][charPosX] = Elementos.elementoPlayer
                mapa[charPosY][charPosX] = Elementos.elementoLivre
                self.charPos[1] = charPosY + 1

            if destino == "left":
                mapa[charPosY][charPosX - 1] = Elementos.elementoPlayer
                mapa[charPosY][charPosX] = Elementos.elementoLivre
                self.charPos[0] = charPosX - 1

            if destino == "right":
                mapa[charPosY][charPosX + 1] = Elementos.elementoPlayer
                mapa[charPosY][charPosX] = Elementos.elementoLivre
                self.charPos[0] = charPosX + 1

        