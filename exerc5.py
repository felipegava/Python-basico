num = int(input('digite um número:'))

# Versão sem lista
cont = 1
while cont <= num:
	if num%cont == 0:
		print(cont,'é divisor de',num)
	cont += 1

# Versão com lista
divisores = []
cont = 1
while cont <= num:
	if num%cont == 0:
		divisores.append(cont)
	cont += 1
print('Os divisores de',num,'são',divisores)