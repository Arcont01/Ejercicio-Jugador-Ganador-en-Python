file = open('prueba.txt', 'r')
array = file.read().splitlines()
rounds = array[0]
print(rounds)
