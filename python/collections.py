familia = ["João Gabriel", "Edilaine", "Gerson"]
#               0               1          2
#               -3              -2         -1
#para fazer uma lista em uma variável, coloque ela entre chaves []

print(familia[0])
#utilizando o índice para pegar a primeira coisa que tem na variável

print(familia[-1])
#pegando de trás para frente

print(familia[1:])
#ele pega os valores que estão do 1 para frente utilizando o :

print(familia[0:2])
#aqui você coloca o valor inicial e o valor final para ele puxar os valores
#No entanto, ele só vai printar João Gabriel e Edilaine, pois ele exclui o valor final

familia[2] = "Olympio" 
#trocando o nome do índice 2 (Gerson para Olympio)
print (familia)

familia.extend(["William", "Melissa"])
#Adiiconando mais dois índices para a variável. Quando se usa o extend, você o utiliza pensando em adicionar mais de um valor
print (familia)

familia.append("Ruby")
#usando o append, você o utiliza pensando em adicionar só mais um valor/índice
print (familia)

familia.insert(2, "Mia")
#quando você usa o insert, você adiciona um índice e já determina qual é a posição dele dentro da varíavel
#nesse caso, fiz com que ele ficasse no segundo lugar, depois do João Gabriel, Edilaine, Segundo Lugar, Olympio
print (familia)

familia.pop()
#utilizando a funçaõ pop, ele remove o último índice registrado na variável. Neste caso a Ruby
print (familia)

familia.remove("Mia")
#removeo o índice em base no nome que vocês selecionarem
print (familia)

#familia.clear()
#limpa a lista, torna ela vazia
#print (familia)

print(familia.count("Olympio"))
#saber quantos valores tem dentro da sua lista. Nesse caso eu coloquei quantos Olympio tem dentro da variável familia

idade_familia = [17, 49, 49, 27, 24]
print(idade_familia)
idade_familia.sort()
#a função sort faz com que na hora de exibir o resultado no terminal, ele printe com os índices em ordem do menor para o maior
print(idade_familia)

familia.sort()
#Aqui funciona da mesma forma, só que ele vai trazer os resultados em ordem alfabética
print(familia)

idade_familia.reverse()
#aqui ele mostra a ordem dos índices de forma inversa. Com essa variável, vai msotrar as idades do maior para o menor
print(idade_familia)

familia_2 = familia
#aqui eu criei uma cópia por referência. Eu criei uma nova variável que indica que é igual a "familia". Tudo o que eu mudar na primeira variável, vai mudar na segunda e vice-versa.
print(familia_2)
familia.remove("João Gabriel")
print(familia_2)
print(familia)
#aqui eu exclui o nome João Gabriel da minha primeira variável "familia". Porém, a segunda variável também teve o João  Gabriel exluido, pois ela é uma cópia por referência da primeira.

familia_3 = familia.copy()
#Aqui eu criei uma cópia da variável "familia". Essa nova variável não é uma referência, o exemplo está aí em baixo.
familia.remove("Olympio")
print(familia)
print(familia_3)


coordenadas = (-49, -36)
#aqui eu criei um tuple, ele é uma lista imutável, ou melhor, ela não pode ser alterada. Se você tentar tirar ou adicionar algum valor dentro dela, vai dar erro no terminal
print(coordenadas)

