num_max = 10000

contador = 1
num_fatorial = 1
somatorio = 0

while contador <= num_max:
	num_fatorial *= contador

	somatorio += 1/num_fatorial
	
	contador += 1

print(somatorio)
