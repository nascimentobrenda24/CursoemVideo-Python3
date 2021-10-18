#Condições(Parte 1)
'''Estruturas Condicionais:Condições compostas e simples

O que são Condições?
Imagine que você viajará e a estrada é cheia de curvas e nada reta. Logo, teremos que
 pegar nosso objeto carro e criar os métodos.

 carro.siga()
 carro.esquerda()
 carro.siga()
 carro.direita()
 carro.siga()
 e etc.
São sequênciais. Conjuntos de passos(de cima para baixo), logo apenas executando SEM POSSIBILIDADES, assim quando
não executado FIELMENTE não chegaremos ao 'lugar'

Mas, agora, faremos diferente. Imagine que em outra estrada temos duas entradas a mesma chegada.
Se o carro vira a esquerda, ele deve seguir, passar para esquerda, seguir e etc.
Se o carro vira a direita, ele deve seguir, ir a direita, seguir e etc.

O caminho da direita soa mais fácil, logo segui-lo pode ser bom.
Pra isso que servem as CONDIÇÕES. São basicamente 2 programas ou + dentro de 1.

Vamos deixar em forma de algoritimo:

carro.siga()#Anda
Se carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
Senão
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
carro.pare()

Temos um bloco de Verdadeiro e um de Falso.
Para o Python é diferente, mas minimalista:

if carro.esquerda():
    bloco True


else:
    bloco False



Ou será o True ou o False a ser executado. NUNCA OS DOIS JUNTOS SERÃO EMULADOS!.

Vamos de exemplo:

    Ex¹: tempo = int(input('Quantos anos tem seu carro?'))
         if tempo <=3: #menor ou igual a 3
            print('Carro Novo')

        else:
            print('carro velho')

            ou

        print('carro novo' if tempo<=3 else 'carro velho')


Ah, sim, entendi. Que tal Praticar?'''



#Momento Prático

#Condição Simples

nome = str(input('Seu Nome:'))
if nome =='Brenda':
    print('Que nome lindo você tem! ')#Só ocorre caso for BRENDA

#Condição Composta
else:
    print('Seu nome é tão feio!')

print('Bom dia, {}'.format(nome))  # Sempre ocorre


n1 = float(input('Nota da 1ª av:'))
n2 = float(input('Nota da 2ª av:'))
m = (n1+n2)/2
print('A sua média foi {}:.1f')
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média foi ruim!. ESTUDE MAIS!')

#print('PARABENS' if m>=6 else 'ESTUDE MAIS')

