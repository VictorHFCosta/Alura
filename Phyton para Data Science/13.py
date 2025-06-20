# A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.


lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']

lista_tupla = []

for i in range(len(lista)):
    lista_tupla.append((i,lista[i]))
print(lista_tupla)











