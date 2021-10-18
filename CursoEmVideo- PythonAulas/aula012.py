# Mundo 2: Iniciando
# Condições Aninhadas

'''Aninhadas são, basicamente, criar condições dentro de outras condições. Isso chama-se Aninhamento.
Mas ok, o que uma Condição Aninhada?
Lembra do exemplo do carro?. Pois é, nem tudo é Verdadiro ou Falso(2 possibilidades) ou direita e esquerda.
As Estruturas Condicionais Aninhadas criam mais possibilidades ao usuário , ou, como dizemos, mais caminhos nessa estrada.


Ex¹:

carro.siga()
#SEMPRE OCORREM(AO INICIAR O PROGRAMA)

Se carro.esquerda():
        carro.siga()
        carro.direita()
        carro.siga()
        carro.direita()
        carro.esquerda()
        carro.siga()
        carro.direita()
        carro.siga

    Senão se carro.direita()
        carro.siga()
        carro.esquerda()
        carro.siga()
        carro.esquerda()
        carro.siga()

    Senão:
        carro.siga():


carro.pare()
#SEMPRE OCORREM(AO FINALIZAR O PROGRAMA)

 Com essa estrutura algoritimica(passo a passo) poderemos converter a linguagem Python:


    carro.siga()
    if carro.esquerda(): #Sempre começa com if
        carro.siga()
            carro.direita()
            carro.siga()
            carro.direita()
            carro.esquerda()
            carro.siga()
            carro.direita()
            carro.siga

    elif carro.direita() #opcional( se não se). Podemos usar diversas vezes.
        carro.siga()
        carro.esquerda()
        carro.siga()
        carro.esquerda()
        carro.siga()

    else: #OPCIONAL(senão). Só podemos usar 1 vez
        carro.siga():'''

'Compreendeu?. Então chegou a hora de praticar!'


#MOMENTO PRÁTICO
nome = str(input('\033[1;4;30;43mQual é seu nome?:')).strip().upper()

if nome == 'BRENDA':
    print('\033[1;4;34mQue nome lindo\033[m!')

elif nome == 'PEDRO' or 'MARIA' or 'PAULO':
    print(f'\033[1;4;34m{nome}, Seu nome é bem popular no BRASIL')

elif nome in 'ANA CLÁUDIA JÉSSICA JULIANA':
    print(f'\033[1;33m{nome}, belo nome feminino')
else:
    print('\033[1;4;37mSeu nome é tão normal.')

print(f'\033[1;4;31mTenha um Bom Dia, {nome}\033[m')


'Trate as Condições Aninhadas como as bonecas russas(uma dentro da outra)'

