#Aula 01 - PRINT e INPUT
print("Hello World")

#Tipos de variáveis
num = int(1)
decimal = float(1)
palavra = str(1)
boleano = bool(1)
boleano1 = bool(0)

print(num)
print(decimal)
print(palavra)
print(boleano)
print(boleano1)
print(type(num))
print(type(decimal))
print(type(palavra))
print(type(boleano))
print(type(boleano1))

#Testando input e print
num1 = float(input("Digite um número: "))
num2 = int(2)
print(num1)
print(num2)
print(type(num1))
print(type(num2))

#Concatenar strings
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
print("Prazer", nome, "você tem", idade, "anos de idade.")