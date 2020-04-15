x = 0
soma = 1
num = 1
fatorial = 1

while x < 1000:
        num += 1
        fatorial = fatorial * num
        soma += 1/fatorial
        x += 1
        
print(' A soma de', x, 'termos dos inversos dos fatoriais é = ', soma)

