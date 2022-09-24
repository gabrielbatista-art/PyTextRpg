from random import randint

class Dungeon:
    def __init__(self):
        self.mapa : list = []

        #Elementos cenário
        self.elementoParede = "|"
        self.elementoTeto = "-"
        self.elementoLivre = " "
        self.elementoObstaculo = "#"
        self.elementoPorta = "A"


    def gridGenerator(self, size : int): #Cria um grid equivalente
        self.largura : int = 0
        self.linha : list = []
        
        while len(self.mapa) < size:
            self.linha.clear()
            while self.largura < size:
                self.linha.append(self.elementoLivre)
                self.largura += 1
 
            self.mapa.append(list(self.linha))
            self.largura = 0

    def wallDetector(self): #Detecta as bordas do grid e os povoa com paredes
        mapa : list = self.mapa
        for index in range(len(mapa)):
            for parede in range(len(mapa[index])):
                if index == 0 or index == len(mapa) - 1:
                    mapa[index][parede] = self.elementoTeto
                    mapa[-1][parede] = self.elementoTeto
                else:
                    mapa[index][0] = self.elementoParede
                    mapa[index][-1] = self.elementoParede

    def mazeCreator(self, dificuldade : float):
        mapa : list = self.mapa
        mapaX : int = len(self.mapa[0])
        mapaY : int = len(self.mapa)

        for linha in range(len(mapa)):
            lineXobjsQuantity : int = 2 * dificuldade
            lineXobjsSetted : int = 0

            for elemento in range(len(mapa[linha])):
                random : int = randint(0, 1)
                if mapa[linha][elemento] == self.elementoLivre and random == 1 and lineXobjsQuantity >= lineXobjsSetted:
                    mapa[linha][elemento] = self.elementoObstaculo
                    lineXobjsSetted += 1

    def doorSetter(self):
        mapa : list = self.mapa
        portasQuantity : int = 2
        portasSetted : dict = {"top" : 0, "bottom" : 0, "left" : 0, "right" : 0}

        for linha in range(len(mapa)):
            for elemento in range(len(mapa[linha])):
                random : int = randint(0, 1)

                #Seta portas no topo do labirinto
                if linha == 0 and elemento > 0 and elemento < (len(mapa[linha]) - 1) and portasSetted["top"] == 0 and random == 1:
                    mapa[linha][elemento] = self.elementoPorta
                    portasSetted["top"] += 1
                    print(portasSetted["top"])
                
                #Seta portas na parte de baixo do labirinto
                if linha == (len(mapa)-1) and elemento > 0 and elemento < (len(mapa[linha]) - 1) and portasSetted["bottom"] == 0 and random == 1:
                    mapa[linha][elemento] = self.elementoPorta
                    portasSetted["bottom"] += 1

                #Seta portas nas laterais do labirinto
                #Esquerda
                if linha != 0 and linha != (len(mapa)-1) and elemento == 0 and portasSetted["left"] == 0 and random == 1:
                    mapa[linha][elemento] = self.elementoPorta
                    portasSetted["left"] += 1

                #Direita
                if linha != 0 and linha != (len(mapa)-1) and elemento > (len(mapa[linha]) - 2) and portasSetted["right"] == 0 and random == 1:
                    mapa[linha][elemento] = self.elementoPorta
                    portasSetted["right"] += 1

    def mapPrinter(self):
        for linha in range(len(self.mapa)):
            print(self.mapa[linha])
