import json

from ship import Ship

WIDTH = 10  # width of the grid
PLAYERS = {'player1', 'player2'}


class Game:
    def __init__(self):
        self.PLAYERS1_BOATS = []
        self.PLAYERS2_BOATS = []

        self.affichage_client()
        print(self.is_strike("player1", "E5"))

    def affichage_client(self):
        Matrix = [["  " for x in range(WIDTH + 1)] for y in range(WIDTH * 2 + 4)]

        # on créer le tableau
        for i in range(1, WIDTH + 1):
            Matrix[i][0] = chr(ord("A") + i - 1)
            Matrix[i][0] = Matrix[i][0] + " "
            Matrix[WIDTH + i + 3][0] = Matrix[i][0]
            Matrix[0][i] = str(i)
            Matrix[WIDTH + 3][i] = str(i)
            if (i < 10):
                Matrix[0][i] = Matrix[0][i] + " "
                Matrix[WIDTH + 3][i] = Matrix[0][i]

        # on ajoute les bateaux
        with open('boats.json') as boats_file:
            data_boats = json.load(boats_file)

        for player in PLAYERS:
            boats = []
            boats.append(Ship(4, data_boats[player]["PA"]))
            boats.append(Ship(3, data_boats[player]["Croiseur"][0]["1"]))
            boats.append(Ship(3, data_boats[player]["Croiseur"][0]["2"]))
            boats.append(Ship(2, data_boats[player]["SM"][0]["1"]))
            boats.append(Ship(2, data_boats[player]["SM"][0]["2"]))
            boats.append(Ship(2, data_boats[player]["SM"][0]["3"]))

            if (player == "player1"):
                self.PLAYERS1_BOATS = boats
            else:
                self.PLAYERS2_BOATS = boats

        for boat in self.PLAYERS1_BOATS:
            for coord in boat.cell:
                coordDecoder = int(format(ord(coord[0]), "d")) - 64
                Matrix[int(coordDecoder)][int(coord[1])] = "# "

        for boat in self.PLAYERS2_BOATS:
            for coord in boat.cell:
                coordDecoder = int(format(ord(coord[0]), "d")) - 64
                Matrix[WIDTH + 3 + int(coordDecoder)][int(coord[1])] = "# "

        # on affiche le tableau
        for y in range(WIDTH + 1):
            ligne = ""
            for x in range(WIDTH * 2 + 4):
                ligne = ligne + Matrix[x][y]
            print(ligne)

    def is_strike(self,player, strikeCoord):
        isstrike = False
        print(strikeCoord)

        if (player == "player1"):
            for boat in self.PLAYERS1_BOATS:
                if strikeCoord in boat.cell:
                    isstrike = True
                    return isstrike
        else:
            for boat in self.PLAYERS2_BOATS:
                if strikeCoord in boat.cell:
                    isstrike = True
                    return isstrike

        return isstrike
