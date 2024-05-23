#Bibliotecas 
import os
import time
#lista
nomes = ['Michael', 'Micaely', 'Fabio', 'César', 'Alexander']

#ordenado a lista
nomes.sort(reverse=True)

#exibe a lista na tela
for lista in range(len(nomes)):
    print(f'{lista + 1}º nome da lista: {nomes[lista]}.')
    time.sleep(1)
    os.system('cls')