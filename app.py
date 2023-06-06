import random
import matplotlib.pyplot ## pip install matplotlib
from datetime import timedelta

#população inicial que irá conter todos os conjuntos de voos
population = dict()

#Listas usadas para gerar o gráfico
geração = list()
pontuação = list()

#dicionários que separam as viagens origem e destino por localidade
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
####### Variável FIXA ########
score_position = 12 # deve ser o ultimo slot de population[conjunto_voos]

###### Variáveis Editáveis ########
tamanho_população = 50

#Parametros Torneio
#torneio_size = 2  #Tamanho que foi usado, implementação genérica não realizada
torneio_escolha = 0.75  #Chance do melhor ou pior ser escolhido no torneio

chance_cruzamento = 0.7
chance_mutação = 0.1
taxa_elitismo = 1  #Adicionado para observar influência da variação do elitismo

numero_gerações = 350
                
#Cria dicionarios apartir dos dados do arquivo txt
# Os dicionarios separam as localidades de cada voo 
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
    

#Formato population = 12 conjutos de voos
#Tamanho de population -> tamanho da variavel "tamanho_população"
def criar_população():
    for item in range(tamanho_população):
        bloco_voos = {0:random.choice(lisfco),
                            1:random.choice(madfco),
                            2:random.choice(cdgfco),
                            3:random.choice(dubfco),
                            4:random.choice(brufco),
                            5:random.choice(lhrfco),
                            6:random.choice(lisfco2),
                            7:random.choice(madfco2),
                            8:random.choice(cdgfco2),
                            9:random.choice(dubfco2),
                            10:random.choice(brufco2),
                            11:random.choice(lhrfco2),
                            score_position: 0}

        bloco_voos_score = fitness(bloco_voos)
        population.update({len(population): bloco_voos_score})
        

#Gera a pontuação de um individuo da população, um individuo é um conjunto de 12 voos
def fitness(individuo):
    score = 0
    price = 0
    ida = list()
    volta = list()
    for voo in individuo:
        #não chega na posição do score
        if voo != score_position:  
            price += int(individuo[voo][4])
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
    score = (maior_ida - menor_ida) + (maior_volta - menor_volta) + price
    individuo[score_position] = score
    return individuo


#Realiza mutação gene a gene
def mutação(individuo):
    for voo in individuo:
        if random.random() < chance_mutação:
            if voo != score_position:
                if voo == 0:
                    individuo[voo] = random.choice(lisfco)
                elif voo == 1:
                    individuo[voo] = random.choice(madfco)
                elif voo == 2:
                    individuo[voo] = random.choice(cdgfco)
                elif voo == 3:
                    individuo[voo] = random.choice(dubfco)
                elif voo == 4:
                    individuo[voo] = random.choice(brufco)
                elif voo == 5:
                    individuo[voo] = random.choice(lhrfco)
                elif voo == 6:
                    individuo[voo] = random.choice(lisfco2)
                elif voo == 7:
                    individuo[voo] = random.choice(madfco2)
                elif voo == 8:
                    individuo[voo] = random.choice(cdgfco2)
                elif voo == 9:
                    individuo[voo] = random.choice(dubfco2)
                elif voo == 10:
                    individuo[voo] = random.choice(brufco2)
                else:
                    individuo[voo] = random.choice(lhrfco2)


#Realiza o torneio de dois individuos
def torneio(individuo1, individuo2):
    #Se o random.random < torneio_escolha, melhor individuo é usado, se não o pior
    if random.random() < torneio_escolha:
        #Melhor individuo é o menor
        if individuo1[score_position] < individuo2[score_position]:
            return individuo1
        else:
            return individuo2
    else:
        #Pior individuo é o maior
        if individuo1[score_position] < individuo2[score_position]:
            return individuo2
        else:
            return individuo1

#Realiza o crossover e mutação dos individuos
def crossover_mutation_elitism(pop_cross):
    nova_population = dict()

    while len(nova_population) < tamanho_população:
        # obtém o indicie da posição dos pais
        position_pai = random.choice(list(pop_cross.keys()))
        position_mae = random.choice(list(pop_cross.keys()))

        #Se os pais não forem a mesma posição prossegue
        while position_pai == position_mae:
            position_mae = random.choice(list(pop_cross.keys()))
        
        pai = pop_cross[position_pai].copy()
        mae = pop_cross[position_mae].copy()
        
        #Chances de crossover
        if random.random() < chance_cruzamento:
            gene_vencedor = torneio(pai, mae)

            filho1 = pai
            filho2 = mae

            #Formato do individuo não permite cortar em '0', ou não cortaria nada
            ponto_de_corte = random.randint(1, score_position-1)    

            #Troca todos voos de f1 por f2 do ponto de corte até o score
            for corte in range(ponto_de_corte, score_position):
                filho1[corte], filho2[corte] = filho2[corte], filho1[corte]

            #Checa mutação, a chance de mutar esta dentro da função mutação
            mutação(filho1)
            mutação(filho2)
                        
            fitness(filho1)
            fitness(filho2)
            #Pior filho morre 
            if filho1[score_position] < filho2[score_position]:
               melhor_filho = filho1
            else:
                melhor_filho = filho2
            
            nova_population.update({len(nova_population): gene_vencedor})
            nova_population.update({len(nova_population): melhor_filho})
        
        #Chance de crossover não atendida, apenas repassa os individuos
        else:
            #Checa mutação, a chance de mutar esta dentro da função
            mutação(pai)
            mutação(mae)
            
            fitness(pai)
            fitness(mae)

            nova_population.update({len(nova_population):pai}) 
            nova_population.update({len(nova_population):mae}) 
    
    #Substitui o pior individuo da nova_população pelo melhor da pop_cross
    if random.random() < taxa_elitismo:
        
        pior_primeiro = sorted(nova_population.items(), key= lambda slot: slot[1][score_position], reverse=True) #resultado é "tupla ordenada"
        melhor_primeiro = sorted(pop_cross.items(), key= lambda slot : slot[1][score_position])
        
        if pior_primeiro[0][1][score_position] > melhor_primeiro[0][1][score_position]:
            nova_population[pior_primeiro[0][0]] = melhor_primeiro[0][1]

    return nova_population

#Obtém o melhor indivíduo da população
def gera_ponto_gráfico(população):
    melhor_individuo = sorted(população.items(), key= lambda slot:slot[1][score_position])

    return melhor_individuo[0][1]


def gera_grafico():
    new_pop = dict()
    new_pop.update(population)
    for i in range(numero_gerações):
        geração.append(i)
        individuo_melhor = gera_ponto_gráfico(new_pop)
        print('Geração: ' + str(i))
        print(individuo_melhor)
        pontuação.append(individuo_melhor[score_position])
        new_pop = crossover_mutation_elitism(new_pop)
    
    matplotlib.pyplot.plot(geração,pontuação)
    matplotlib.pyplot.show()   
        
## Chamando as funções
tratamento_txt()
criar_população()
gera_grafico()