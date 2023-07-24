#teste de função

def pessoa(nome):
    print(f"Legal saber que seu nome é {nome}")

pessoa("Pablo")
pessoa("Sérgio\n")







def joao(nome, idade, altura, jogo, amigos):
   print(f"Olá, não é nenhum segredo que meu nome é {nome}, tenho apenas {idade} anos de idade e tenho {altura} de altura. Meu jogo preferido é {jogo} e meus amigos que mais converso no momento são o {amigos}")

joao("João Gabriel", 17, 1.74, "Batman Arkham Asylum", "Guilherme e Luís\n")







def roupa(cor, marca):
    print(f"A cor de sua roupa é {cor} e a marca dela é {marca}")

roupa ("Amarela", "Aleatory\n")







def tipo_roupa (estilo):
     print(f"O estilo de roupa selecionado é {estilo}")

def tamanho_roupa (tamanho):
     print(f"O tamanho da roupa será {tamanho}")

def marca_roupa (marca):
     print(f"O marca da roupa será {marca}")

def cor_roupa (cor):
    print(f"A cor da roupa será {cor}")

def roupa(estilo, tamanho, marca, cor):
    tipo_roupa(estilo)
    tamanho_roupa(tamanho)
    marca_roupa(marca)
    cor_roupa(cor)

roupa ("Polo", "M", "Lacoste", "Preta")
