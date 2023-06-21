nome = input ("Digite seu nome: ")
#sem segredo, o input pergunta sobre alguns dados que a pessoa digitou no terminal
idade = int(input(f"Qual a sua idade {nome}?"))
#aqui eu transformei esse input em int (conversão). Ele só vai aceitar números inteiros
nascimento = 2023 - idade


print(f"Seu nome é {nome}, sua idade é: {idade}, e você nasceu em {nascimento}")

#Para fazer comentários dentro do Python, você pode utilizar o "#" para fazer o comentário em uma linha só
#Ou utilizar comentários em várias linhas, utilizando três aspas """. Não é muito recomendado pelo Python

#Calculadora Básica:

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
resultado = num1 + num2

print(f"O resultado é {resultado}")
