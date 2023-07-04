"""
Tipo booleano vem da algebra, criada por George Boole
2 constantes, Verdadeiro(TRUE) ou Falso(FALSE), sempre com a letra maisucula

"""

ativo = True
print(ativo)

"""
Operações Básicas
"""

# Negação (not~):
# Fazendo a negação, seo valor booleano for verdadeiro o resultado será falso,
#se for falso o resultado será verdadeiro, Ou seja, ao contrário.

print(not ativo)

logado = False

# Ou (or^):
"""
 É uma opreação binária, ou seja, depende de dois valores. ou um ou outro deve ser verdadeiro,
True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

# E (and):
"""
Também uma operação binária, ambos os valores devem ser verdadeiros.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""
