# Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.


lista =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



num_quadrado = list(map(lambda x: x * x, lista ))
print(num_quadrado)

