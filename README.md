# ProjIA2023AtdAG
Projeto da matéria de IA 2023 Atividade de Algoritmos Genéticos

# Como utilizar

### O arquivo Executa_1.py
Caso deseje ver apenas uma execução, rodar o arquivo Executa_1.py. Essa execução exibe o melhor indivíduo  e a média da população por geração.

É o arquivo que contém a execução do algoritmo genético. Nele é possível mudar os parâmetros do AG. Parâmetros editáveis:

* tamanho da população inicial
* tamanho do torneio
* porcentagem do torneio
* porcentagem de crossover
* porcentagem de mutação
* porcentagem de elitismo
* número de gerações

### O arquivo Executa_X.py
Caso deseje ver diversas execuções, rodar o arquivo Executa_X.py, nele é possível obter o melhor indivíduo de X execuções do arquivo Executa_1.py. Cada execução exibe o gráfico do arquivo Executa_1.py, ao fechar o gráfico, o seguinte é exibido até que acabe o número de execuções. Após a última é exibido o gráfico dos melhores de cada execução.

É o arquivo que permite executar diversas vezes o Executa_1.py, nele é possível obter o desvio padrão das melhores soluções das X execuções e editar o número das X execuções. Parâmetro editável:

* Número de execuções


## Bibliotecas necessárias

- matplotlib comando de instalação: 
```
pip install matplotlib
```