import os.path
import pathlib

class Players:
    def play(self, routeFile):
        array = self.openFile(routeFile)
        if array is not None:
            rounds = self.checkRounds(array)
            if rounds != 0:
                response = self.checkContent(rounds,array)
                if response == 0:
                    print('Solo se pueden 2 jugadores')
            else:
                print('Las rondas no pueden ser mayor a 10000')

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
                        print('Error al tratar de leer archivo')
                else:
                    print('el archivo debe de ser tipo TXT')
        else:
            print('No existe el archivo')

    def checkRounds(self, content):
        rounds = int(content[0])
        content.pop(0)

        if rounds > 10000:
           return 0

        return rounds

    def checkContent(self, rounds, arrayContent):
        winnerPlayers = []
        differences = []
        for i in range(rounds):
           temp = arrayContent[i].split()

           if(len(temp) != 2):
                return 0;

           firstPlayer = int(temp[0])
           secondPlayer = int(temp[1])

           if firstPlayer > secondPlayer:
               winnerPlayers.append(1)
           else:
               winnerPlayers.append(2)

           tempDifference = firstPlayer - secondPlayer
           differences.append(abs(tempDifference))
            
        maxPoint = max(differences)
        index = differences.index(maxPoint)
        winnerPlayer = winnerPlayers[index]

        print('El jugador: ' + str(winnerPlayer) + ' gano, en la ronda ' + str(index + 1))
        print('Con una diferencia de: ' + str(maxPoint))
        return 1


routeFile = input('Por favor escriba el nombre del archivo: ')

object = Players()
object.play(routeFile)


