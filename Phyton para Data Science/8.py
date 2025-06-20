#  Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo. Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.

# Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.

# Observação: se a quantidade de gols marcados numa partida for maior que a de sofridos, o time venceu. Caso seja igual, o time empatou e se for menor, o time perdeu. Para calcular o aproveitamento devemos fazer a razão entre a pontuação do time pela pontuação máxima que ele poderia receber.

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

def calcula_pontos(lista1,lista2):
    pontos = 0
    vitoria = 0
    derrota = 0
    empates = 0
    for gm , gs in zip(lista1,lista2):
        if gm > gs :
            pontos += 3
            vitoria += 1
        elif gm == gs:
            pontos += 1
            empates += 1 
        else:
            derrota += 1
    total_possivel = len(lista1) * 3
    aproveitamento = (pontos / total_possivel) * 100    
    print(f"A pontuação do time foi de {pontos} e seu aproveitamento foi de {aproveitamento:.2f}%.\n {vitoria} vitorias \n {derrota} derrotas \n {empates} emaptes")
    return pontos,aproveitamento,vitoria,empates,derrota
    
    

calcula_pontos(gols_marcados,gols_sofridos)
