# Variável simples
'''
 Uma situação de requisito de um hambúrguer e suco somente usando o
conceito de variáveis simples

lanche = "suco"
lanche = "hamburguer"

print( lanche ) # Não haverá um valor certo e muito menos ambos aparecerão
Afinal, se somente há um único espaço na memória do computador, dois valores não caberão

# Mostrar valores em ordem crescente
# Mostrar o primeiro valor ( utilizando os índices )
# Mostrar a quantidade de itens ( len )


#           0             1        2        3
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

print(lanche[-2]) # As últimas posições são simbolizadas pelo negativo "-"
# e seu resepctivo valor
# Output¹: pizza ; pois está na 2 última posição, de trás para frente

print( lanche[0] ) # Output²: hamburguer
print( len(lanche)) # Output³: 4 -> na súmula são quatro elementos de 0 a 3

lanche = ( "hamburguer" , "suco" , "pizza", "pudim" )
# Aqui haverá uma entrada e saída de cada elemento de "lanche"
# nessa variável de controle "c"
for c in lanche:
	print( c )

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
lanche[1] = 'refrigerante'
print(lanche)

# Output: TypeError: 'tuple' object does not support item assignment

# Escolher os lanches
lanche = ( 'hamburguer' , 'suco', 'pudim' , 'pizza', 'Batata Frita' )

# Primeira Solução ( "range" )
for c in range ( 0, len(lanche))
	print(f'Eu vou comer {lanche[cont]}
# Segunda Solução ( Variável direta )
for comida in lanche:
	print(f'Eu vou comer {comida}')

print('Comi pra caramba')

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for pos, comida in enumerate(lanche):
	print(f'Eu vou comer {comida} na posição {pos} )

lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'Batata Frita')

print(sorted(lanche)) # Virou uma lista para mostrar em ordem alfabética
print(lanche) #provando que a tupla é a mesma

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a

print(f'A + B = {c}')
print(f'B + A = {d}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(len(c))
# Output: 7

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(c.count(5))
# Output: 2

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)

print(c.index(5))
print(c.index(5, 1)) # requisita a posição de 5 a partir do índice 1

Output:
( 5, 8, 1, 2, 2, 5, 4 ) 
0
5


pessoa = "Brenda", 16, "F", 45.5
del(pessoa[0])
print(pessoa)

# Output: TypeError: 'tuple' object doesn't support item deletion

'''