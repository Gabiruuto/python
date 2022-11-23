mo = float(input('Quanto dinheiro você tem na carteira?  R$'))

print('Com R${} você pode comprar US$ {:.2f} Dolares \n Pode comprar €{:.2f} Euros \n Pode comprar ¥{:.2f} Ienes'.format(mo, mo / 5.30, mo / 5.17, mo * 28.38))