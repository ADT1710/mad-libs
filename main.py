import pokemon, naruto, vingadores
import random

print('Defina as palavras solicitadas e veja como ficariam suas frases!')
verbo1 = input('Primeiro verbo: ')
verbo2 = input('Segundo verbo:' )
substantivo1 = input('Primeiro substantivo: ')
substantivo2 = input('Segundo substantivo: ')

m = random.choice([pokemon,naruto,vingadores])
m.mad_libs(verbo1,verbo2,substantivo1,substantivo2)