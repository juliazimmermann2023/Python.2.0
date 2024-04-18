def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Não é possível dividir por zero!"
    else:
        return x / y

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação desejada: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == '1':
    print("Resultado:", soma(num1, num2))
elif opcao == '2':
    print("Resultado:", subtracao(num1, num2))
elif opcao == '3':
    print("Resultado:", multiplicacao(num1, num2))
elif opcao == '4':
    print("Resultado:", divisao(num1, num2))
else:
    print("Opção inválida. Por favor, escolha uma opção válida (1, 2, 3 ou 4).")
  
