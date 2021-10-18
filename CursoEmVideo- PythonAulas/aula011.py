#Cores no Terminal(Encerrando o Mundo 1- Fundamentos)
# Aula Extra

'''Por que colorir o terminal?. Cá entre nós, ficará muito mais bonito e legal.
Ok, mas como introduzir cores nos meus progrmas ?. Bem, temos o Padrão ANSI(escape sequence)
Como funciona esse código ANSI?. Olha, toda vez, em python, que quiseres representar cores iniciamos com(\033['preencheremos com códigos de cores'm

Estrutura do código:
Estilo, cor do texto e cor de fundo(3 valores). São opcionais. Pode por 1 e não por outro
\033[style; text; back m

Quais são os códigos a escrever?

1)Style:
    0 - Sem estilo
    1 - Em Negrito
    4- Underline(Sublinhar)
    7- Negative( Inversão de cores)

2) Text
    30 - Branco
    31 - Vermelho
    32 - Verde
    33 - Amarelo
    34 - Azul
    35 - Roxo
    36 - Azul Marinho
    37- Cinza

3) Back
    40 à 47 com as cores do Texto, só que no background(fundo)


Ex¹: \033[0;33;44m = 0:caracteres sem estilo, 33 = verde, 44 = fundo azul e m para finalizar.

Exemplos Finais:'''

'''#O(sem estilo nenhum) é opcional
print('\033[0;30;41mTeste')#Vermelho no background e branco no texto
print('\033[4;33;44mFesta em[m Ipanema, meu amor!')# Amarelo nas letras, com estilo sublinhado e fundo amarelo
print('\033[1;35;43mCurso Em Vídeo Python')# Fundo Amarelo, letras em roxo e sublinhadas
print('\033[30;34mProgramação é 10!')# Amarelo no background, letra em azul e sublinhada
print('\033[7;30m Be a programmer! ')# Inversão de cores
'''

# Momento Prático
print('\033[7;30mOlá, Mundo!\033[m')
print('\033[1;4;34;43mProgramar é VIDA!\033[m')

#OBS: módulo colorize tem mais cores. PESQUISE!


#Ex¹:
print('=*'*200)
a = 3
b = 5
print(f'Os valores são \033[32m{a} e \033[31m{b}\033[m !!')
# a variavel 'a' terá a cor amarela e a 'b' terá a cor vermelha
print('=*'*200)

#Ex²:
nome = str(input('Seu Nome:'))

#Podemos criar nossa própria lista de cores que usaremos. Em alguns casos, muito útil, pois minimaliza e deixa legível
#o código.
cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[7;30m',
         'preto_branco': '\033[7;30m'}

escolha = str(input('\033[1;4;30mQual cor tu queres o teu nome?\033[m')).upper()
print('Olá. Muito prazer em te conhecer,{}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))




