# Estrutura de Repetição While(Estrutura de Repetição com Teste Lógico)
''' Falando sobre estruturas 'while', relembre daquele exemplo do personagem echegando ao destino pelo chão de blocos(minecraft):
O objetivo é pegar aquela maça, lembra?. Naquela estrutura usamos o 'for':
    for passos(1,10)
        passos()
    pega_maca()

Mas nem sempre saberemos o quão exato será os 'passos' do seu programa. Imagine agora, entre o personagem e a maçã e não sabemos
quantos blocos há à atingir esse objetivo, nesse caso o 'for' não será necessário e nem haverá como usa-lo. Logo, assim, substituiremos
o 'for' por 'enquanto', ou seja, enquanto não chegar à maça, continua andando e pegue ela depois desse 'laço'. Essa estrutura, chama-se,
tecnicamente de: Estrutura de Repetição com Teste Lógico.

Vamos Algoritimizar:

enquanto não_chegar_na_maça:
    passo()
pega()

#Enquanto for verdade o fato de não chegar até a maça, continua a andar.
Quando tornar-se falsa essa afirmativa, ele parará e pegará a maçã.

Ok, mas como transcrever isso para o PYTHON?
Bem simples, substitui-se o 'enquanto' por while, que tem a mesma semântica linguística.

while not apple():
    walk()
take()

Em alguns casos, o 'while' é mais versátio que o 'for', por ser mais 'abstrato' quanto a realização do programa.

Agora, voltando ao exemplo principal, imaginamos que aquele personagem,agora, tenha diversos buracos a desviar, até chegar
na bendita maçã do game. Não existe um padrão para pular, pois está irregular, ou seja, não haverá certeza de quando ele deverá
pular, já que na primeira ocasião ele pula após um bloco, na segunda, ele pula e paga a moeda, na terceira, ele anda 2 blocos
e pega uma moeda no 3 e depois pula. Entendeu, novamente, o porquê do 'for' não ser utilizado?, assim, facilitando demais nossas
vidas usando o 'while'. Beleza, vamos solucionar esse problema:

Vamos Algoritimar:

enquanto não_chegar_na_maça():
    se tiver_chão() == VERDADEIRO:
        passo()

    se tiver_buraco == VERDADEIRO:
        pula()

    se tiver_moeda() == VERDADEIRO:
        pega()

pega_maca() #Quando for FALSO a 'não chegada na maça' ele acabará com esse looping e pegará a maça.

'Saquei, entendi', porém como transcrever ao PYTHON?

while not_apple():
    if tiver_chão() == TRUE:
        passo()

    if tiver_buraco() == TRUE:
        pula()

    if tiver_moeda() == TRUE:
        pega()

Gostou?. Claro que sim, né, fala a verdade. Bem, mas não importa a praticidade ou dificuldade vamos ao momento mais esperado:
PRATICAR CÓDIGOS .'''

#Momento Prático
#Observem a diferença de usabilidade do 'while' e o 'for', em dterminados casos, é claro.

#Programa com a estrutura de repetição por variável de controle(for)
'''for c in range(1, 10):
    print(c)
print('Fim')'''

#Programa com estrutura de repetição lógica(while)
c = 1

while c < 10: #Enquanto contador for menor que 10
    print(c)
    c += 1 #Quando ele volta da repetição, somarár-se valor por valor

print('FIM')

#Mesmos resultados, nesse caso, de for e while. Preste Atenção: O while serve quando sei o limite da repetição e para
# quando não souber, já o for SOMENTE para limites definidos. Agora é com você e sua necessidade

#MAIS EXEMPLOS COM WHILE: Validação de dados desconhecidos


#Ex¹: O zero define o 'break' de nosso programa, caso for outro valor, ele funcionará até o infinito.
n = 1
while n != 0: #Só uma forma de começar o looping(n !=0, pois definimos, acima, ele sendo equivalente a 1). Quando isso
    # se tornar FALSO, o programa para de funcionar. Chamamos isso de flag(condição de parada)
    n = int(input('\033[1;4;30mDigite um valor:'))
print('FIM')

#Ex²: O SIM define o loop, caso o usuário digite o contráro, o programa PARA.
r = 'S'
while r == 'S': #Enquanto a resposta for 'S' ele causa o loop. Quando se tornar FALSA essa condição, será falsa
    n_b = int(input('Digite um valor:'))
    r = str(input('Quer continuar?[S/N]:')).upper()
print('FIM')

#Ex³: Definindo indeterminados valores de impares e pares. Desconsiderando o nosso FLAG = 0.
num = 1
cont = 0
par = 0
impar = 0

while num != 0:
    cont += 1
    num = int(input(f'{cont}º valor:'))
    #Validando Imapres e pares no looping
    if num != 0: #Desconsiderando o nosso FLAG(Condição de Parada)
        if num % 2 == 0:
            par += 1

        else:
            impar += 1

print(f'Fora digitado no total {cont} número(s): {impar} ímpar(es) e {par} par(es)')
print('ACABOU')