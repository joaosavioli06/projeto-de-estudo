num1 = 5  #int
num2 = 3.5 #float

print(type(num1))
print(type(num2))
# a função type verifica qual é tipo de uma certa variável

a = float(num1)
print(a)
print(type(a))
#agora eu fiz a conversão do tipo da variável. Ela era uma variável inteira,
#agora ela é uma variável de tipo float

b = int(num2)
print(b)
print(type(b))
#no Python, quando você converte uma variável de tipo float para inteira
#o número sempre será arredondado para baixo. Ele pode ser um 3.2, 3.8, 3.5 ou 3.9, o número
#o número sempre será arredondado para 3 neste caso

d = int("10")
print(d)
print(type(d))
#a variável era de tipo string, mas eu mudei para tipo inteiro

# e = int("8.3")
# print (e)
# print(type(e))
#Se você tentar rodar o código assim, uma string com casas decimais para um inteiro, vai dar pau
# Se você quiser que funcione, primeiro você transforma em float e depois para inteiro

e = int(float("8.3"))
print (e)
print(type(e))

#Operadores aritméticos

num3 = 2
num4 = 4

print (num3 + num4)
#adição
print (num3 - num4)
#subtração
print (num3 * num4)
#multiplicação
print (10 / 3)
#divisão
print (3 ** 3 )
#exponenciação - 3 * 3 * 3 = 27
print (10 % 3)
#módulo / resto da divisão ex: 10 % 3 = 3 * 3 = 9 ( 9 + 1 = 10) O módulo de 10 % 3 será 1
print (10 // 3)
# divisão sem casas decimais. O resultado dessa divisão normal, seria 3.3333333... Utilizando o //, o resultado vai ser 3 

print (3 + 5 * 7 + 3)
#faz a multiplicação primeiro de 5 * 7 e depois faz as contas de adição.
print ((3 + 5) * (7 + 3))
#nesse caso aqui, as contas já são isoladas utilizando os parênteses 

print (abs(-15)) 
#retorna o valor absoluto de algo, explicação: O valor absoluto de qualquer número se refere a sua magnitude e não ao sinal que pode ter, seja ele positivo ou negativo ... 
# Em termos matemáticos, o valor absoluto é uma operação que permite qualquer número tornar-se positivo.
print (pow(3,3))
#é basicamente a exponenciação só q de um jeito mais resumido. Você coloca o número principal e depois o segundo número vai ser o expoente. Nesse caso 3 * 3 * 3 = 27. Isso é o que eu entendi...

print (max(1,5, 19, 20, 89, -29, 12))
#ele printa o número mais alto dentre os números selecionados
print (min(1,5, 19, 20, 89, -29, 12))
#aqui ele faz o contrário, ele sempre printa o número mais baixo dentro os números selecionados
print(round(8.3))
#usando a função round, o número será arredondado para o número inteiro mais próximo. Aqui, o terminal vai printar 8, pois é o mais próximo de 8.3
print(round(8.8))
#aqui ele irá para 9, pois é mais próximo de 9 doq de 8

import math
#importando uma biblioteca no Python, normalmente isso é feito no início do código, aqui só é feito para mostrar essas funções de exemplo. Vou ver isso mais para frente...

print(math.floor(8.9999))
#a função floor arredonda os números para baixo, funciona da mesma forma que o ceiol, só que para baixo. Como vemos no exemplo, ele pode estar extremamente perto de 9, mas ele será arredondado para 8
print(math.ceil(8.00001))
#arredonda o número para cima. Se o número for 8.3, será arredondado para 9, pode até ser 8.000000000000000000000000000001, mas ele irá ser arredondado para 9. A função ceil arredonda para cima

print(math.sqrt(9))
print(math.sqrt(64))
#printa a raíz quadrada de certo número, como mostra aí no exemplo de 64 (8) e 9 (3). O resultado sempre sai em float  