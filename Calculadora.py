valor1 = float(input("Insira o valor 1: "))
valor2 = float(input("Insira o valor 2: "))
operation = input("Informe a operação desejada: (+/-/*///):")

if operation.upper() == "+":
    print(valor1 + valor2)
elif operation.upper() == "-":
    print(valor1 - valor2)
elif operation.upper() == "*":
    print(valor1 * valor2)
elif operation.upper() == "/":
    print(valor1 / valor2)
else:
    print("Insira valores e/ou operação corretos.")
