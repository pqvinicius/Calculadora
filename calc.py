print("Welcome to Python Calculator 3.2 / Bem-vindo à Calculadora Python 3.2")

def soma(a, b):
    return a + b

def div(a, b):
    if b == 0:
        return None
    else:
        return a / b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def selecionar_idioma():
    while True:
        print("\nChoose your language / Escolha seu idioma:")
        print("1. English")
        print("2. Português")
        idioma = input("Your choice / Sua escolha (1/2): ")
        if idioma in ['1', '2']:
            return idioma
        else:
            print("Invalid option / Opção inválida. Please try again / Tente novamente.")

idioma = selecionar_idioma()

if idioma == '1':
    name = input("What's your name? ")
else:
    name = input("Qual seu nome? ")

def calculadora():
    while True:
        if idioma == '1':
            print("\nSelect an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")
            escolha = input("Enter your choice (1/2/3/4/5): ")
        else:
            print("\nSelecione a operação:")
            print("1. Soma")
            print("2. Subtração")
            print("3. Multiplicação")
            print("4. Divisão")
            print("5. Sair")
            escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha == '5':
            if idioma == '1':
                print(f"Thanks for using the calculator, {name}! See you next time!")
            else:
                print(f"Obrigado por usar a calculadora, {name}! Até a próxima!")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                if idioma == '1':
                    num1 = float(input(f"{name}, enter the first number: "))
                    num2 = float(input(f"{name}, enter the second number: "))
                else:
                    num1 = float(input(f"{name}, escolha o primeiro número: "))
                    num2 = float(input(f"{name}, escolha o segundo número: "))

                if escolha == '1':
                    if idioma == '1':
                        print(f"You chose addition: {num1} + {num2} = {soma(num1, num2)}")
                    else:
                        print(f"Você escolheu somar: {num1} + {num2} = {soma(num1, num2)}")
                elif escolha == '2':
                    if idioma == '1':
                        print(f"You chose subtraction: {num1} - {num2} = {sub(num1, num2)}")
                    else:
                        print(f"Você escolheu subtrair: {num1} - {num2} = {sub(num1, num2)}")
                elif escolha == '3':
                    if idioma == '1':
                        print(f"You chose multiplication: {num1} * {num2} = {multi(num1, num2)}")
                    else:
                        print(f"Você escolheu multiplicar: {num1} * {num2} = {multi(num1, num2)}")
                elif escolha == '4':
                    resultado = div(num1, num2)
                    if resultado is not None:
                        if idioma == '1':
                            print(f"You chose division: {num1} / {num2} = {resultado}")
                        else:
                            print(f"Você escolheu dividir: {num1} / {num2} = {resultado}")
                    else:
                        if idioma == '1':
                            print("Cannot divide by zero.")
                        else:
                            print("Não é possível dividir por zero.")
            except ValueError:
                if idioma == '1':
                    print("Please enter valid numbers.")
                else:
                    print("Por favor, insira números válidos.")
        else:
            if idioma == '1':
                print("Invalid option. Please try again.")
            else:
                print("Opção inválida. Tente novamente.")

calculadora()