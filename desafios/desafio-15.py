aluguel = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

# a = aluguel * 60
# b = km * 0.15
# c = a + b

pago = (aluguel * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(pago))