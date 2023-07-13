# sets são listas desordenadas, não aceita valores duplicados. Vc consegue adicionar e remover valores dentro do set, mas não pode modificar valores que estão dentro dele.

frutas = {"maça", "laranja", "Abacaxi"}
print (frutas)

# não tem uma ordem correta, vc nunca sabe a ordem que ele vai trazer pra vc
# o set usa [] e o set usa {}

#como é uma lista desordenada, ele não tem índice, pois é desordenado
# ele não aceita valores duplicados, então se você adicionar mais um valor q seja igual, não vai dar erro no código, mas n vai mudar em nada


# frutas = {"maça", "laranja", "Abacaxi", "maça", "laranja"}
# print (frutas)

#esse é o exemplo de valor duplicado, n altera nada

frutas.add("pera")
print(frutas)

# aqui eu adiciono uma nova fruta dentro do set

frutas.remove("maça")
print(frutas)

# aqui eu removo um item dentro do set

frutas.pop()
print(frutas)

#como é pop,ele removeria o último valor da lista, mas como a lista não é ordenada, então ele remove um aleatório

set2 = {0,3,50,-80}
set3 = {True, False, False, True}
set4 = {"João G", 17, True}

print(set2)
print(set3)
print(set4)
