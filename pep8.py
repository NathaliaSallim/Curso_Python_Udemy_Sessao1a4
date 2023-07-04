"""
PEP8 - Pyhton Enhacement Proposal
São propostas de melhorias para a linguagem pyhton
The zen of python
import this
"""
"""
A ideia da pep8 é que possamos escrever códigos python de forma pythonica

[1] Utilize CameCase para nomes de classes;
[2] Utilize nomes em minusculos separados em  underline para funções ou varáveis;

class Calculadora:
    pass

class CalculadoraCientifica:
    pass

def soma():
    pass 

def soma_dois():
    pass

numero =4

numero_impar = 5

[3]  Utilize quatro espaços para identação! (Não use TAB), o espaço do tab geralmente é configurado em 4 espaços, mas de
depende da configuração da ide.

#if 'a' in 'banana':
#print('tem')
#erro de identação

if 'a' in 'banana':
    print('tem') #quatro espaços entre o print"#

[4] Linhas em branco - quando se cria uma class espera-se que tenha duas linhas em branco
para criar outra classe. Separar funções e deficnições de classe com duas linhas em branco;
Metodos dentro de uma classe deve ser separados com uma unica linha em branco;

[5] Imports devem ser sempre feitos em linhas separardas;  
Exemplos
# Errado
import sys. os

# certo
import sys
import os

# Não há problemas em utilizar
from types import StringType, ListType

#Caso tenha muitos imports deum mesmo pacote recomenda-se fazer: 
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# import devem ser colocados no topo do arquivo logo depois de 
# quaisquwer comentarios ou doc strings e antes de constantes ou variaveis globais  

[6] espaços em expressões e instruções
Exemplos

#Não faça:

função( algo[ 1], { outro: 2 })


#Faça
função(Algo[1], {outro: 2})

#Não faça:
algo (1)

#Faça:
algo(1)

#Não Faça:

dict ['chave'] = list [indice]

#Faça:

dict['chave'] = list[indice]

[7] Termine sempre uma instrução com uma nova linha.

"""
import this