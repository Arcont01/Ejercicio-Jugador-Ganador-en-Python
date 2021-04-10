import os.path
import pathlib
import logging
import re
from os import system
logging.basicConfig(filename='logs.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)


class Players:
    def play(self, routeFile):
        array = self.openFile(routeFile)
        if array is not None:
            rounds = self.checkRounds(array)

        self.checkContent(rounds, array)

    def openFile(self, routeFile):
        path = pathlib.Path(routeFile)
        if path.exists():
            if os.path.exists(routeFile):
                name, extension = os.path.splitext(routeFile)
                if(extension == '.txt'):
                    try:
                        file = open(routeFile, 'r')
                        array = file.read().splitlines()
                        file.close()
                        return array
                    except IOError:
                        raise Exception('Error al tratar de leer archivo')
                else:
                    raise TypeError('el archivo debe de ser tipo TXT')
        else:
            raise Exception('No existe el archivo')

    def checkRounds(self, content):
        rounds = content[0]
        if re.fullmatch(r'\d', rounds) is None:
            raise Exception('No puedes definir rondas con strings')

        rounds = int(rounds)
        content.pop(0)

        if rounds > 10000:
            raise Exception('Las rondas no pueden ser mayor a 10000')
        elif rounds == 0:
            raise Exception(
                'No es posible jugar con una definicion de 0 rondas')

        return rounds

    def checkContent(self, rounds, arrayContent):
        winnerPlayers = []
        differences = []

        if rounds != len(arrayContent):
            raise Exception(
                'El numero de rounds definido es diferente a los que juegan los jugadores')

        for i in range(rounds):
            temp = arrayContent[i].split()

            if(len(temp) != 2):
                raise Exception('Las rondas son unicamente de 2 jugadores')

            if re.fullmatch(r'\d', temp[0]) is None or re.fullmatch(r'\d', temp[1]) is None:
                raise Exception('Solo se puede calcular puntos de diferencia con numeros enteros')

            firstPlayer = int(temp[0])
            secondPlayer = int(temp[1])

            if firstPlayer > secondPlayer:
                winnerPlayers.append(1)
                tempDifference = firstPlayer - secondPlayer
            else:
                winnerPlayers.append(2)
                tempDifference = secondPlayer - firstPlayer

            differences.append(tempDifference)

        maxPoint = max(differences)
        index = differences.index(maxPoint)
        winnerPlayer = winnerPlayers[index]

        print('Gano el jugador numero:', str(winnerPlayer))
        print('Con una diferencia de puntos de:', str(maxPoint))


try:
    routeFile = input('Por favor escriba el nombre del archivo: ')
    object = Players()
    object.play(routeFile)
except Exception as e:
    system('clear')
    logging.error(e)
    print('Error: ', e)
