#7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome.

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

def concat_nomes(nomes,sobrenomes):
    for nome, sobrenome in zip(nomes, sobrenomes):
            nome_corrigido = nome.capitalize()
            sobrenome_corrigido = sobrenome.capitalize()
            print(f"Nome Completo: {nome_corrigido} {sobrenome_corrigido}")

concat_nomes(nomes,sobrenomes)

# # Nomes dos estudantes
# nomes = ["joão", "MaRia", "JOSÉ"]
# sobrenomes = ["SILVA", "souza", "Tavares"]

# # Função lambda que recebe duas listas e itera em cada uma concatenando seu nome e sobrenome
# # na forma desejada
# nome_completo = map(lambda nome, sobrenome: f'{nome.title()} {sobrenome.title()}', nomes, sobrenomes)

# # Leitura do objeto mapa(iterável)
# for n in nome_completo:
#   print(f'Nome completo: {n}')