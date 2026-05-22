print("-CALCULADORA BÁSICA-")
print()


try:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
except:
    print()
    print("ERRO: VALOR INVÁLIDO!")
    exit()

operacao = str(input("Entre a operação que você quer realizar: "))

print()

if operacao in ["+", "soma", "adição", "Soma", "Adição", "mais", "Mais"]:
    resultado = valor1 + valor2

elif operacao in ["-", "menos", "subtração", "Menos", "Subtração"]:
    resultado = valor1 - valor2

elif operacao in ["*", "vezes", "multiplicação", "Vezes", "Multiplicação"]:
    resultado = valor1 * valor2

elif operacao in ["divisão", "dividir", "Divisão", "Divisão"]:

    tipo_divisao = input("Tipo de divisão (INTEIRA ou REAL/FLOAT): ")

    if tipo_divisao in ["//", "inteira", "Inteira", "INTEIRA"]:
        resultado = valor1 // valor2
    
    elif tipo_divisao in ["/", "float", "real", "Float", "Real", "FLOAT", "REAL"]:
        resultado = valor1 / valor2

    else:
        print(f"RESULTADO: ERRO!")

elif operacao == "/":
    resultado = valor1 / valor2

elif operacao == "//":
    resultado = valor1 // valor2

else:
    print("ERRO: OPERADOR INVÁLIDO!")
    exit()

print(f"RESULTADO: {resultado}")
