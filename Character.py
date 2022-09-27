from distutils.archive_util import make_archive
from random import randint
from Dungeon import Dungeon
import Elementos
from Utilis import aroundElementsDetector

class Character:
    def __init__(self, cenario : Dungeon, elemento : str):
        self.nome : str
        self.tipoChar : str = elemento
        self.str : int
        self.lck : int
        self.defe : int
        self.xp : int
        self.lvl : int
        self.items : dict = {"arma" : None, "for" : None}

        self.mapa : list = cenario.mapa
        self.charPositioned : bool = False

        self.aroundEl : dict = {}
        self.charPos : list
        self.oldPos : str = ""
        self.actPos : str = ""

    def setStartPosition(self):
        mapa : list = self.mapa
        self.charPosX : int
        self.charPosY : int
        while not self.charPositioned:
            for linha in range(len(mapa)):
                if not self.charPositioned:
                    for elemento in range(len(mapa[linha])):
                        random : int = randint(0, 2)
                        if mapa[linha][elemento] == Elementos.elementoPorta and random == 1:
                            self.actPos = mapa[linha][elemento]

                            mapa[linha][elemento] = self.tipoChar

                            self.charPositioned = True
                            
                            self.charPosX = elemento
                            self.charPosY = linha

        self.charPos = [self.charPosX, self.charPosY]

    def getPosition(self) -> list:
        return self.charPos

    def collisionDetector(self, mapa: list, destino : str): #Permite ou não que o personagem se mova dependendo dos objetos envolta dele
        self.charPosX : int = self.charPos[0]
        self.charPosY : int= self.charPos[1]

        self.aroundElements : dict = self.aroundElementsDetector(mapa, self.charPosX, self.charPosY)

        if destino == "up":
            if self.aroundElements["top"] in [Elementos.elementoParede, Elementos.elementoTeto, Elementos.elementoObstaculo, None]:
                return False
            else:
                self.aroundEl = self.aroundElements
                return True
        
        if destino == "down":
            if self.aroundElements["bottom"] in [Elementos.elementoParede, Elementos.elementoTeto, Elementos.elementoObstaculo, None]:
                return False
            else:
                self.aroundEl = self.aroundElements
                return True

        if destino == "left":
            if self.aroundElements["left"] in [Elementos.elementoParede, Elementos.elementoTeto, Elementos.elementoObstaculo, None]:
                return False
            else:
                self.aroundEl = self.aroundElements
                return True

        if destino == "right":
            if self.aroundElements["right"] in [Elementos.elementoParede, Elementos.elementoTeto, Elementos.elementoObstaculo, None]:
                return False
            else:
                self.aroundEl = self.aroundElements
                return True
       
    def aroundElementsDetector(self, mapa : list, posX : int, posY : int): #Detecta os elementos que estão envolta do personagem nas quatro direções de movimento possível.
        self.elementos : dict = {"top" : None, "right" : None, "bottom" : None, "left" : None}

        for linha in range(len(mapa)):
            if posY - 1 >= 0:
                self.elementos["top"] = mapa[posY - 1][posX]

            if posY + 1 < len(mapa):
                self.elementos["bottom"] = mapa[posY + 1][posX]

            if posX - 1 >= 0:
                self.elementos["left"] = mapa[posY][posX - 1]

            if posX + 1 < len(mapa[posY]):
                self.elementos["right"] = mapa[posY][posX + 1]

        return self.elementos

    def MoveCharacter(self, mapa : list, destino : str): #Move o personagem levando em conta o feedback do collisionDetector()
        self.charPosX = self.charPos[0]
        self.charPosY = self.charPos[1]
        self.posMove = self.collisionDetector(mapa, destino)

        if self.posMove:
            if destino == "up":
                print("A")
                self.oldPos = self.actPos
                mapa[self.charPosY - 1][self.charPosX] = self.tipoChar
                mapa[self.charPosY][self.charPosX] = self.oldPos
                self.actPos = self.aroundEl["top"]
                self.charPos[1] = self.charPosY - 1

            if destino == "down":
                self.oldPos = self.actPos
                mapa[self.charPosY + 1][self.charPosX] = self.tipoChar
                mapa[self.charPosY][self.charPosX] = self.oldPos
                self.actPos = self.aroundEl["bottom"]
                self.charPos[1] = self.charPosY + 1

            if destino == "left":
                self.oldPos = self.actPos
                mapa[self.charPosY][self.charPosX - 1] = self.tipoChar
                mapa[self.charPosY][self.charPosX] = self.oldPos
                self.actPos = self.aroundEl["left"]
                self.charPos[0] = self.charPosX - 1

            if destino == "right":
                self.oldPos = self.actPos
                mapa[self.charPosY][self.charPosX + 1] = self.tipoChar
                mapa[self.charPosY][self.charPosX] = self.oldPos
                self.actPos = self.aroundEl["right"]
                self.charPos[0] = self.charPosX + 1
        