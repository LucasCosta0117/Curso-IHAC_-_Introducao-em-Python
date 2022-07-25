#Aula 02 - Operadores e Exemplos práticos

'''
    Soma: +
    Subtração: -
    Multiplicação: *
    Divisão: /
    Divisão com retorno inteiro: //
    Resto da divisão: %
'''

#Teste de comparação, "==" sempre estritamente igual
n1 = 5
n2 = '5'

if(n1 == n2) :
    print("True")
else :
    print("False") #Resposta é false


#Concatção de string (Duas opções com uso de formatação)
nome = str("Lucas")
plano = str("Gold")
fatura = float(1270.8678)

#Opção 01
print("Ola {}, \nsua fatura do plano {}, é de {:.2f}".format(nome, plano, fatura))

#Opção 02
print(f""" 
Ola {nome},
sua fatura do plano {plano}, é de {fatura:.2f}."
""")