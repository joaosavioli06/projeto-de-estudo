kg = int(input('Digite seu peso: '))
alt = float(input('Agora digite sua altura: '))

imc = kg / (alt * alt)

print(f'\nSeu Índice de Massa Corporal é: {imc:.2f}kg/m²')