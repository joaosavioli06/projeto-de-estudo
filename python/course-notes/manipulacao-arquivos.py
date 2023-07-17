# open("caminho", "modo")

# Mode
# r - Leitura
# a - Append / Incrementar
# w - Write / Escrita
# x - Criar arquivos
# r+ - Leitura + Escrita

arquivo = open("python/course-notes/test3.txt","x")
# aqui você coloca o caminho do arquiivo que você quer abrir
# sempre mude o modo do aquivo pela letra depois do caminho

print(arquivo.readable())
# retorna um verdadeiro ou falso que mostra se o arquivo pode ser lido

print(arquivo.read())
# ele lê o arquivo e printa toudo o que tem no arquivo

print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
# aqui ele lê linha por linha, então você precisa fazer o mesmo print várias vezes para retronar o que tem dentro do arquivo. Ele sempre lê a primeira linha do arquivo

lista = arquivo.readlines()
print(lista)

print(lista[3])

# aqui eu criei uma lista com oq tinha dentro do arquivo
# depois usei um índice para ele printar o texto de índice 3
# tudo utilizando o modo "r"

arquivo.close()
# aqui você fecha o arquivo com esse comando, é sempre importante antes de escrever algum código, sempre fechar ele depois de terminar o que vc queria fazer

arquivo.write("Python\n")
#utilizando o "a" 
#eu escrevo algo novo dentro deste arquivo, aí você escolhe se for usar o \n antes ou depois do que vc quiser adicionar
# se vc utilizar o "w" nesse caso, ele vai excluir tudo o que tem dentro do arquivo, e adicionar o que você digitou
# a diferença do append e write, é que o append você adiciona coisas no arquivo que já existe, já o w limpa tudo e começa algo novo em um arquivo que já existe

# utilizando o "w", você pode criar um arquivo novo mudando o nome do caminho do arquivo( colocando test2 por ex)
# o "x" funciona da mesma forma para criar um arquivo

import os 
# importei uma biblioteca no Python

os.remove("python/course-notes/test2.txt")
# remove um arquivo colocando o caminho dele

if os.path.exists("python/course-notes/test.txt"):
    os.remove("python/course-notes/test.txt")
else:
    print("Arquivo não existe")
# fazendo uma estrutura condicional para validar se o arquivo existe com o if e else
 
os.rmdir("python/course-notes/novapasta")
# remove uma pasta colocando o caminho dele