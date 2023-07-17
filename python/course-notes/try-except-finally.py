try:
    numero = int(input("Digite um número: "))
    print(numero)
#       10/0

except ZeroDivisionError:
    print("Divisão por 0 não é possível")
except ValueError:
    print("Digite um valor válido.")
except:
    print("Erro inesperado")
finally:
    print("Sempre executa")

# Sobre cada coisa:
# o try é basicamente uma tentativa de algo, ali eu coloquei um input, e com esse input, começam as condições com o except
# A primeira condição é se tivesse uma divisão ali, como a nota está mostrando, simplesmente uma divisão jogada lá. Como é impossível dividir por 0, então ele mostraria o erro do print no terminal
# A segunda condição é quando se digita uma string ao invés de um valor
# A terceira condição é se acontecer algum erro, tipo o nome da variável numero for x, aí vai ter um erro no nome e n vai dar para executar
# O finally, é uma mensagem que sempre executa, mesmo se o código der certo ou errado

