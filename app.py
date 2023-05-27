"""
Lisbon LIS
Madrid MAD
Paris CDG
Dublin DUB
Brussels BRU
London LHR
Rome FCO <--

"""

data = dict()
population = dict()

#Cria dicionario apartir dos dados do arquivo txt
def tratamento_txt():
    with open("flights.txt") as file:
        file_opened = file.readlines()
    for line, item in zip(file_opened, range(len(file_opened))):
        line_split = line.split(',')
        
        data[item] = line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0]

tratamento_txt()

#item = 118, 118 - 12 = 106 = onde parar o loop
#formato population = 12 conjutos de voos
def criar_população():
    for item in range(len(data)):
        population[item] = data[item], data[item], data[item], data[item], data[item], data[item], data[item], data[item], data[item], data[item], data[item], data[item]

criar_população()

print(population[0])