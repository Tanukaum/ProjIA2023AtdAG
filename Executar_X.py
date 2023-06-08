import os
import matplotlib.pyplot as plt ## pip install matplotlib
score_position = 12

Execuções = 50
n_Execut = list()
melhores = dict()
lista_pontuações = list()
total_para_media = 0

for i in range(Execuções):
    print('Execução: ' + str(i))
    n_Execut.append(i)
    os.system('python Executa_1.py')

with open("resultados.txt") as file:
    file_opened = file.readlines()

for line in file_opened:
    melhores.update({len(melhores):(line.split('\n')[0])})
    lista_pontuações.append(float(line.split('12: ')[1].replace('}\n','')))
    total_para_media += float(line.split('12: ')[1].replace('}\n',''))

media = total_para_media/len(file_opened)
DPadrao_parcial = 0

for ponto in lista_pontuações:
    DPadrao_parcial += (ponto - media)**2

Dpadrao = (DPadrao_parcial/len(file_opened)) ** 0.5

print(Dpadrao)


min = int(min(lista_pontuações))

for item in melhores:
    a = ((melhores[item].split('12: '))[1]).replace('}','')
    if int(a) == min:
        print(melhores[item])
        break

plt.plot(n_Execut, lista_pontuações)
plt.title('Melhor indivíduo de cada execução de 120 gerações')
plt.show()