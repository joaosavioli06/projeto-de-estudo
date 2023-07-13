# os dicionários são uma coleção de chave e de valor. No dicionário vc diz a chave, e ele retorna o valor para você daquela chave
# eles não são ordenados. mas vc pode buscar um dicionário especiífico passando a chave dele, não aceitam valores duplicados e ele é mutável


#a primeira palavra simboliza a chave, e a segunda é o valor


meses = {
    "Jan" : "Janeiro",
    "Fev" : "Fevereiro",
    "Mar" : "Março",
    "Apr" : "Abril",
    "May" : "Maio",
    "Jun" : "Junho", 
    "Jul" : "Julho",
    "Aug" : "Agosto",
    "Sep" : "Setembro",
    "Oct" : "Outubro",
    "Nov" : "Novembro",
    "Dec" : "Dezembro",
}

print(meses)
# ele não tem um índice, mas tem uma chave. Para chamar uma chave específica, basta fazer desta forma
print(meses["Jan"])


# print(meses["Abc"])
# aqui retorna um erro, pois essa chave n existe dentro do dicionário, e nenhum valor tbm

print(meses.get("Abc"))
# se vc chamar ele com o "get" usando o colchetes, pois precisa usar, ele vai retornar "None"

print(meses.get("Abc","Janeiro"))
# aqui, eu coloco um segundo parâmetro/valor padrão para printar, caso o primeiro valor seja inválido

print(meses.get("Oct","Janeiro"))
# aqui ele printa Outubro mesmo, pois o valor de "Oct" realmente existe

print(len(meses))
# como usa o len, ele mostra a quantidade de resultados. Funciona da mesma forma no set