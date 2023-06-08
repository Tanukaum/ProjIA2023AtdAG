import random
import matplotlib.pyplot as plt ## pip install matplotlib
from datetime import timedelta

#população inicial que irá conter todos os conjuntos de voos
population = dict()

#Listas usadas para gerar o gráfico
geração = list()
melhor_pontuação = list()
pior_pontuação = list()
media_pontuação = list()

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
tamanho_população = 100

#Parametros Torneio
torneio_size = 7 #Tamanho usado para o torneio
torneio_chance = 0.75  #Chance do melhor ou pior ser escolhido no torneio

chance_cruzamento = 0.7
chance_mutação = 0.05
taxa_elitismo = 1  #Adicionado para observar influência da variação do elitismo

numero_gerações = 120

                
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
    individuo[score_position] = int(score)

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


#Realiza o torneio e cria a piscina de cruzamento
def torneio(pop_torneio):
    piscina = dict()
    vencedores = dict()
    while len(piscina) < tamanho_população:
        vencedores.clear()
        for lutadores in range(torneio_size):
            vencedores.update({len(vencedores): random.choice(pop_torneio)})
        
        melhor = (sorted(vencedores.items(), key= lambda slot : slot[1][score_position]))[0][1] #[0][1]primeiro individuo do dict e informações do individuo, [0][0]primeiro individuo do dict e seu indice no dict desordenado
        pior = (sorted(vencedores.items(), key= lambda slot : slot[1][score_position], reverse=True))[0][1]
        
        
        #Seleciona o melhor indivíduo
        if random.random() < torneio_chance:
            piscina.update({len(piscina): melhor})
        else:
            piscina.update({len(piscina): pior})
        
    return piscina


#Se o melhor da nova for pior que o melhor antigo substitui o pior da nova pelo melhor antigo
def elitismo_população(pop_anterior, pop_nova):
    #Substitui o pior individuo da nova_população pelo melhor da pop_anterior
    melhor_antigo = sorted(pop_anterior.items(), key= lambda slot :slot[1][score_position])#resultado é "tupla ordenada" crescente
    melhor_novo = sorted(pop_nova.items(), key= lambda slot :slot[1][score_position])#resultado é "tupla ordenada" crescente
    pior_novo = sorted(pop_anterior.items(), key= lambda slot :slot[1][score_position], reverse=True)#resultado é "tupla ordenada" decrescente

    if melhor_antigo[0][1][score_position] < melhor_novo[0][1][score_position]:
        pop_nova[pior_novo[0][0]] = melhor_antigo[0][1]
    

#Realiza o crossover e mutação dos indivíduos
def crossover_mutation_elitism(pop_cross):
    nova_population = dict()
    piscina = torneio(pop_cross)
    
    
    while len(nova_population) < tamanho_população:
        #Seleciona os índices do casal
        pai_index = random.choice(list(piscina.keys()))
        mae_index = random.choice(list(piscina.keys()))
        while pai_index == mae_index:
            mae_index = random.choice(list(piscina.keys()))
        #Remove da piscina os individuos e dá pra variavel
        pai_value = piscina.pop(pai_index)
        mae_value = piscina.pop(mae_index)
        
        #Realiza o crossover
        if random.random() < chance_cruzamento:
            #Formato do individuo não permite cortar em '0', ou os pais continuariam os mesmos
            ponto_de_corte = random.randint(1, score_position-1)    

            filho1 = pai_value.copy()
            filho2 = mae_value.copy()

            #Troca todos voos de f1 por f2 do ponto de corte até o score
            for corte in range(ponto_de_corte, score_position):
                filho1[corte], filho2[corte] = filho2[corte], filho1[corte]

            
            #Checa mutação, a chance de mutar esta dentro da função mutação
            mutação(filho1)
            mutação(filho2)
                        
            fitness(filho1)
            fitness(filho2)
            #Adiciona a nova_população os filhos
            nova_population.update({len(nova_population): filho1})
            nova_population.update({len(nova_population): filho2})

        
        #Chance de crossover não atendida, apenas repassa os indivíduos
        else:
            #Checa mutação, a chance de mutar esta dentro da função
            mutação(pai_value)
            mutação(mae_value)
            
            fitness(pai_value)
            fitness(mae_value)
            
            nova_population.update({len(nova_population):pai_value}) 
            nova_population.update({len(nova_population):mae_value}) 
        
    elitismo_população(pop_cross, nova_population)
    
    return nova_population

#Obtém o melhor indivíduo da população
def gera_ponto_gráfico(população):
    melhor_individuo = sorted(população.items(), key= lambda slot:slot[1][score_position])
    pior_individuo = sorted(população.items(), key= lambda slot:slot[1][score_position], reverse=True)
    total = 0
    for item in população:
       total += (população[item][score_position])
    
    
    return melhor_individuo[0][1], pior_individuo[0][1], total/tamanho_população


def gera_grafico():
    new_pop = dict()
    new_pop.update(population)
    best = ''
    for i in range(numero_gerações):
        geração.append(i)
        individuo_melhor, individuo_pior, media = gera_ponto_gráfico(new_pop)
        melhor_pontuação.append(individuo_melhor[score_position])
        #pior_pontuação.append(individuo_pior[score_position])
        media_pontuação.append(media)
        new_pop = crossover_mutation_elitism(new_pop)

    '''plt.plot(geração, melhor_pontuação)
    plt.plot(geração,media_pontuação)
    plt.show()
'''
    for individuo in new_pop:
        if (new_pop[individuo][score_position]) == melhor_pontuação[-1]:
            best = (new_pop[individuo])
            break
    
    return best, melhor_pontuação[-1]
     
        
## Chamando as funções
tratamento_txt()
criar_população()
individuo, ponto = gera_grafico() #Aqui ocorrem as gerações
#Comentar daqui para baixo para usar apenas um o gráfico de media e melhor individuo
#Remover comentário se for rodar várias execuções com o roda_x.py
try:
    with open('resultados.txt', 'a+') as f:
        f.writelines(str(individuo) + '\n')
except:
    with open('resultados.txt', 'a+') as f:
        f.writelines(str(individuo)+ '\n')



