print("Bem vindo a calculadora em Python!")

print("\nPara começarmos, digite dois números de sua preferência")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Obrigado por fornecer os números! No entanto, agora você deve escolher quais das operações você deseja. Você pode escolher entre essas:")
print("\n(+) = Adição")
print("\n(-) = Subtração")
print("\n(*) = Multiplicação")
print("\n(/) = Divisão")
print("\n(**) = Exponenciação")
print("\n(%) = Módulo")
print("\n(//) = Divisão sem casas decimais")

operacao = input("\nQual operação você irá utilizar? ")

if operacao == "+":
     print("O resultado de sua operação é: " + str(float(num1 + num2)))
elif operacao == "-":
     print("O resultado de sua operação é: " + str(float(num1 - num2)))
elif operacao == "*":
     print("O resultado de sua operação é: " + str(float(num1 * num2)))
elif operacao == "/":
     print("O resultado de sua operação é: " + str(float(num1 / num2)))
elif operacao == "**":
     print("O resultado de sua operação é: " + str(float(num1 ** num2)))
elif operacao == "%":
     print("O resultado de sua operação é: " + str(float(num1 % num2)))
elif operacao == "//":
     print("O resultado de sua operação é: " + str(float(num1 // num2)))