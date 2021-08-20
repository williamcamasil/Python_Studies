

# -------------------------------------------------------------------

# 035
# la = int(input('Insira o tamanho do 1° lado: '))
# lb = int(input('Insira o tamanho do 2° lado: '))
# lc = int(input('Insira o tamanho do 3° lado: '))
#
# lat = False
# lbt = False
# lct = False
#
# maior = -1000;
#
# if(la > maior): maior = la
# if(lb > maior): maior = lb
# if(lc > maior): maior = lc
#
# if(maior < (lb + lc)):
#     lat = True
#
# if(maior < (la + lc)):
#     lbt = True
#
# if(maior < (lb + la)):
#     lct = True
#
# if(lat == True & lbt == True & lct == True):
#     print('Será possível fazer um triangulo')
# else:
#     print('Não será possível fazer um triangulo')

# -------------------------------------------------------------------

# 033
# n1 = int(input('Insira o 1° número: '))
# n2 = int(input('Insira o 2° número: '))
# n3 = int(input('Insira o 3° número: '))
#
# menor = 1000;
# maior = -1000;
#
# if(n1 > maior): maior = n1
# if(n2 > maior): maior = n2
# if(n3 > maior): maior = n3
#
# if(n1 < menor): menor = n1
# if(n2 < menor): menor = n2
# if(n3 < menor): menor = n3
#
# print('O maior valor é {} e o menor é {}'.format(maior, menor))

# -------------------------------------------------------------------

# 032
# ano = int(input('Digite o ano: '))
#
# if (ano%4==0 and ano%100!=0) or (ano%400==0):
#     print('Bissexto')
# else:
#     print('Não é bissexto')

# -------------------------------------------------------------------

# 028
# import random
# vlr = random.randrange(5)
# numero = int(input('Insira um número de 0 a 5 para ver se você esta com sorte: '))
# if(vlr == numero):
#     print('Acertou na mosca, ambos os número são {} e valor {}'.format(numero, vlr))
# else:
#     print('Errou feio o número escolhido {}  não é igual ao número randomico {}'.format(numero, vlr))


# -------------------------------------------------------------------

# 027
# fullName = input('Digite seu nome completo: ')
# splitFullName = fullName.split()
#
# print('Ex: {} \nprimeiro: {} \núltimo: {}'.format(fullName, splitFullName[0], splitFullName[len(splitFullName)-1]))

# -------------------------------------------------------------------

# 026
# frase = input('Escreva uma frase: ')
# qtdCaracterA = frase.upper().count('A')
# finded = True
#
# fraseSemEspaco = frase.strip()
#
# for i in range(0, len(fraseSemEspaco)):
#     if((fraseSemEspaco[i].upper() == 'A') & (finded == True)):
#         startPositionA = i+1
#         finded = False
#
#     if (fraseSemEspaco[i].upper() == 'A'):
#         endPositionA = i+1
#
# print('A frase {} tem {} caracteres A, e começa na posição: {} e aparece a última vez na posição: {} '.format(frase, qtdCaracterA, startPositionA, endPositionA))

# >>>>>> OTHER OPTION <<<<<<<<

# frase = str(input('Digite uma frase: ')).upper().strip()
# print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
# print('A 1° letra A apareceu na posição {}'.format(frase.find('A')+1))
# print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))

# -------------------------------------------------------------------

# 025
# nome = input('Digite seu nome: ')
# silvaTrue = nome.upper().find('SILVA')
#
# if(silvaTrue != -1):
#     print("Seu nome {} contém SILVA".format(nome.upper()))
# else:
#     print("Seu nome {} não contém SILVA".format(nome.upper()))

# -------------------------------------------------------------------

# 024
# city = input('Digite o nome da sua cidade: ')
# startCity = city.split()
#
# if(startCity[0].upper() == 'SANTO'):
#     print('A CIDADE {} COMEÇA COM SANTO'.format(city.upper()))
# else:
#     print('A CIDADE {} NÃO COMEÇA COM SANTO'.format(city.upper()))

# -------------------------------------------------------------------

# 023
# number = input('Digite um número de 0 a 9999: ')
#
# if(len(number) < 4):
#     tm = len(number)
#     tempnumber = number
#     if(tm == 1):
#         number = '000' + tempnumber;
#     if (tm == 2):
#         number = '00' + tempnumber;
#     if (tm == 3):
#         number = '0' + tempnumber;
#
# print('unidade: {}'.format(number[3]))
# print('dezena: {}'.format(number[2]))
# print('centena: {}'.format(number[1]))
# print('milhar: {}'.format(number[0]))

# >>>>>> OTHER OPTION <<<<<<<<

# num = int(input('Informe um número: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
#
# print('Analisando o número {}'.format(num))
# print('Unidade: {}'.format(u))
# print('Dezena: {}'.format(d))
# print('Centena: {}'.format(c))
# print('Milhar: {}'.format(m))

# -------------------------------------------------------------------

# 022
# fullName = input("Digite seu nome completo: ")
# upperFullName = fullName.upper()
# lowerFullName = fullName.lower()
# lenWithoutSpaceFullName = len(fullName.replace(" ", "")) #verificar pq esta contando o espaço
# splitFullName = fullName.split()
# lenSplitName = len(splitFullName[0])
#
# print("Nome completo: {} \nNome UPPER: {} \nNome lower: {} \nNome tamanho sem espaço: {} \n1° Nome tamanho: {} ".format(fullName, upperFullName, lowerFullName, lenWithoutSpaceFullName, lenSplitName))

# -------------------------------------------------------------------

# frase = 'Curso em Video Python'
#
# print(frase[2:])
# print(frase[1:15])
# print(frase[::2]) #pulando de 2 em 2
# print(frase.count('0'))
# print(frase.upper().count('O'))
# print(len(frase.strip())) #Verificando tamanho sem espaços iniciais e finais
# print(frase.replace('Python', 'Android'))
# print('Curso' in frase) #Verificando se existe curso dentro da frase
# print(frase.find('Curso'))
# print(frase.lower().find('vídeo'))
# print(frase.split())
#
#
# Imprimindo o texto inteiro
# print("""lorem ipsum hurita osaina plato mendes justin monyr
# orem ipsum hurita osaina plato mendes justin monyr
# orem ipsum hurita osaina plato mendes justin monyr""")

# -------------------------------------------------------------------

# 21 mp3 player
# import pygame
#
# pygame.init()
# pygame.mixer.music.load('song.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()

# -------------------------------------------------------------------

# 20 - ordem de apresentação
# import random
# n1 = input('Digite o nome do 1° aluno: ')
# n2 = input('Digite o nome do 2° aluno: ')
# n3 = input('Digite o nome do 3° aluno: ')
# n4 = input('Digite o nome do 4° aluno: ')

# lista = [n1, n2, n3, n4]
# escolhidos = random.shuffle(lista)
# print('A ordem de apresentação será: {}'.format(escolhidos))

# -------------------------------------------------------------------

# 018 - cosseno, seno e tangente
# from math import radians, sin, cos, tan


# angulo = float(input('Informe o ângulo: '))
# s = sin(radians(angulo))
# c = cos(radians(angulo))
# t = tan(radians(angulo))

# print('O calculo do ângulo {}°: \n COS = {:.2f} \n SEN = {:.2f} \n TANGENTE = {:.2f}'.format(angulo, c, s, t))

# -------------------------------------------------------------------

# 017 - catetos e hipotenusa
# import math

# co = float(input('Insira o valor do cateto oposto: '))
# ca = float(input('Insira o valor do cateto adjacente: '))
# hyp = math.sqrt(co**2 + ca**2)
# print('A hipotenusa vai medir: {:.2f}'.format(hyp))

# -------------------------------------------------------------------

# 016
# import math

# num = float(input('Digite um número: '))
# numint = math.trunc(num)

# print('O número digitado é {} e o inteiro dele é {}'.format(num, numint))

# -------------------------------------------------------------------

# import emoji

# print(emoji.emojize("Olá mundo :sunglasses:", use_aliases=True))
# print(emoji.emojize('Python es :pulgar_hacia_arriba:', language='es'))

# -------------------------------------------------------------------

# import math (ceil / floor / trunc / pow / sqrt / factorial)
# ex.: import math
# or : from math import sqrt

# import math
# OR
# from math import sqrt

# num = int(input('Digite um número: '))
# # raiz = math.sqrt(num)
# # OR
# raiz = sqrt(num)
# print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# -------------------------------------------------------------------


# 015
# km = float(input('Digite KM percorridos: '))
# dal = float(input('Digite quantos dias o carro ficou alugado: '))
# qtdDia = dal * 60
# qtdKm = km * 0.15
# total = qtdDia + qtdKm

# print('O valor final a pagar é R${}'.format(total))

# -------------------------------------------------------------------

# 005
# n = int(input('Digite um número: '))
# print('O número que você digitou é {} e antecessor a ele é {} e o sucessor é {}'.format(
#     n, (n-1), (n+1)))

# -------------------------------------------------------------------

# 006
# n = int(input('Digite um número: '))
# print('O número que você digitou é {} e o dobro dele é {} e o triplo é {} e a raiz quadrada é {}'.format(
#     n, (n*2), (n*3), (n**2)))

# -------------------------------------------------------------------

# 007
# n1 = int(input('Digite sua 1° nota: '))
# n2 = int(input('Digite sua 2° nota: '))
# print('Sua média é {}'.format((n1+n2)/2))

# 008
# n = int(input('Digite uma quantidade em metros: '))
# print('Em metros você tem {} em centimetros você tem {} e em milemetros você tem {}'.format(
#     n, (n*100), (n*1000)))

# -------------------------------------------------------------------

# 009
# n = int(input('Digite um número: '))
# print('A tabuada de {} é '.format(n))
# for i in range(1, 11):
#     print('{} * {} = {}'.format(n, i, (n*i)))

# -------------------------------------------------------------------

# 010
# operadores aritméticos (+ | - | * | / | ** | // | %)
# ordem de precedência -> () | ** | * / // % | + -
# nome = input('Digite seu nome: ')
# print('É um prazer te conhecer {:>20}!'.format(nome))
# print('É um prazer te conhecer {:<20}!'.format(nome))
# print('É um prazer te conhecer {:^20}!'.format(nome))
# print('É um prazer te conhecer {:=^20}!'.format(nome))

# n1 = int(input('Digite o 1° valor: '))
# n2 = int(input('Digite o 2° valor: '))
# s = n1 + n2
# m = n1 * n2
# d = n1 / n2
# di = n1 // n2
# e = n1 ** n2
# print('A soma é {}, \n o produto é {} e a divisão é {:.3f}'.format(
#     s, m, d), end=' >>> ')
# print('Divisão intereira {}, e potência {}'.format(di, e))

# -------------------------------------------------------------------

# n = input('Digite algo: ')
# print(n.isalpha())  # Verifica se é letra e retorna um bool
# print(n.isnumeric())  # Verifica se é numero e retorna um bool
# print(type(n))

# -------------------------------------------------------------------

# números primitivos (int / float / bool / str)
# n1 = int(input('Digite o 1° valor: '))
# n2 = int(input('Digite o 2° valor: '))

# soma = n1 + n2
# print("A soma total entre {} e {} é {}".format(n1, n2, soma))

# -------------------------------------------------------------------

# nome = input('Digite seu nome: ')
# print('É um prazer te conhecer {}!'.format(nome))

# -------------------------------------------------------------------

# n1 = input('Insira o 1° número?')
# n2 = input('Insira o 2° número?')
# soma = n1+n2
# print('A soma é: ', soma)
