import random
def define_vencedor(escolha_jogador,escolha_computador):
        if escolha_jogador == escolha_computador:
            return "Empate"
        elif(
            (escolha_jogador == "papel" and escolha_computador == "pedra") or
            (escolha_jogador == "pedra" and escolha_computador == "tesoura") or
            (escolha_jogador == "tesoura" and escolha_computador == "papel")
            ):
            return "Você ganhou"
        else:
            return "Você perdeu"

def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura"]
    vitorias=0
    print ("Bem-vindo ao jogo Jokenpô!")
    print ("Escolha: Pedra, Papel ou Tesoura")

    while True:
        escolha_jogador = input("Sua escolha:").lower()
        if escolha_jogador not in opcoes:
            print ("Não temos essa opção. Tente novamente!")
            continue

        escolha_computador = random.choice(opcoes)

        print(f"Computador escolheu: {escolha_computador}")
        resultado= define_vencedor(escolha_jogador,escolha_computador)
        print(resultado)
        if resultado == "voce ganhou":
            vitorias +=1
        elif resultado =="Voce perdeu":
            -=1
        else:
            vitorias+=0
        jogar_novamente = input("Você quer jogar novamente?").lower()
        if jogar_novamente != "sim":
            break


     

if _name_ == "_main_":
    jogar_jokenpo()

        jogar_novamente = input("Você quer jogar novamente?").lower()
        if jogar_novamente != "sim":
            break


