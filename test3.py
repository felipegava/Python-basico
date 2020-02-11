operacoes = {'soma', 'subtração', 'divisão', 'multiplicação'}
_repete = 42
print("\n\t CALCULADORA v 1.0\n")
while True:
    escolha = str(input("escolha a operação:\n(soma, subtração, divisão, multiplicação)\n\n"))

    if escolha == 'sair':
        break
    elif escolha in operacoes:

        num1 = int(input("Digite o primeiro número.\n"))
        num2 = int(input("\nDigite o segundo número.\n"))

        if escolha == 'soma':
            resul = num1 + num2
        elif escolha == 'subtração':
            resul = num1 - num2
        elif escolha == 'divisão':
            resul = num1 / num2
        else:
            resul = num1 * num2

        print("resultado:", resul, "\n")
        break
    else:
        print("\nOPÇÃO INVÁLIDA!\n")