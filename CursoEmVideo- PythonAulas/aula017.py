'''num = [2, 5, 9, 1] # Creating a list

# Additions, Replaces and Reverses in list
num[2] = 3 # replacing the value in position 2 with the value 3
num.append(7) # Adding a 7 value in final position
num.sort(reverse=True) # Reversing the tuple position'''
'''num.insert(2, 0) # Exchanging the value of the key 2 with the number 0
'''
'''num.insert(2, 2) # Same thing as the top command, but with a existence element (2)
# Removing values'''
'''num.pop()  It'll clear the element of the last key
num.pop(2) # If the position was invoked, now the 2 position will be 0, after all with the sorted
# method the list was inverted, the 0 element will be clear
'''
'''if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')

print(num)
print(f'Essa lista tem {len(num)} elementos') # the size of this list
'''
'''
values = []
for x in range(1, 5):
    values.append(int(input('Digite um valor: ')))


# Adding values in my list
values.append(5)
values.append(9)
values.append(4)

print(values)
# Well, but I wanna organize my values
# Position c
# Value v
# enumerate methode serves for count the times of the elements of the list
for c, v in enumerate(values):
    print(f'\nNa posição {c+1} encontrei o valor {v}', end=' ')# c+1 'cauz the basis of pyton is to count first 0 and not 1

print('\n\nCheguei no fim da lista!')
'''
''' 
# When you equal both lists, we have not a copy of a to b, but a connection between these
# Then, if you modify any lists, the final result will be equal to these both
a = [2, 3, 4, 7]
b = a
# Though of the connections with lists be underlying, we can copy a list and manipulate this as we want
c = a[:]
# Manipulations
b[2] = 8 # It will be to both lists, 'cauz are equal (a and b)
c[2] = 5 # Just c, 'cauz it is just a copy of a

print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C (Cópia Modificada De A): {c}')
'''

lanche = ["hamburguer", "pera", "uva", "suco", "refrigerante"]

lanche.remove("hamburguer")

print(lanche)
