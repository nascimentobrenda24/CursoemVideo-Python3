# Manipulando Textos
'''Tratar cadeias de caracteres é algo muito importante, sabia?.
Nessa nona fase aprenderemos a manipular textos.
Mas espera ai!. O que é uma Cadeia de Caractere ou String?.
Toda linguagem de programação trata: 'CURSO EM VIDEO', essa palavra, como uma string ou uma cadeia de
caractere.
Lembra daquela frase que citamos acima: CURSO EM VIDEO, colocaremos
em uma variavel do tipo string.
    Ex¹: frase = 'Curso em Video Python'

O que o Python faz com esses dados?. O Python cria mini espaços dentro da memória do pc(até mesmo o espaço).
Vai de 0 até 20, nesse caso.

Com esse tratamento que o Py e outras linguagens fazem, fica fácil de fazer operações
com esses caracteres ou strings.

1) FATIAMENTO DE STRING
    frase[9]= identifica dentro da cadeia de caracter a décima letra(por causa
    dos espaços e por começar por 0). Nesse caso, a 10 letra é 'V'.

    frase[9:13] = Capta do V até o E(Não no '0', pois pro Py, onde termina ele exclui):Resultado = Vide
    frase[9:21] = Capta do V até o 0, já que ele ignora a última 'casa. Resultado = Video Python'

    frase[9:21:2] = Fatia de 9 a 21, porém pulando de 2 em 2. Resultado = VDOPTO

    frase[:5] = Fatia de 0 a 5, quando eu omito a parte da frente, ele vai do inicio até o 5. Resultado: Curso

    frase[15:] = Fatia de 15 até o fim do caractere. Resultado:Python

    frase[9::3] = Fatia de 9 ao fim, já que omiti o valor do meio, todavia pulando de 3 em 3. Resultado: VEPH

2) Análise
É basicamente você saber com que letra começa ou terminar, largura e etc.

    len(frase) = Comprimento do caracter = 21 caracteres

    frase.count('o') = Quantas vezes aparece esse 'o' minusculo = 3vezes
    frase.count('o',0,13) = Quantas vezes aparece esse 'o' minúsculo do inicio
    a 13(contagem com fatiamento) = 1 vez, pois o 13 é ignorado.

    frase.find('deo') = Qunatas vezes encontrou 'deo' no caracter. Resultado: 11(começa no 11)
    frase.find('Android') = Resultado: -1(inexistente)

    'Curso' in frase = Significa: 'Há Curso nesse caracter?'. Resultado: TRUE


3) Transformação
Uma lista de string é imutável, mas consegue modificar por métodos.

    frase.replace('Python', 'Android') = Substituir Python por Android, assim, ficando CURSO EM VIDEO ANDROID

    frase.upper()= UPPER(MAIÚSCULO). Resultado: CURSO EM VIDEO PYTHON(Tudo em maiusculo)

    FRASE.lower()= lower(minúsculo). Resultado: curso em video python

    frase.capitalize()= Transforma uma 'string' inteira e por tudo em minúsculo, exceto
    o primeiro caractere. Resultado: Curso em video python

    frase.title() = Semelhante ao 'capitalize', o 'title', analisa quantas palavras há,
    pulando os espaços, assim ficando apenas os caracteres iniciais das palavras em maiúsculo.Resultado: Curso Em Video
    Python.

    frase.strip() = Remove os espaços insignificantes. Claro que o espaço ao meio das palavras NÃO
    serão ignorados, já que a funcionalidade deles é separar 'strings'.

    frase.rstrip() = Remove os espaços do lado 'right', ou seja, o lado direito.

    frase.lstrip() = Remove os espaços do lado 'left', ou seja, o lado esquerdo.

4) Divisão de Strings

        #Há mais funções para o 'split': PESQUISE
        frase.split() = Ocorre uma divisão da strings, assim a transformando em uma lista.
        Resultado: (Curso)0,1,2,3,4 (Em)0,1 (Video)0,1,2,3,4 (Python)0,1,2,3,4,5 *Muda até a numeração das palavras

        '-'.join(frase) = Juntará todos elementos da frase e usará o '-' como separador.
        Resultado: Curso-Em-Video-Python


Mas como nós todos sabemos, nem só de Teoria vive um homem. Praticar é mais que necessário!.'''


#Momento Prático

#Fatiamento
frase = 'Curso em Vídeo Python'
print(frase[:14])

print(frase[1:15:2])# De um a 15 de 2 em 2
print(frase[::2])# Do 0 ao fim de 2 em 2
print(frase.count('o'))# Procurar nos meus caracteres o 'o'. P.S. Ele encontrará o minúsculo caso não coloque em CapsLock.
print(frase.upper().count('O'))# Deixará tudo em maiusculo, logo dará o mesmo resultado de acima, pois ele conta com aqueles
#mesmos 'o', só que agora maiúsculo
print(len(frase.strip()))#Largura do caracter sem espaços(strip)
print(frase.replace('Python', 'Android'))#Troca Py por AD
#Replace modifica apenas naquela circustância, logo sua variável ainda é Curso em Video Python.
print(frase.find('Vídeo'))
print(frase.split())#Cria uma lista com separador de espaços

dividido = frase.split()
print(dividido[2])#Vai na separação 2 e pega a string inteira
print(dividido[2][3])#Pega na separação 2 a terceira palavra



