num = int(input())

cont = 0
fatorial = 1

while cont < num:
	cont += 1 #cont = cont + 1
	fatorial *= cont # fatorial = fatorial * cont
print(fatorial)