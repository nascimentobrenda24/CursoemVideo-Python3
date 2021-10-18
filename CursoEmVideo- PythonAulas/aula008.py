'''Módulos- O que são?
#Imagine que você comprou um carro, mas ele vem com apenas o básico.
Logo, assim, precisamos, posteriormente, de módulos(som, ar condicionado e etc)
Entendeu?. Pra facilitar, lembre-se de você!Sim, você mesmo.
Nosso corpo é uma máquina que vem com o básico pra funcionar, mas ficamos fracos em algumas coisas adicionais, tais como:
comidas,bebidas, doces e etc. Assim que ocorre em Python. Imagina que cada 'grupo de comida' sejam
chamados no ramo de programação de bibliotecas e precisamos importa-las caso necessá-
rio.

Importações mais generalistas:
Ex¹: import bebida = importará TODAS AS BEBIDAS EXISTENTES
Ex²: import doce = importará TODOS OS DOCES EXISTENTES


Mas se eu quiser importar apenas um item ou detalhar quais eu quero:

Importações mais detalhistas
Ex³:from doce import pudim = importará APENAS o pudim


#Saindo da perspectiva mais lúdica, vamos falar da biblioteca 'math'
Ex¹: import math
        funcionalidades de math: ceil(arrendondamento pra cima)
                                floor(arredondamento para baixo)
                                trunc(Quebrar o número ao meio)
                                pow(Potência)
                                sqrt(raiz quadrada)

                                factorial(para calculo de fatorial)
Assim, quando eu digitar(import math), ele importará todas aquelas funcionalidades.
Mas se eu quiser calcular SOMENTE raiz quadrada?
    Ex²:from math import sqrt

Ok, entendi, mas eu quero fazer um programa que usa potência, raiz quadrada e quero arredondar o valor
para cima?
    Ex³: from math import sqrt, pow, ceil

Beleza, mas nada adianta só teoria. Vamos praticar!'''

#Momento Prático:

#Importação generalista
import math
num = int(input('Digite um valor:'))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é {:.1f}.'.format(num,math.ceil(raiz)))


#Importação detalhista
from math import sqrt, floor
n1 = int(input('Valor:'))
r = sqrt(n1)
print('A raiz quadrada de {} é {:.1f}'.format(n1, floor(r)))



#Ok, entendi, mas só existe essa biblioteca. E se eu quiser importar coisas diferenciadas?.
'''Bom questionamento, olha, se você acessar o site python.org e for em bibliotecas
poderás ver a diversidade de bibliotecas diferenciadas.
Testaremos algumas dessas maravilhosas bibliotecas!

Que tal 'chutarmos' valores aleatórios?

P.S.Biblioteca padrão(Já vem no Python)'''

import random
numero = random.randint(1, 10)
numero_float = random.random()
print(numero, numero_float)
        
'''E não acabou!. Funcionalidades extras no pypi da python.org mostram bibliotecas
insanas. Dentre essas temos a biblioteca 'emoji'
 Se eu escreve-la sem ter usado a mesma antes, dará um erro. Por que?.
 Bem, você precisa baixa-la na sua idle.'''

#Saiba que a biblioteca(módulo externo) emoji NÃO VEM INSTALADA NO PROGRAMA BASE assim como DIVERSAS poderosas bibliotecas
import emoji
print(emoji.emojize('Olá, Mundo :earth_americas:', use_aliases=True))#Escolher o código das reações dos emojis na pypi da python.org
