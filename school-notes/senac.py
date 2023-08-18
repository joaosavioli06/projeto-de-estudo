# Rode o código no terminal e seja feliz :)
# João Gabriel Savioli - 3ºA

import textwrap

nome = input("Digite o seu nome: ")
print(f"\nBem vindo {nome}!")
print(f"\nO objetivo deste pequeno script utilizando Python, é realizar o trabalho programando. Desta forma, eu já realizo 2 coisas de uma vez só :)")
print("Eu já tenho uma certa experiência e conhecimento desta linguagem, mas meu objetivo é se aprofundar ainda mais...")

print("\nNeste trabalho, os tópicos a serem respondidos são: ")
lista = ["\nLinguagem Python", "Apps em Python", "Ferramentas", "Estudo de Caso", "Protótipo"]

for linha in lista:
    print(linha)
    print("----------------")


def formatacao(texto, largura):
    linhas_formatadas = textwrap.wrap(texto, width=largura)
    for linha in linhas_formatadas:
        print(linha)


print("\n * Linguagem Python")
texto1 = ("\nPython é uma linguagem de programação popular por sua sintaxe fácil de entender e usar. É usada em diversas áreas, como desenvolvimento web, análise de dados e aprendizado de máquina. Possui uma comunidade ativa e muitas bibliotecas úteis. Python é gratuito, de código aberto e tem duas versões principais: Python 2 (descontinuado) e Python 3 (recomendado). É uma ótima escolha para iniciantes e programadores experientes.")
formatacao(texto1, 70)


print("\n * Aplicativos em Python")
texto2 = ("\nPython pode ser usado para criar uma ampla variedade de aplicativos, incluindo aplicativos de linha de comando, aplicativos desktop com interfaces gráficas, aplicativos web, análise de dados, aprendizado de máquina, automação, processamento de imagens e muito mais. Sua versatilidade o torna adequado para desenvolver desde simples scripts até aplicativos complexos e robustos.")
formatacao(texto2, 70)

print("\n * Ferramentas para o desenvolvimento em Python")
texto2 = ("\nPara um desenvolvimento eficaz em Python, você pode aproveitar várias ferramentas: Escolha um bom ambiente de desenvolvimento integrado (IDE) como PyCharm ou Visual Studio Code. Considere editores de texto como Sublime Text ou Atom para projetos mais simples. Use Git e GitHub para controle de versão e colaboração. Você também pode utilizar várias bibliotecas para te auxiliar durante o seu código, como a que está sendo utilizado neste script (textwrap)")
formatacao(texto2, 70)

print("\n * Estudo de Caso")
texto3 = ("\nUm estudo de caso em Python é um exemplo prático onde você usa a linguagem para resolver um problema real. Envolve escrever código para abordar um cenário específico, executá-lo, analisar os resultados e aprender com a experiência. É uma maneira prática de aplicar e aprender conceitos de programação em Python.")
formatacao(texto3, 70)

print("\n * Protótipo")
texto4 = ("\nSerá feito no laboratório nas próximas aulas")
formatacao(texto4, 70)

print("\n\nVocê gostou deste script? Se sim, obrigado! Senão, me encontre em sala de aula e me fale o porquê, estou aberto a sugestões e críticas construtivas.")
print("Thanks!")

