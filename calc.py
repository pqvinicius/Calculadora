
Print("BEM VINDO A CALCULADORA!")

def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

def subtracao(a, b):
    return a - b

def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por zero!"
    return a / b

def calculadora():
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Multiplicação")
    print("3. Subtração")
    print("4. Divisão")

    while True:
        escolha = input("Digite sua escolha (Opções 1/2/3/4): ")
        
        if escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print("Você escolheu somar:")
                print(f"{num1} + {num2} O resultado é:{soma(num1, num2)}")
            elif escolha == '2':
                print("Você escolheu subtrair:")
                print(f"{num1} - {num2} O resultado é:{subtracao(num1, num2)}")
            elif escolha == '3':
                print("Você escolheu multiplicar:")
                print(f"{num1} * {num2} O resultado é:{multiplicacao(num1, num2)}")
            elif escolha == '4':
                print("Você escolheu dividir:")
                print(f"{num1} / {num2} = O resultado é:{divisao(num1, num2)}")

            break

calculadora()