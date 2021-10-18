# Estrutura de repetição for
'''Aprenderemos uma nova categoria de estruturas de controle no PYTHON, outras linguagens também: laços/repetições/itera-
çoões, chame do que quiser. Então, assim sendo, vamos para TEORIA:

Imagine uns bloquinhos, seu chão, haverá 6 desse e nele, imagine, um personagem e a 'recompensa', uma maçã, 5 chãozinhos
depois. Vamos tentar chegar até lá.

Vamos algoritimizar:

    personagem.passo()
    personagem.passo()
    personagem.passo()
    personagem.passo()
    personagem.passo()
    personagem.passo()
    personagem.pegar_maca()

Bem simples, né?. Porém as repetições são evidentes e cansativas(imagine 1000 passos nessse game).
Por isso, as estruturas de controle, no caso, de repetições for é imprescíndivel a um código LIMPO e legível.

Vamos algoritimizar:
    Personagem dará 11(0,10) passos agora:

    laço_passo(imagine uma bolinha com setas infinitas = personagem.passo())
    #Se eu fizer isso ele andará até cair. Logo, terei de por um limite nessa repetição!
    #Cada chãozinho terá de 0 a 10, no caso.

    laço_passo(0, 10)
    #Quando chegar no 10 ele para e nada faz.
    #Vamos pegar a fruta
    laço_passo(0, 10):
    pegar()


Vamos melhorar isso escrevendo em português a poder passar para o PY.

#criarei um laço com uma variavel c(contador) no intervalo de 1 a 10
laco c no intervalo(1, 10)
    passo #dentro da identação do laço. Ocorrerá 10X
pega #pegar a maça está fora do laço, logo pegará 1 vez.


Ok,entendi a lógica, mas como escrever em python?
Simples:

for c in range(1, 10):
    passo()
pega()

Vamos criar outras situações. Lembra daquele personagem que queria pegar a maçã?, poisé, ele agora tem obstáculos a frente, nessa fase.
Imagine, que temos aquele chãozinho, como costumo a falar, mas a cada dois blocos desse chão há um abismo. Se ele simplis-
mente for repetir aqueles passos, ele cairá nesses abismos, logo precisamos intervir nessa ocasião, criando, assim, inter-
rupções, ou nesse contexto, pulos:

passo()
pula()
passo()
pula()
passo()
pula()
passo()
pega()

Repetitivamente digitamos(passo e pula). Logo, criaremos um laço para legibilizar nosso script.
Porém, limitaremos a quantidades de pulos e passos, para não ocorrer infinitamente.


laço c no intervalo(0,3)
    #Ocorrrerá 3 vezes até o personagem chegar na maçã
    passo()
    pula()
#Fora da identação, pois ocorrerá apenas 1 vez que o laço acabar
passo()
pega()

Bem mais legível, né?. Vamos transcrever para PYTHON:


for c in range(0,3):
    passo()
    pula()
passo()
pega()

Vamos para 3ª, e última, situação. Agora, novamente, imagine, aquele personagem e toda situação acima. Todavia, além da
captura de maças, haverá captura de moedas. Porém haverá apenas 2 chãozinhos que possuirão moedas:
O primeiro, ele pulará e pegará, no outro não pega, pois não há, e no terceiro capture a moeda e a maça.
Viu que eu tenho que pegar moedas só se elas existirem?. Assim, acredito, que já 'matastes a charada' e tens ciência que
precisaremos de um laço de condição dentro de um laço de repetição:

Vamos algoritimizar:

laco c no intervalo(0,3):
    se moeda == VERDADE:
        pega()# Esse 'pega' diferencia-se dos outros por estar dentro de uma estrutura de repetição, porém será acionado
        APENAS se a moeda existir, sacou?
    passo()
    pula()
    passo()
    pega()
    #Já esses outros ocorrem 3X sem condições a ocorrerem e pararão, tal como o outro também, em um momento.

Percebeu como um código é estritamente estruturado para solucionar problemas?. Lembra até aquela bonenequinha russa(aglutinando
uma peça dentro da outra). Ou seja, ratifica-se o poder de pôr uma estrutura de condicional dentro dela mesma ou dentro de uma estrutura de
repetição.

Como converter para PYTHON?

for c in range(0,3):
    if moeda:
        pega()
    passo()
    pula()
passo()
pega()

Agora que sabemos todo a parte conceitual, vamos para a PRÁTICA:
'''

#MOMENTO PRÁTICO

#Quero repetir um 'OI':
print('=*'*20, 'FORMA Nº1', '=*'*20)
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('=*'*20, '=*'*20)

#Dá um trabalhão escrever mais de 4 vezes, imagine 10000000 vezes. Logo, vem a ESTRUTURA DE CONTROLE DE REPETIÇÃO A NOS
# SALVAR
print('=*'*10, 'FORMA Nº2(ESTRUTURA DE CONTROLE DE REPETIÇÃO FOR)', '=*'*20)

#P.S. A VÁRIAVEL C PODE SER O QUE TU QUISERES
for c in range(0, 100):
    print('Olá Mundo!!')
print('FIM')

#MOSTRANDO VALORES(CRESCENTES)
print('=*'*20, 'FORMA Nº3(MOSTRANDO NºS PELA VÁRIAVEL DE CONTROLE)', '=*'*20)
for c in range(0, 11): #até 10, pois ele ignora o último:
    print(c)
print('FIM')

#MOSTRANDO VALORES(DECRESCENTES)
print('=*'*20, 'FORMA Nº4(MOSTRANDO NºS DECRESCENTES PELA VÁRIAVEL DE CONTROLE)', '=*'*20)
for c in range(6, 0, -1): #-1 = PULAR DE 1 EM 1. Se fosse -2, em 2 em 2
    print(c)
print('FIM')

#CRIANDO VARIAVEIS E INDUZINDO CONTAGENS NO FOR
print('=*'*20, 'FORMA Nº5', '=*'*20)

n = int(input('Digite um Número:'))
for c in range(0, n+1): #n+1, para ele credibilizar mais uma casa e mostrar o valor como conhecemos
    print(c)
print('FIM')
#se eu puser uma vírgula e um valor(-1,-2 e etc) ele pulára, também, de casa em casa.

#DEIXANDO MAIS COMPLEXO E DEIXANDO O ÚSUARIO DECIDIR ONDE COMEÇA,TERMINA E QUANTOS PASSOS DARÁ DE UM NÚMERO A OUTRO
print('=*'*20, 'FORMA Nº6', '=*'*20)

i = int(input('Qual Valor Inicia?:'))
f = int(input('Qual Valor Terminar?:'))
p = int(input('Quantos Passos Dará Entre Início e Fim?:'))

for c in range(i, f+1, p): #inicio, fim+1, passos
    print(c)
print('FIM')

#REPETINDO INPUT'S, ASSIM, LEGIBILIZANDO E OCUPANDO MENOS ESPAÇOS
s = 0
for c in range(0, 4):
    n = float(input('Digite um número:'))
    s += n# mesma coisa de s = s+n. MELHOR A SE FAZER.
print(f'O SOMATÓRIO DE TODOS OS VALORES FOI {s}')

