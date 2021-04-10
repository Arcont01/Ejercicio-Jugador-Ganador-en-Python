import os.path
import pathlib
import logging
from os import system

class Players:
    def play(self, routeFile):
        array = self.openFile(routeFile)
        if array is not None:
            rounds = self.checkRounds(array)
            if rounds != 0:
                response = self.checkContent(rounds,array)
            else:
                raise Exception('Las rondas no pueden ser mayor a 10000')

    def openFile(self, routeFile):
        path = pathlib.Path(routeFile);
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

        rounds = int(rounds)
        content.pop(0)  

        if rounds > 10000:
           return 0

        return rounds

    def checkContent(self, rounds, arrayContent):
        winnerPlayers = []
        differences = []

        if rounds != len(arrayContent):
            raise Exception('El numero de rounds definido es diferente a los que juegan los jugadores')

        for i in range(rounds):
           temp = arrayContent[i].split()

           if(len(temp) != 2):
               raise Exception('Las rondas son unicamente de 2 jugadores')

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


