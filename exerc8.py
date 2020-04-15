idade = int(input('digite sua idade:'))
while idade < 0 or idade > 150:
	idade = int(input('digite sua idade:'))

salario = float(input('digite seu salário:'))
while salario < 0:
	salario = float(input('digite seu salário:'))

genero = input('escolha um gênero:\nM - Masculino\nF - Feminino\nO - Outro')
while genero != 'M' or genero != 'F' or genero != 'O':
	genero = input('escolha um gênero:\nM - Masculino\nF - Feminino\nO - Outro')