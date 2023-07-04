"""
Recebendo dados do usuário

input() significa entrada -> Todo dado recebido via input é do tipo string
Em pyhton, string é tudo que estiver entre:
- Aspas simples : 'nathalia'
- Aspas duplas: "nathalia"
- Aspas simples triplas: '''nathalia'''
"""
# - Aspas duplas triplas: """ nathalia"""

#entrada de dados
#print('Qual é o seu nome?')

nome = input('Qual o seu nome? ').title()

#exemplo de print antigo 2.x
#print('Seja bem-vindo(a) %s' % nome)

#print moderno 3,x
#print('Seja bem-vindo(a) {0}'.format(nome))

#print mais atual 3.7
print(f'Seja bem-vindo(a) {nome}')

##print('Qual é a sua idade?')
idade = input('Qual a sua idade? ')

#Processamento

#Saída de dados

#print antigo
#print('A %s tem %s anos' % (nome, idade))

#print mais moderno 3.x
#print('A {0} tem {1} anos'.format(nome,idade))

#print 3,7 versao atual

print(f'A {nome} tem {idade} anos')

print(f'A {nome} nasceu em {2022 - int(idade)}')
