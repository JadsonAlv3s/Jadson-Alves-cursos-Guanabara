"""n1 = int(input("digite um numero: "))
n2 = int(input("digite outro numero: "))

soma = n1 + n2

print("soma entre {} e {} vale {}".format(n1, n2, soma))"""
#####FIm

"""a = (input("digite algo: "))
print("O tipo primitivo desse valor é: ", type(a) )
print("Só tem espaços?: ", a.isspace())
print("É um numero?: ", a.isnumeric())
print("É alfabeto?: ", a.isalpha())
print("É alfanumerico?: ", a.isalnum())
print("Esta em maiúsculas?: ", a.isupper())
print("Está capitaizado?: ", a.istitle())"""
######################################################
#Operadores Aritiméticos

"""nome=input("digite seu nome: ")
print("Prazer em te conhecer:{:=^15}! ".format(nome))"""

"""n1= int(input("Digite um valor: "))
n2=int(input("Digite outro valor: "))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2

print("A soma vale {}, o produto é {} e a divisão é {:.3}".format(s, m, d), end=" ")
print("divisão inteira é {} e pontencia {}".format(di, e))"""

##Exercicio 05
#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.

"""numero=int(input("digite um numero: "))
sucessor=(numero+1)
antecessor=(numero-1)

print("O seu numero digitado foi {} e o seu Sucessor é {} e o antecessor {} ".format(numero, sucessor, antecessor))

print ("Fim do Programa")"""

##Exercicio 06
#Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

"""n=int(input("Digite um numero"))

d=(n*2)
t=(n*3)
r=(n**2)

print("o dobro é {}, o triplo é {} e a raiz quadrada {}".format(d, t, r))
print("Fim de programa!!")"""

##Exercicio 07

#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media.

"""nota1=int(input("Digite a primeira nota: "))
nota2=int(input("Digite a segunda nota: "))
s=(nota1+nota2) / 2
print("Sua primeira nota foi {}, sua segunda nota foi {} e sua média é {}".format(nota1, nota2, s))
print("Fim de programa!!")"""

##Exercicio 08

#Escreve um programa que leia um valor em metros e o exiba convertido centimetros e milimetros.

"""m=int(input("Digite o valor em METROS: "))
c=(m*100)
ml=(m*1000)

print("O valor em metro é {} convertido para centimetros é {} e centimetros {}".format(m, c, ml))
print("Fim do programa")"""

##Exercicio 09

#Faça um programa que leia um numero inteiro qualquer e mostre na tela sua tabuada.

"""n=int(input("Digite um numero: "))
a=(n*1)
b=(n*2)
c=(n*3)
d=(n*4)
e=(n*5)
f=(n*6)
g=(n*7)
h=(n*8)
i=(n*9)

print("A tabuada do numero {} é {}".format(n,a))
print("A tabuada do numero {} é {}".format(n, b))
print("A tabuada do numero {} é {}".format(n,c))
print("A tabuada do numero {} é {}".format(n, d))
print("A tabuada do numero {} é {}".format(n,e))
print("A tabuada do numero {} é {}".format(n, f))
print("A tabuada do numero {} é {}".format(n,g))
print("A tabuada do numero {} é {}".format(n, h))
print("A tabuada do numero {} é {}".format(n, i))
print("FIm do programa!!")"""





##Exercicio 10

#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. Conside US$1,00=3.27

"""carteira=int(input("Valor na carteira: "))
dolar= 3.27
conversao= (carteira/dolar)

print("Tenho na carteira {} reais e posso comprar {} Dolares".format(carteira, conversao))
print("Fim do programa!!")"""


##Exercicio 11

#Faça um programa que leia a altura e a largura de uma parede em metros, calcule sua area e a quantidade de tinta 
# necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m2.

"""altura=int(input("Digite a altura: "))
largura=int(input("Digite a largura "))

area= (altura*largura)
lt_tinta=(area/2)

print("A altura é {} e a largura {} sua area total {} e a quantidade de tinta a usar é {} litros".format(altura, largura, area, lt_tinta))

print("Fim do programa")"""




##Exercicio 12

#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

"""preco=float(input("Digite o valor do produto: "))
n=(preco*0.95)

print("o valor do produto foi {} e o valor com desconto é {}".format(preco, n))
print("Fim do programa!!")"""

##Exercicio 13

#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salário com 15% de aumento.

"""p=int(input("Digite o salario: "))
a=(p*115)

print("Seu salario atual é {}, porém teve uma melhoria para {} ".format(p, a))
print("Fim do programa!!")"""

