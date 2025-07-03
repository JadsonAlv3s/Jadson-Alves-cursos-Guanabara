# 4. Conversão de Lista para Tupla: Escreva um programa que dada uma lista de números,
# converta essa lista em uma tupla e, em seguida, utilize slices para criar uma nova tupla
# que contenha apenas os três primeiros elementos da tupla original. Imprima o
# resultado da lista original e as duas tuplas criadas. Exemplo:


# lista= [1,2,3,4,5]
# tupla=(lista)
# slices=(1,2,3)

# for i in tupla:
#     print(f"Tupla: {tupla} e slice da tupla: {slices}")

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


# Escreva um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, do zero ate vinte.
# seu programa devera ler um numero pelo teclado (entre 0 a 20) e mostra-lo por extenso.

"""tupla = ("zero","um","dois","tres","quatro","cinco")

while True:
    usuario=int(input("Digite um numero de 0 a 5: "))
    if 0 <= usuario <=5:
        break
    print("tente novamente. ", end="")
    
print(f"Voce digitou o numero {tupla[usuario]}")"""