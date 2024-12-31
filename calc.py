print("Bem Vindo à Calculadora Python 3.2")

def soma(a, b):
    return a + b

def div(a, b):
    if b == 0:
        print("Não é possível dividir por zero")
        return None
    else:
        return a / b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

name = input("Qual seu nome? ")

def calculadora():
    while True:
        print(f"\nSelecione a operação {name}:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite sua escolha (Opções 1/2/3/4/5): ")

        if escolha == '5':
            print(f"Obrigado por usar a calculadora, {name}! Até a próxima!")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input(f"{name}, escolha o primeiro número: "))
                num2 = float(input(f"{name}, escolha o segundo número: "))

                if escolha == '1':
                    print("Você escolheu somar:")
                    print(f"{num1} + {num2} = {soma(num1, num2)}")
                elif escolha == '2':
                    print("Você escolheu subtrair:")
                    print(f"{num1} - {num2} = {sub(num1, num2)}")
                elif escolha == '3':
                    print("Você escolheu multiplicar:")
                    print(f"{num1} * {num2} = {multi(num1, num2)}")
                elif escolha == '4':
                    resultado = div(num1, num2)
                    if resultado is not None:
                        print(f"{num1} / {num2} = {resultado}")
            except ValueError:
                print("Por favor, insira números válidos.")

        else:
            print("Opção inválida. Tente novamente.")

calculadora()