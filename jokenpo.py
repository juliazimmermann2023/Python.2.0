import random
import jogo
def jogar_jokenpo():
    
    opcoes = ["pedra", "papel", "tesoura"]
    print ("Bem-vindo ao jogo Jokenpô!")
    print ("Escolha: Pedra, Papel ou Tesoura")

    while True:
        escolha_jogador = input("Sua escolha:").lower()
        if escolha_jogador not in opcoes:
            print ("Não temos essa opção. Tente novamente!")
            continue

        escolha_computador = random.choice(opcoes)
        print(f"Computador escolheu:{escolha_computador}")
        if escolha_jogador == escolha_computador:
            print("EMPATE!!")
        elif (
            (escolha_jogador=="papel" and escolha_computador=="pedra")
            (escolha_jogador=="tesoura" and escolha_computador== "papel")or
            (escolha_jogador=="papel" and escolha_computador=="pedra")
            ): 
            print("Vc venceu!!!!")
        else:
            print("Vc perdeu :(")
        jogar_novamente=input("Vc quer jogar novamente").lower()
        if jogar_novamente!="sim":
            break
    if __name__ == "__main__":
        jogar_jokenpo()
