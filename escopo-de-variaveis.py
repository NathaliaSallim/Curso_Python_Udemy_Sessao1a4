'''
escopo de várialveis

Dois casos de escopo;

1- Variáveis globais;
   são reconhecidas, ou seja, seu escopo compreende todo o programa

2 - Variáveis locais ;
    são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao
    bloco onde foi delcarada,

    Para declarar variáveis em python utlizamos:
    nome-da-variavel = numero-da-variavel = 42
    Ex: abaixo

PYTHON É LINGUAGEM DE TIPAGEM DINAMICA : SIGNIFICA QUE AO DECLARARMOS UMA VARIÁVEL
NÃO PRECISA COLOCAR O TIPO DE DADO DELA.
ESTE TIPO É INFERIDO AO ATRIBUIRMOS O VALOR A MESMA

EXE EM C:
int numero = 42;

Exemplo em Java:
Int numero = 42;
'''

numero = 42 #Exemplo de variavel global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

numero = 2
if numero > 10:
    novo = numero + 10 # A variavel novo está declarada dentro do if, portanto é variavel local
    print(novo)

print(novo)
