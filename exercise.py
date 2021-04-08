import os.path

class Players:
    def play(self, routeFile):
        array = self.openFile(routeFile)
        self.checkContent(array)

    def openFile(self, routeFile):
        if os.path.exists(routeFile):
            name, extension = os.path.splitext(routeFile)
            if(extension == '.txt'):
                file = open(routeFile, 'r')
                array = file.read().splitlines()
                file.close()
                return array
            else:
                print('el archivo debe de ser tipo TXT')
    def checkContent(self, arrayContent):
        rounds = int(arrayContent[0])
        arrayContent.pop(0)
        winnerPlayers = []
        differences = []
        for i in range(rounds):
           temp = arrayContent[i].split()
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


routeFile = input('Por favor escriba el nombre del archivo: ')

object = Players()
object.play(routeFile)


