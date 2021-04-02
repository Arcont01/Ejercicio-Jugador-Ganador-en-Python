import os.path

routeFile = input('Por favor escriba el nombre del archivo: ')

if os.path.exists(routeFile):
    name, extension = os.path.splitext(routeFile)
    if extension == '.txt':
        file = open(routeFile, 'r')
        array = file.read().splitlines()
        file.close()
        rounds = int(array[0])
        array.pop(0)
        winnerPlayers = []
        differences = []
        for i in range(rounds):
           temp = array[i].split()
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

    else:
        print('El archivo debe ser .txt')
else:
    print('El archivo no existe')


