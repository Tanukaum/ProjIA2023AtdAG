"""
Lisbon LIS
Madrid MAD
Paris CDG
Dublin DUB
Brussels BRU
London LHR
Rome FCO <--

"""
import random

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

#data possui todos os voos, totalizando 118
#formato population = 12 conjutos de voos
def criar_população():
    for item in range(100):
        bloco_12 = [random.choice(data) for item in range(12)]
        population.update(bloco_12)

criar_população()


