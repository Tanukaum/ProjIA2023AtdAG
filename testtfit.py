import random
from datetime import timedelta
#população inicial que irá conter todos os conjuntos de voos
population = dict()
#voos ida
lisfco = dict()
madfco = dict()
cdgfco = dict() 
dubfco = dict()
brufco = dict()
lhrfco = dict()
#voos volta
lisfco2 = dict()
madfco2 = dict()
cdgfco2 = dict()
dubfco2 = dict()
brufco2 = dict()
lhrfco2 = dict()

###### Variáveis Editáveis ########
tamanho_população = 1
score_position = 12 # deve ser o ultimo slot de population[conjunto_voos]

def tratamento_txt():
    with open("flights.txt") as file:
        file_opened = file.readlines()
    for line in file_opened:
        line_split = line.split(',')
        
        if line_split[0] == 'LIS':
            lisfco.update({len(lisfco):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0])})
        elif line_split[0] == 'MAD':
            madfco.update({len(madfco):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0])})
        elif line_split[0] == 'CDG':
            cdgfco.update({len(cdgfco):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0])})
        elif line_split[0] == 'DUB':
            dubfco.update({len(dubfco):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0])})
        elif line_split[0] == 'BRU':
            brufco.update({len(brufco):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0])})
        elif line_split[0] == 'LHR':
            lhrfco.update({len(lhrfco):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0])})

        elif line_split[1] == 'LIS':
            lisfco2.update({len(lisfco2):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0])})
        elif line_split[1] == 'MAD':
            madfco2.update({len(madfco2):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0])})
        elif line_split[1] == 'CDG':
            cdgfco2.update({len(cdgfco2):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0])})
        elif line_split[1] == 'DUB':
            dubfco2.update({len(dubfco2):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0])})
        elif line_split[1] == 'BRU':
            brufco2.update({len(brufco2):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0])})
        elif line_split[1] == 'LHR':
            lhrfco2.update({len(lhrfco2):(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].split('\n')[0])})


def criar_população():
    for item in range(tamanho_população):
        bloco_voos = {  0:(lisfco[0]),
                        1:(madfco[0]),
                        2:(cdgfco[0]),
                        3:(dubfco[0]),
                        4:(brufco[0]),
                        5:(lhrfco[0]),
                        6:(lisfco2[0]),
                        7:(madfco2[0]),
                        8:(cdgfco2[0]),
                        9:(dubfco2[0]),
                        10:(brufco2[0]),
                        11:(lhrfco2[0]),
                        score_position: 0}
        
        population.update({len(population): bloco_voos})

def fitness(individuo):
    score = 0
    ida = list()
    volta = list()
    for voo in individuo: 
        #não chega na posição do score
        if voo != score_position:  
            #voos ida, compara o horário de chegada
            if voo <= 5: 
                tempo = individuo[voo][3].split(':')
                ida.append(timedelta(hours=int(tempo[0]),minutes=int(tempo[1])).total_seconds())
            
            #voos volta, compara o horário de partida
            else: 
                tempo = individuo[voo][2].split(':')
                volta.append(timedelta(hours=int(tempo[0]),minutes=int(tempo[1])).total_seconds())
       
    menor_ida = min(ida)
    maior_ida = max(ida)
    menor_volta = min(volta)
    maior_volta = max(volta)
    score = (maior_ida - menor_ida) + (maior_volta - menor_volta)
    individuo[score_position] = score

###Inicialização
tratamento_txt()
criar_população()
for item in range(12):
    print(population[0][item])

print('')
fitness(population[0])
for item in population:
    print(population[item])