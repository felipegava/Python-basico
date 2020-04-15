L = [3, 4, 6, 12, 13, 14, 87, 78, 99, 100]

qtos_pares = 0

for elemento in L:
        if elemento%2 == 0:
            qtos_pares += 1
print('Existem', qtos_pares, 'numeros pares')

