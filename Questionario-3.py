#Questão 01 - Netflix Salários
print("Informe os valores dos salário (todos de uma vez, separados por espaço): ")
salarios = input().split()

#salarios = [int(salario) for salario in salarios] #Alternativa para converter item por item via Loop
salarios = list(map(int, salarios)) #Alternativa sugerida

print(f"O menor salário é de {min(salarios)}, e o maior {max(salarios)}")

#Extra - Ordenando a lista usando algoritmo Bubble Sort
i = 0
while i < len(salarios):
    j = 0
    while j < len(salarios):
        if salarios[i] < salarios[j]:
            aux = salarios[j]
            salarios[j] = salarios[i]
            salarios[i] = aux
        j += 1
    i += 1

print(f"Ordenado by Bubble algorithm: {salarios}")

#Extra - Ordenando a lista usando função sorted
salarios = sorted(salarios)
print(f"Ordenado by sorted() function: {salarios}")

'''
OBS:
salario = "100 200 3" #Recebendo a entrada em forma de string
salario = salario.split() #Convertendo para um vetor/lista

y = [int(a) for a in salario] #convete item por item da lista em int
print(y)

x = list(map(int, salario)) #converte ao mesmo tempo todos itens da lista
print(x)
'''

#Questão 02 - Lente de contato calculadora
print(f"""
|CALCULADORA SUPER AVANÇADA POR LENTE DE CONTATO|
Escolha uma opção a seguir para operar 2 números:
1 - Somar       (Digite (1) ou pisque 1 vez)
2 - Subtrair    (Digite (2) ou pisque 2 vezes)
3 - Multiplicar (Digite (3) ou pisque 3 vezes)
4 - Divir       (Digite (4) ou pisque 4 vezes)

                                by Brenno e João
""")

piscou = int(input("Digite a opção desejada: "))

if piscou >= 1 and piscou <= 4:

    num1 = float(input("Informe o primeiro número: "))
    num2 = float(input("Informe o segundo número: "))

    if piscou == 1:
        res = num1 + num2
        print(f"A soma é: {res}")
    elif piscou == 2:
        res = num1 - num2
        print(f"A subtração é: {res}")
    elif piscou == 3:
        res = num1 * num2
        print(f"A multiplicação é: {res}")
    else:
        if  num2 != 0:
            res = num1/num2
            print(f"A divisão é: {res}")
        else:
            print(f"O segundo número precisa ser diferente '0'.")

else:
    print("Você digitou uma opção inválida")