# O que são módulos? São bibliotecas, pacotes de funções e variáveis para se usar em seu sistema
# Exemplo de módulo: OS, usado no arquivo manipulacao-arquivos.py

import tools
# aqui eu importo o meu módulo, que é o arquivo tools.py


print(tools.PI)
print(tools.GRAVITY)
print(tools.highest_number([1, 2, 3, 4]))
print(tools.get_extension("text.txt"))
# aqui eu realizo a impressão de todas as variáveis e funções que foram criados lá no tools.py

# o módulo serve para você reutilizar códigos
# invés de vc ter q escreever coisas bem específicas, é só criar um módulo e usar quando for preciso

# O que é o PIP? É o gerenciador de pacotes do Python, é usado para você gerenciar bibliotecas/módulos de terceiro no Python
# https://docs.python.org/3/py-modindex... lista de modulos em python ja disponiveis para usar

# Funções de alguns módulos populares:
# numpy: biblioteca para calculos, muito utilizada em machine learning
# pillow: biblioteca que gera imagens 
# movie.py: biblitoeca que gera e faz processamento de vídeos em Python
# pytest: biblioteca que testa o seu código
# Django: framework que te ajuda no desenvolvimento web





