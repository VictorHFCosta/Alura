#  Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:

# maior nota
# menor nota
# média
# situação (Aprovado(a) ou Reprovado(a))


def desempenho():
    notas = []
    for i in range(1,5):
        valor_notas = float(input(f"Insira a nota {i}:"))
        notas.append(valor_notas)
    
    maior = max(notas)
    menor = min(notas)
    media = sum(notas)/len(notas)
    
    if media > 6 :
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    print(f"O(a) estudante obteve uma média de {media}, com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos e foi {situacao}")
    
desempenho()

# # declarando a lista de notas
# notas = []
# # laço for para pedir as 4 notas e armazená-las na lista notas
# for i in range(1,5):
#   nota = float(input(f"Digite a {i}ª nota: "))
#   notas.append(nota)

# def cadastro(lista):
#   maior = max(lista)
#   menor = min(lista)
#   media = sum(lista) / len(lista)
#   if media >= 6:
#     situacao = "Aprovado(a)"
#   else:
#     situacao = "Reprovado(a)"
  
#   return (media, maior, menor, situacao)

# media, maior, menor, situacao = cadastro(notas)

# print(f"O(a) estudante obteve uma media de {media}, com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos e foi {situacao}")