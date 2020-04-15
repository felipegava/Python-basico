L = [3, 4, 1, 8, 3]
maior = 0

for contador  in range(0, 5):
        if contador == 0:
                maior = L[contador]
        else:
            if L[contador] > maior:
                maior = L[contador]
                
print('O maior valor foi: ', maior)



chute = L[0]
for elemento in L:
    if elemento > chute:
        chute = elemento
print(chute)
