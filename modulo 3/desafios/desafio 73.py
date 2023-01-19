tabelaBrasileirao = ('Palmeiras' , 'Internacional' , 'Fluminense' , 'Corinthians' , 'Flamengo' , 'Athletico' , 'Atlético MG' , 'Fortaleza' , 'São Paulo' , 'América' , 'Botafogo' , 'Santos' , 'Goiás' , 'Bragantino' , 'Coritiba' , 'Cuiabá' , 'Ceará' , 'Atlético GO' , 'Avaí' , 'Juventude')

print(f'Os 5 primeiros colocados: {tabelaBrasileirao[0:5]}')
print('-'*100)
print(f'Os 4 últimos colocados: {tabelaBrasileirao[-4:]}')
print('-'*100)
print(f'Times em ordem alfabética: {sorted(tabelaBrasileirao)}')
print('-'*100)
print(f'Posição do Atlético MG: {tabelaBrasileirao.index("Atlético MG")}°')