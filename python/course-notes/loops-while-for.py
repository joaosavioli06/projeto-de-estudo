"""
i = 1 

while i < 10:
    print(i)
    i +=1 #i = i + 1

print("terminou")
print(i)
"""
criancas = ["Manu", "Vini", "Selina"]

"""

for item in criancas:
    print(item)

"""

# canal = "Refatorando"

# for letra in canal:
#     print(letra)

# for index in range(6, 20, 2):
#     #como podemos ver dentro do (6, 20, 2), o 6 simboliza onde o index começa, o 20 simboliza até onde ele deve parar, que no caso vai parar no 19, e o 2 simbolzia de quantos em quantos números ele vai contar (6, 8, 10, 12 , 14, 16, 18)
#     print (index)

# for index in range(len(criancas)):
#     print(criancas[index], index)

# for index in range(5):
#     if index == 0:
#         print("primeira linha")
#     else:
#         print(f"outras linhas {index}")

matrix_numeros = [
   [1,2,3], 
   [4,5,6], 
   [7,8,9], 
   [0],
]

for linha in matrix_numeros:
    #print(linha)
    print("----")
    for coluna in linha:
        print(coluna)