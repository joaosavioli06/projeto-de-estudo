#Tudo que estiver entre aspas é uma string

minha_string = "qualquer texto"
print(type(minha_string))
print(minha_string)


print(f"contatenar {minha_string} em string")

print(minha_string.upper())
#deixar em maiúsculo

print(minha_string.lower())
#minúsculo

print(minha_string.capitalize())
#deixar a primeira letra do texto em maiúsculo

print(minha_string.isupper())
#verificar em true / false se esse texto está em maiúsculo

print(minha_string.islower())
#verificar em true / false se esse texto está em minúsculo

string_2 = " teste da strip/espaço "

print(string_2.strip())
#a função strip retira os espaços de um texto

print(string_2.replace("espaço", "meu"))
#esse função faz com que você troque uma palavra ou letra dentro da string poor outra

print(string_2.replace("t", "T"))
#troquei as letras "t" para "T"

print(string_2.replace("t", "T", 1))
#aqui eu dei o comando para ele trocar apenas a primeira letra "t" da string

print(len(string_2))
#a função len retorna quantas letras tem na sua string

print(string_2[2])
#utilizando um número dentro das colchetes, você busca a respectiva letra dentro desta string
#como nesse caso eu escolhi o número 2, então essa função busca qual é a letra número dentro da minha string
#neste caso, a letra será a letra "e", pois: t"e"ste da strip/espaço

print(string_2[0])
#nesse caso aqui, como a primeira letra da string é um espaço, ele não retorna nada

print(string_2[2:5])
#buscou de uma letra até outra letra, começou a segunda até a quinta letra

print(string_2[-2:-1])
#fazendo a busca na string de trás para frente, neste caso ele começa do -1, pois -0 não existe
#ele printa as letras "ç" e "o". -1 é o !o, pois -0 não existe então ele ignora o espaço.

print(string_2.index("e"))
#com o .index você faz a busca de quantas letras "x" existem dentro da sua string

print(string_2.index("teste"))
#buscando uma palavra pelo index, mas ele só vai printar o número 1, pois essa é a palavra inicial da string

print(string_2.index("str"))
#retorna o número 10, eu estou buscando um valor q está dentro de uma palavra

#é importante deixar claro que o index busca o número/índice inicial da palavra, letra ou parte de uma palavra 

"""print(string_2.index("z"))
#ele n vai achar nada com z na string, vai dar erro"""

x = "texto" in minha_string

print(x)

x = "texo" in minha_string

print(x)


#essa função acima mostra se a palavra "texto" está presente ou não dentro da minha string
#no caso, a palavra "texto" realmente existe dentro da minha_string, agora a palavra "texo" não existe

linha = """linha 1,
linha 2,
linha 3.
 """

print(linha)

#usando as """, você consegue escrever/quebrar várias linhas uma embaixo da outra. É como se fosse um /n do Python  

teste_aspas = "olha que legal, se eu quiser imprimir aspas dentro de aspas, é só fazer isso. Eu falei que queria \"entre aspas\" no texto"
print(tes)






