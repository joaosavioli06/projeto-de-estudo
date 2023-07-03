#def big_mac():
#    print("Sanduíche Big Mac")

#print("inicio")
#big_mac()
#print("fim")

def fazer_big_mac(nome):
     print(f"Sanduíche Big Mac {nome}")

#fazer_big_mac("João")
#fazer_big_mac("JG")
#fazer_big_mac("JA")

def fazer_batata(tamanho):
     print(f"Batata {tamanho}")

def preparar_refri(tipo, tamanho):
     print(f"{tipo} {tamanho}")

#fazer_big_mac("João")
#fazer_batata("Grande")
#preparar_refri("Coca", "Média")

def fazer_combo_big_mac(nome, tamanho_batata, tipo_refri, tamanho_refri):
     fazer_big_mac(nome)
     fazer_batata(tamanho_batata)
     preparar_refri(tipo_refri, tamanho_refri)

#fazer_combo_big_mac("João", "Grande", "Coca", "Média")

def soma_num(num1, num2):
     return num1 + num2

#resultado = soma_num(15,20)
#print(resultado)

def maior_num(lista_num):
     lista_num.sort()
     lista_num.reverse()
     maior_num = lista_num[0]
     return maior_num

resultado = maior_num([321, 213, -3123, 31, 432, 12, -34, -134, 134])
print(resultado)
