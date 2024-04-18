print("OLÁ :)")
n1 = float(input("Escolha o primeiro número: "))
n2 = float(input("Escolha o segundo número: "))

print("Escolha uma opção:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = input("Digite o número do que vc quer fazer: ")
def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 == 0:
        return "Não é possível dividir por zero!"
    else:
        return n1 / n2

if opcao == '1':
    print("Resultado:", soma(n1, n2))
elif opcao == '2':
    print("Resultado:", subtracao(n1, n2))
elif opcao == '3':
    print("Resultado:", multiplicacao(n1, n2))
elif opcao == '4':
    print("Resultado:", divisao(n1, n2))
else:
    print("Opção inválida. Escolha uma opção (1, 2, 3 ou 4).")
  
