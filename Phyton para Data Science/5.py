# 5. Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

# Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:

# "Nota da manobra: [media]"


notas =[]

def receber_notas(notas):   #não precisava da função
    for i in range(1,6):
        valor_notas = float(input(f"Insira a nota {i}: "))
        notas.append(valor_notas)
 
def preparar_media(notas):
    notas.remove(min(notas))
    notas.remove(max(notas))
    print(notas)
    
    
receber_notas(notas)   
preparar_media(notas)   


media = sum(notas)/ len(notas) #podia colcoar um return na função para ter a media

print(f"Nota da manobra: {media}")














