#2. Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

def peso(lista: list):
    peso = [tupla[2] for tupla in lista]
    print(peso)

peso(lista_de_tuplas)





# lista = []
# for tupla in lista_de_tuplas:
#     lista.append(tupla[2])
# print(lista)