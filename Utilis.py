def aroundElementsDetector(mapa : list, posX : int, posY : int): #Detecta os elementos que estão envolta do personagem nas quatro direções de movimento possível.
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