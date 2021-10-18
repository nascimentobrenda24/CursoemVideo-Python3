# Laço de Repetição(Parte 3)
'''Normalmente, as linguagens de programação tem 3 tipos de Estruturas de Repetição/Interação, cujas geralmente são, dependendo
da linguagem: While, For e Repeat ou o Do While. Todavia, o Python distoa dessa conjuntura, ele possue apenas o (while e o for),
porém isso não significa que não há possibilidade de haver representação da estrutura Do While, em python.
Então vamos ao que interessa:

Na aula 014 aprendemos a usar de forma sagaz a Estrutura de Repetição com Teste Lógico. Nela, havia uma situação que havia um personagem, no
qual tinha a enfrentar um caminho volátil e cheio de obstáculos e recompensas(maça e moedas) e enquanto não chegasse na moeda,
ele seguiria um caminho que tinha primeiramente um obstáculo, posteriormente pegando moeda e assim evidenciando esse loop.

Ex¹: Algoritimo da aula014
    while não maçã:
        if chão:
            andar()

        elif abismo:
            pular()

        elif moeda()
            pegar()

    pega() #No fim, quando o fato de não pegar a maçã for FALSO, ele pega-a.

Agora, imaginemos uma situação um pouco distinta:
Imagine, aquele mesmo personagem, naquela situação de obstáculos,abismos, moedas e a tão sonhada maçã, entretanto o que distoa, nesse
caso, é o fato de no terceiro chão, ao passar os abismos, haver uma plataforma flutuante, na qual tem um TROFÉU. Ok, mas
é a mesma coisa, mesmo algoritimo, é só criar mais uma linha de 'if'. Não, nesse ponto que te enganas, esse troféu majoritariamente
tem o intuito primordial de 'zerar o game', entende?. Calma, explicarei melhor: Imagine que pegando a maça, as moedas...
sejam objetivos secundários, claro, um é mais almejado que o outro, entretanto ao pegarmos o GRANDE TROFÉU, o jogo finaliza, pois
o personagem, digamos assim, zerou a vida sua vida e será congratulado por isso. Agora melhorou, né?.
Agora pense comigo, se usarmos aquela mesma codificação anteposta, o personagem passará e nem 'notará' o troféu, pois está programado
a pegar maçãs a finalizar o game. Logo, é imprescíndivel fazermos a seguinte modificação: Retiramos o 'enquanto não maçã' e
só colocaremos 'while infinito', criamos um loop infinito, posteriormente acrescentamos mais uma linha de 'if', dizendo: se
houver troféu, pularemos na plataforma e pegaremos o troféu. Porém, isso não é autosuficiente, pois lembre que esse loop é
infinito, logo ao pegarmos o trófeu nada mudará e sim rodará a toda eternidade, ou até teu pc explodir. Ok, então devemos acrescentar
naquele nosso 'if trófeu' um comando novo que terá a potência semântica 'stop', ou seja, 'FIM DO JOGO', ele cumprira sua
missão. Bem, vamos representar isso melhor aqui abaixo, naquele nosso código da aula014:

Ex²: Agoritimo Lógico(Portugol)

enquanto Verdadeiro:
    se chão:
        passo()

    se abismo:
        pula()

    se moeda:
        pega()

    se trófeu
        pula()
        interrompa # Esse 'interrompa' jogará o programa pra parte abaixo, fora da identação, assim finalizando o programa.

pega()


Ok, entendi tudo, mas como fica em Python?

Ex³: Agoritimo sintaxe Python
while True:
    if chão:
        passo()

    elif abismo:
        pula()

    elif moeda:
        pega()

    elif Trófeu:
        pula()
        break

pega()

Analisando o código, vemos que se não chegar no trófeu, ele rodará eternamente(infinity loop) até chegar no nosso 'break'.
Pense assim, quando ele chega no 'break', ele joga para a posição não identada final(pega) e PARA O PROGRAMA.

Eai?. Entendeu, senão volte a ler e estudar, pois agora iremos a melhor parte: PARTE PRÁTICA
'''

#Momento Prático

# Aquele básico contador em while(loop finito)
'''cont = 0
while cont <= 10:
    print(cont, '->', end='')
    cont += 1 # Responsável pelo fim do loop e pelo exibicionismo de 0 até 10 no laço.
print('Acabou')'''

# Mas se eu por 'while True: ..., ele rodará para sempre. Experimenta ai!
# Resultado ao trocar 'cont <= 10' por 'True': 1234905 1829439 53783... infinitos valores.

# Para que tal problemática não ocorra, chamamos o nosso 'break' a dar aquele stop que o quadradinho vermelho da Pycharm
# fez para teu PC não bugar.

# Usando Flags(Enquanto diferir de 999):
'''n = 0
while n != 999: # Meu FLAG=999
    n = int(input('Digite um número:'))
'''

# Ok, mas olha esse problema que requisitará o 'break'.
# Aqui queremos somar tudo, menos o nosso flag.
'''n = s = 0
while n != 999:
    n = int(input('Digite um número:'))
    s += n'''
#Usando gambiarra a consertar esse erro:
'''s -= 999'''
# Agora tu ficastes satisfeito com isso, né?, sinto desapontar-te, mas isso é uma extrema 'gambiarra' desnecessária na
# programação, porquê há dois basilares erros: sua variável('s') continua com valor errado, pois soma os números com o meu
# FLAG e o meu Teste Lógico não está cumprindo sua função adequadamente.
'''print(f'A soma vale {s}') # Mostrando a soma no fim do programa'''


# Melhorando o código usando o break a solucionar tal impasse:
n = s = 0
while True: # Criamos um loop infinito
    n = int(input('Digite um número:'))
    if n == 999: # Se número for 999, ele para e vai mostrar a soma, na qual não terá sua participação, pois a 's += n',
        # está no loop infinito de números possíveis e não no 999.
        break # Nosso 'PARA'
    s += n # A variável 's', somará somente se diferir de 999.

print(f'A soma vale {s}')

# Assim, teremos um código limpo e uma variável com o valor correto e não uma gambiarra.

