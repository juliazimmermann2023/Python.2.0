def gravar_lista(lista):
    gravar_arq = input("Digite o nome do arquivo: ")
    with open(gravar_arq, "w") as arquivo:  # 'w' deve ser minúsculo
        for item in lista:
            arquivo.write(item + "\n")  # 'in' deve ser '\n' para nova linha
        print("Gravado", gravar_arq)
    
def carregar_lista():
    nome_arquivo = input("Digite o nome do arquivo a ser carregado:")
    try:
        with open(nome_arquivo, "r") as arquivo:
            lista.clear()
            for linha in arquivo: 
                lista.append(linha.strip())
        print("Lista carregada co suceso.")

    except FileNotFoundError:
        print("arquivo não encontrado.")
    except Exception as e: 
        print("Ocorreu um erro".e)
        
def ordenar_lista(lista.sort()):
    print("Lista ordenada com sucesso")

def minha_lista():
    lista = []  
    while True:
        print("Bem-vindo a sua lista e mercado!!!")
        print("Escolha uma opção:")
        print("1. Mostrar a lista atual;")
        print("2. Inserir um novo item na sua lista de mercado;")
        print("3. Excluir um item da sua lista;")
        print("4. Gravar a lista em um arquivo;")
        print("5. Sair da lista.")
        escolha = input("Digite o número do que vc deseja fazer: ")
        if escolha == "1":
            print("Lista atual:")
            for item in lista:
                print(item)
        elif escolha == "2":
            item = input("Digite o novo item: ")
            lista.append(item)
            print(f"{item} foi adicionado à sua lista de mercado.")
        elif escolha == "3":
            item = input("Digite o item que vc deseja ser removido: ")
            if item in lista:
                lista.remove(item)
                print(f"{item} foi removido da sua lista.")
            else:
                print(f"{item} não está na sua lista.")
        elif escolha == "4":
            gravar_lista(lista)  5
        elif escolha == "5":
            print("Vc saiu da lista.")
            break
        else:
            print("Opção incorreta, tente novamente.")

if __name__ == "__main__":
    minha_lista()
