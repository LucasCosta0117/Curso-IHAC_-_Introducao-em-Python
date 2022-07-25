#Questão 01 - Tiktok
print("Informe o nome do perfil: ")
perfil = str(input())

totalCurtidas = int(0)
i = 0
while i < 5:
    print(f"""Informe a qtd de curtidas do {i +1}º vídeo.""")
    totalCurtidas += int(input())
    i += 1

media = int( totalCurtidas/i )

print(f"""
O perfil {perfil} teve {totalCurtidas} curtidas com média de {media} curtidas por vídeo
""")

#Questão 02 - Thanos
print("Informe o tempo da chegada de Thanos em dias: ")
totalDias = int(input())

anos = int( totalDias//360 )
meses = int( (totalDias%360)//30 ) 
dias = int( (totalDias%360)%30 )

print(f"""
Thanos chega em: {anos} ano(s) {meses} mês(es) e {dias} dias(s)
""")

#Questão Extra - Notas
print("Insira as 4 notas (Todas de uma única vez, separadas por espaço): ")
nota1, nota2, nota3, nota4 = input().split()

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

media = (nota1 + nota2 + nota3 + nota4)/4
media = float(media)

if media%0.5 == 0 : #Para conseguir chegar na saída exata do exercício haha
    print("Média é igual: {:.1f}".format(media))
else :
    print("Média é igual: {:.2f}".format(media))