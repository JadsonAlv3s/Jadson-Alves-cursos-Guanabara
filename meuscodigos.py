#===========================INICIO=================================

# 4. Conversão de Lista para Tupla: Escreva um programa que dada uma lista de números,
# converta essa lista em uma tupla e, em seguida, utilize slices para criar uma nova tupla
# que contenha apenas os três primeiros elementos da tupla original. Imprima o
# resultado da lista original e as duas tuplas criadas. Exemplo:


# lista= [1,2,3,4,5]
# tupla=(lista)
# slices=(1,2,3)

# for i in tupla:
#     print(f"Tupla: {tupla} e slice da tupla: {slices}")
#===========================FIM=================================  

#===========================INICIO=================================

                        #QUESTAO 05
# Troca de posições em tuplas: Escreva um programa que, dada uma tupla e dois valores
# inteiros correspondentes às posições nessa tupla, troque os elementos conforme as
# posições fornecidas. Lembre-se de que tuplas são imutáveis, portanto, você precisará
# converter a tupla para uma lista, fazer a troca e depois converter de volta para uma
# tupla. Imprima o resultado da tupla inicial e com as posições permutadas. Exemplos:

# tupla1=((1,2,3,4,5),(7,2,4,8,3))
# lista=[tupla1]
# posicao1=(lista[:3])
# posicao2=(lista[:4])

# for x,y in lista:
#     print(f"tupla A{posicao1} tupla B{posicao2}")

#===========================FIM=================================  

#===========================INICIO=================================

# Escreva um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, do zero ate vinte.
# seu programa devera ler um numero pelo teclado (entre 0 a 20) e mostra-lo por extenso.

"""tupla = ("zero","um","dois","tres","quatro","cinco")

while True:
    usuario=int(input("Digite um numero de 0 a 5: "))
    if 0 <= usuario <=5:
        break
    print("tente novamente. ", end="")
    
print(f"Voce digitou o numero {tupla[usuario]}")"""

#===========================FIM=================================  


#===========================INICIO=================================

'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''
"""preco = float(input("Qual o valor da casa? \n"))
sal = float(input("Qual é o seu salário? \n"))
tempo = int(input("Em quantos anos você vai pagar? \n"))

mensalidade = (preco / (tempo * 12))
print("Valor da casa: {:.2f}".format(preco))
print("Prestação: {:.2f}".format(mensalidade))

if mensalidade >= (sal * 30 / 100):
    # if sal < (mensalidade * (30 / 100)):
    print("Empréstimo negado.")
else:
    print('''Empréstimo concedido.
    Mensalidade durante {} anos: R${:.2f}.'''.format(tempo, mensalidade))"""
    
#===========================FIM=================================    


#===========================INICIO=================================

''' Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
2 para hexadecimal
'''
"""num = int(input("Digite um número a ser convertido: \n"))
base = int(input('''Escolha a base da conversão:
Para binário digite: 1
Para octal digite: 2
Para hexadecimal digite: 3

Sua escolha: \n'''))

if base == 1:
    print("Você escolheu binário.")
    print("{} convertido para binário é: {}.".format(num, bin(num)[2:]))
elif base == 2:
    print("Você escolheu octal.")
    print("{} convertido para octal é: {}.".format(num, oct(num)[2:]))
elif base == 3:
    print("Você escolheu hexadecimal.")
    print("{} convertido para hexadecimal é: {}.".format(num, hex(num)[2:]))
else:
    print("Por favor, escolha apenas uma das 3 opções.")"""
    
#===========================FIM=================================    


#===========================INICIO=================================

'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior; os dois são iguais
'''
"""print("Comparados de números \n")
num1 = int(input("Digite um número inteiro: \n"))
num2 = int(input("Digite outro número inteiro: \n"))

if num1 > num2:
    print("O primeiro valor é maior, pois {} > {}.".format(num1, num2))
elif num2 > num1:
    print("O segundo valor é maior, pois {} > {}.".format(num2, num1))
else:
    print("Não existe valor maior; os números digitados são iguais.")"""
    
#===========================FIM=================================  


#===========================INICIO=================================
'''
Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
'''
"""from datetime import datetime

nasc = int(input("Em qual ano você nasceu? \n"))
ano_atual = datetime.now().year
# print("Ano atual: {}".format(ano_atual))
idade = (ano_atual - nasc)
if idade < 18:
    print("Você tem {} anos em {} e vai se alistar daqui a {} anos, em {}.".format(
        idade, ano_atual, (18 - idade), (nasc + 18)))
elif idade > 18:
    print("Você tem {} anos e já passou seu período de alistamento.".format(idade))
    print("Se não se alistou, deveria ter se alistado em {}, há {} anos atrás.".format(
        (nasc + 18), idade - 18))
else:
    print("Você tem {} anos. Está na hora de se alistar.".format(idade))"""

#===========================FIM=================================  


#===========================INICIO=================================

'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- média abaixo de 5.0: reprovado
- média entre 5.0 e 6,9: recuperação
- média 7.0 ou superior: aprovado
'''
"""n1 = float(input("Digite a primeira nota: \n"))
n2 = float(input("Digite a segunda nota: \n"))
m = ((n1 + n2) / 2)

if m < 5.0:
    print("Média {}. Você foi REPROVADO.".format(m))
elif m > 6.9:
    print("Média {}. Você foi APROVADO".format(m))
else:
    print("Média {}. RECUPERAÇÃO.".format(m))"""
    
#===========================FIM=================================  

#===========================INICIO=================================

#from datetime import date
'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 20 anos: sênior
acima de 20: master
'''
"""atual = date.today().year
nasc = int(input("Ano de nascimento do(a) nadador(a): \n"))
idade = atual - nasc
print("O atleta tem {} anos em {}.".format(idade, atual))


if idade <= 9:
    print("Classificação: Mirim.".format(idade))
elif idade <= 14:
    print("Classificação: Infantil.".format(idade))
elif idade <= 19:
    print("Classificação: Júnior.".format(idade))
elif idade <= 25:
    print("Classificação: Sênior.".format(idade))
else:
    print("Classificação: Master.".format(idade))"""
    
#===========================FIM=================================  

#===========================INICIO=================================
'''
Refaça o DESAFIO 35, dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:

- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes
'''
"""a = float(input("Primeiro segmento de reta: \n"))
b = float(input("Segundo segmento de reta: \n"))
c = float(input("Terceiro segmento de reta: \n"))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("O triângulo que existe é um ", end="")
    if a == b == c:
        print("triângulo EQUILÁTERO.")
    elif (a == b) or (a == c) or (b == c):
        print("triângulo ISÓSCELES.")
    else:
        print("triângulo ESCALENO.")
else:
    print("O triângulo inexiste.")"""
    
#===========================FIM=================================  

#===========================INICIO=================================
'''

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, e acordo com a tabela abaixo:

- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida
'''
"""m = float(input("Digite seu peso (em kg): \n"))
h = float(input("Digite sua altura (em m): \n"))

imc = (m / (h**2))

if imc < 18.5:
    print("Seu IMC é de: {:.1f}. Você está abaixo do peso.".format(imc))
elif imc < 25:
    print("Seu IMC é de: {:.1f}. Você está no peso ideal.".format(imc))
elif imc < 30:
    print("Seu IMC é de: {:.1f}. Você está com sobrepeso.".format(imc))
elif imc < 40:
    print("Seu IMC é de : {:.1f}. Você está com obesidade.".format(imc))
else:
    print("Seu IMC é de {:.1f}. Você está com obesidade mórbida.".format(imc))"""

#===========================FIM=================================  

#===========================INICIO=================================
'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros
'''
"""valor = float(input("Qual o preço do produto? \n"))
print("Selecione uma forma de pagamento")
print('''
Digite 1: Para pagar à vista no dinheiro.
Digite 2: Para pagar à vista no cartão.
Digite 3: Em 2x no cartão.
Digite 4: Em 3x no cartão ou mais \n''')
forma = int(input("Selecione a forma de pagamento: \n"))

if forma == 1:  # 10% de desconto
    print("Você selecionou à vista no dinheiro.")
    desconto = (valor * (10/100))
    print("Valor à vista no dinheiro: R${:.2f}.".format(
        valor - desconto)
    )
elif forma == 2:  # 5% de desconto
    print("Você selecionou à vista no cartão.")
    desconto = (valor * (5 / 100))
    print("Valor à vista no cartão: {:.2f}.".format(
        valor - desconto)
    )
elif forma == 3:  # Em até 2x no cartão: preço normal
    print("Você selecionou em 2x no cartão.")
    print("Pagamento em 2x de R${:.2f}.".format((valor / 2))
          )

elif forma == 4:  # Em até 3x ou mais: 20% de juros
    print("Você selecionou em 3x ou mais no cartão.")
    desconto = (valor * (20 / 100))
    parcelas = int(input("Em quantas vezes você deseja parcelar? \n"))
    if parcelas < 3:
        print("A quantidade mínima de parcelas é de 3x no cartão.")
    else:
        print("Pagamento, com juros de 20%, em {}x de R$ {:.2f}.".format(
            parcelas, (valor + (desconto)) / parcelas))
else:
    print("Por favor, selecione uma alternativa válida. Tente novamente.")"""
    
#===========================FIM=================================

#===========================INICIO=================================


"""from random import choice
from time import sleep

"""
#Crie um programa que faça o computador jogar Jokenpô com você.
"""
choices_list = ["pedra", "papel", "tesoura"]
print("""
# COMPUTADOR: Vamos jogar Pedra, Papel, Tesoura!
# As regras são as seguintes:
# - Papel vence Pedra e perde para Tesoura
# - Pedra vence Tesoura e perde para Papel
# - Tesoura vence Papel e perde para Pedra
# """)

# player_prompt = str(input("Você escolhe pedra, papel ou tesoura? \n")).lower()

# print("JO")
# sleep(0.50)
# print("KEN")
# sleep(0.5)
# print("PÔ!!!")

# computer_choice = choice(choices_list)


# def judge(computer, player):
#     print(
#         f"""
#    """ Jogador: {player_prompt}
#     Computador: {computer}"""
#     """
#     )

#     ### Exceptions:
#     if player != "pedra" and player != "papel" and player != "tesoura":
#         return print(
#             f"{player} não é uma opção válida. Escolha pedra, papel ou tesoura!"
#         )

#     if player != "pedra" and player != "papel" and player != "tesoura":
#         return print(
#             f"{player} não é uma opção válida. Escolha pedra, papel ou tesoura!"
#         )

#     if computer == player:
#         return print("Empate. Vamos jogar novamente!")

#     ### Valid plays
#     if player_prompt == "pedra" and computer == "tesoura":  # Pedra x Tesoura: Pedra
#         return print("Pedra vence tesoura. Jogador ganhou.")

#     if player_prompt == "tesoura" and computer == "pedra":  # Tesoura x Pedra: Pedra
#         return print("Pedra vence tesoura. Computador ganhou.")

#     if player_prompt == "papel" and computer == "pedra":  # Papel x Pedra: Papel
#         return print("Papel vence pedra. Jogador ganhou.")

#     if player_prompt == "pedra" and computer == "papel":  # Pedra x Papel: Papel
#         return print("Papel vence pedra. Computador ganhou.")

#     if player_prompt == "papel" and computer == "tesoura":  # Papel x Tesoura: Tesoura
#         return print("Tesoura vence papel. Computador ganhou.")

#     if player_prompt == "tesoura" and computer == "papel":  # Tesoura x Papel: Tesoura
#         return print("Tesoura vence papel. Jogador  ganhou.")


# judge(choice(choices_list), player_prompt)"""


#===========================FIM=================================

#===========================INICIO=================================

# nome = str(input("Digite um nome: \n")).strip().lower().capitalize()

# if nome == "Guilherme" or nome == "Kendrick":
#     print("{} é um nome bonito.".format(nome))
# elif nome == "Mateus" or nome == "Marcos":
#     print("{} é um nome bem bíblico.".format(nome))
# elif nome == "Galadriel" or nome == "Glorfindel":
#     print("{} é um nome bem élfico.".format(nome))
# else:
#     print("Seu nome é bem normal.")
# print("Tenha um excelente dia, {}.".format(nome))

#===========================FIM=================================

#===========================INICIO=================================