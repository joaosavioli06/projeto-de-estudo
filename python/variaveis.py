nome = "João Gabriel Savioli" 
#string = tudo que seja texto
idade = 17 
#int ou inteiro = todo número que seja inteiro, seja negativo ou positivo
#nesse caso eu nem preciso utilizar às "" (10, -10, 0 etc)
linguagem = "Python"
#outro exemplo de string
altura = 1.74
#float = números quebrados, números com casas decimais (-1.81, 0.38, 27.5 etc)
homem = True 
#booleano = basicamente o falso e verdadeiro dentro do contexto de programação
#mais para frente, eu provavelmente vou ver a função booleana com outras coisas como: &, ||, !, and, or etc

print (f"Meu nome é {nome}")
""" invés de utilizar o f e a variável entre às chaves, eu poderia simplesmente 
fazer desta maneira: " + nome + ". Não é a melhor forma de chamar uma variável.
"""

print (f"Eu tenho o interesse de aprender {linguagem}")
print (f"Tenho {idade} anos")
print (f"{linguagem} me parece ser uma ótima linguagem...")

idade = "18"

print(f"\nDaqui menos de um ano, eu terei {idade} anos")

