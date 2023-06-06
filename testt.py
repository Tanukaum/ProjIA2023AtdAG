import random
from datetime import timedelta

def gera_score_voo(partida,chegada, preço):
    partida_split = partida.split(':')
    chegada_split = chegada.split(':')

    t1 = timedelta(hours=int(partida_split[0]), minutes=int(partida_split[1]))
    t2 = timedelta(hours=int(chegada_split[0]),minutes=int(chegada_split[1]))

    
    score = t2.total_seconds() - t1.total_seconds() + int(preço)

    return int(score)

score_position = 2
a = {0: ('LIS', 'FCO', '18:12', '20:17', '242', 7742), 1: ('FCO', 'LIS', '8:04', '10:59', '136', 10636), 2: 18378}
b = {0: ('LIS', 'FCO', '11:08', '13:07', '175', 7315), 1: ('FCO', 'LIS', '12:31', '14:02', '234', 5694), 2: 13009}
a1 = a.copy()
b2 = b.copy()
ponto_corte = random.randint(1, score_position - 1)

for i in range(ponto_corte, score_position) :
    a1[i], b2[i] = b2[i], a1[i]
    
a1[score_position] = a1[0][-1] + a1[1][-1]
b2[score_position] = b2[0][-1] + b2[1][-1]

dict = dict()
dict.update({len(dict): a})
dict.update({len(dict): a1})
dict.update({len(dict): b})
dict.update({len(dict): b2})

ordenado_ruim = sorted(dict.items(), key= lambda slot: slot[1][score_position], reverse=True) #resultado é "tupla ordenada"
ordenado_bom = sorted(dict.items(), key= lambda slot : slot[1][score_position])
pior_item = ordenado_ruim[0][1]
melhor_item = ordenado_bom[0][1]

ordena_dict = sorted(dict.items(), key = lambda slot: slot[1][score_position], reverse=True)

print(ordenado_bom[0][1][score_position])
dict[ordena_dict[0][0]] = melhor_item
