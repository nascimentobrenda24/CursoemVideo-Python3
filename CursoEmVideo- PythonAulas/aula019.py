estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['initials'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # .copy() is a dictionary world version of "[:]" in the lists, because this command is
    # for copy the element declared

for s in brasil:
    for v in s.values():
        print(f'{v}', end=' ')
        print()

