cont = 0
total = 0
termo = 1

while cont < 1000:
	total += termo
	print(termo)
	termo = termo/2
	cont += 1

print('O valor total é',total)
