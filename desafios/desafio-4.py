algo=input('Digite algo: ')

print('O tipo primitivo desse valor é? ',type (algo))
print('É um número? ',algo.isnumeric())
print('É alfabético ',algo.isalpha())
print('É minusculo? ',algo.islower())
print('É maiusculo? ',algo.isupper())
print('É alfanúmerico?',algo.isalnum())
print('É um espaço? ',algo.isspace())