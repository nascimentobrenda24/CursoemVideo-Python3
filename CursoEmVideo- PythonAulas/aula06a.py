#Tipos primitivos e Saída de dados


n1 = float(input('Digite um valor:'))#ou int ou float serve.Todo int é float,mas nem todo float é int
n2 = float(input('Digite outro:'))
s = n1 + n2
#print('A soma entre',n1,'e',n2,'é',s). Sintaxe feia e ultrapassada
print('A soma entre {0} e {1} é {2}'.format(n1, n2, s))# Sintaxe bela e atual
