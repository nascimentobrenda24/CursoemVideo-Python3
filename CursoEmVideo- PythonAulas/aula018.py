'''# List 01
test = list()
test.append("Brenda")
test.append(16)

group = list()
# When I use the ":", actually, I copy the currently list
group.append(test[:])

# List 02
test[0] = "Heytor"
test[1] = 0.9

# When I use the ":", actually, I copy the currently list
group.append(test[:])

print(group)
'''

'''
family = [["Bia", 22], ["Brenda", 16], ["Roberta", 40], ["Marcelo", 46]]
print('A família Nascimento é composta por: ', end=' ')

for p in family:
    print(p[0], end=',')
print('\n', '=*'*40)

# Showing the databases of "family"
# Showing the "Bia" databases: specifically her name, 'cause this information is findable in zero position of this sub-list
print(f"\nA primogênita da família é {family[0][0]}, tendo {family[0][1]} anos")
print(f'A caçula é {family[1][0]}, que tem {family[1][1]} anos ')
print(f'Os pais são: {family[2][0]} com {family[2][1]} anos '
      f'e {family[3][0]} com  {family[3][1]} anos')
'''

'''
guys = list() # master list
database = list() # auxiliary list
# Total of under ages and majors in the list
total_under_age = total_major = 0

# This battery is for input informations in "database" and index in the "guys" variable
for c in range(0, 3):
    print('=*'*20)
    # Storing datas
    database.append(str(input('Nome:')))
    database.append(int(input('Idade:')))
    # Converting datas to "guys" variable
    guys.append(database[:]) # database copy all stuffs add in "database" variable. This manipulation will profitable, 'cause without it we'll, in the next code line, clear the "guys" databases, because we don't copy rhe interesting list
    database.clear() # We're cleaning the database each looping, otherwise, the old informations in looping will acumulate in the new sub-lists

print('-'*30)
# This loop is so important, because we'll analyze "each person" inside "guys" variable and will add in your respectives variables
for p in guys:
    # If the data in 1º position, whose it's where the years data are save, bigger or equal to 21
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        total_major += 1
    else:
        print(f'{p[0]} é menor de idade')
        total_under_age += 1
print('-'*30)

print(f'Há {total_major} maiores de idade' if total_major > 1 else f'Há {total_major} maior de idade')
print(f'Há {total_under_age} menores de idade' if total_under_age > 1 else f'Há {total_under_age} menor de idade')
'''