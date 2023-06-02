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
from datetime import timedelta, datetime

population = dict()

lisfco = dict()
madfco = dict()
cdgfco = dict()
dubfco = dict()
brufco = dict()
lhrfco = dict()
lisfco2 = dict()
madfco2 = dict()
cdgfco2 = dict()
dubfco2 = dict()
brufco2 = dict()
lhrfco2 = dict()

###### Variáveis Editáveis ########
tamanho_população = 3

#Gera a pontuação de um voo, converte o tempo em segundos e soma com 
def gera_score_voo(partida,chegada, preço):
    partida_split = partida.split(':')
    chegada_split = chegada.split(':')

    t1 = timedelta(hours=int(partida_split[0]), minutes=int(partida_split[1]))
    t2 = timedelta(hours=int(chegada_split[0]),minutes=int(chegada_split[1]))

    
    score = t2.total_seconds() - t1.total_seconds() + int(preço)

    return score

#Gera a pontuação de um individuo da população, um individuo é um conjunto de 12 voos
def gera_score_conjunto_voo():
    for conjuto_voos in population:
        score = 0
        for voo in population[conjuto_voos]:
            if voo != 3:
                score += population[conjuto_voos][voo][-1]
            else:
                population[conjuto_voos][voo] = score
                
#Cria dicionario apartir dos dados do arquivo txt
def tratamento_txt():
    with open("flights.txt") as file:
        file_opened = file.readlines()
    for line in file_opened:
        line_split = line.split(',')

        #score = gera_score_voo(line_split[2], line_split[3], line_split[4].split('\n')[0])
        
        if line_split[0] == 'LIS':
            score = gera_score_voo(line_split[2], line_split[3], line_split[4].split('\n')[0])
            lisfco.update({len(lisfco):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0], score)})
        elif line_split[0] == 'MAD':
            madfco.update({len(madfco):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0], score)})
        elif line_split[0] == 'CDG':
            cdgfco.update({len(cdgfco):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0], score)})
        elif line_split[0] == 'DUB':
            dubfco.update({len(dubfco):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0], score)})
        elif line_split[0] == 'BRU':
            brufco.update({len(brufco):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0], score)})
        elif line_split[0] == 'LHR':
            lhrfco.update({len(lhrfco):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0], score)})

        elif line_split[1] == 'LIS':
            score = gera_score_voo(line_split[2], line_split[3], line_split[4].split('\n')[0])
            lisfco2.update({len(lisfco2):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0], score)})
        elif line_split[1] == 'MAD':
            madfco2.update({len(madfco2):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0], score)})
        elif line_split[1] == 'CDG':
            cdgfco2.update({len(cdgfco2):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0], score)})
        elif line_split[1] == 'DUB':
            dubfco2.update({len(dubfco2):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0], score)})
        elif line_split[1] == 'BRU':
            brufco2.update({len(brufco2):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0], score)})
        elif line_split[1] == 'LHR':
            lhrfco2.update({len(lhrfco2):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0], score)})
    

#Data possui todos os voos, totalizando 118
#formato population = 12 conjutos de voos
def criar_população():
    for item in range(tamanho_população):
        bloco_voos_score = {0:random.choice(lisfco), 
                            1:random.choice(lisfco2),
                            3: 0}
        population.update({len(population): bloco_voos_score})
        



# Calcula o fitness dos voos e armazena em dicionário
def fitness():
    for individuo in population:
        population[individuo]['score']




## Camando as funções
tratamento_txt()
criar_população()

print('Population: ')
print(population)
print('')

gera_score_conjunto_voo()


#print(population['0'][5])
