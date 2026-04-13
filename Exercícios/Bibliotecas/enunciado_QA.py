import random
def sistema_seguranca(energia):
    if energia < 10:
        return "CRÍTICO"
    else:
        return "ESTÁVEL"
def evento_espacial():
    return random.randint(1, 5)
def iniciar_missao():
    distancia = 0
    energia = 50
    print("--- LANÇAMENTO DA SONDA ---")
    while distancia < 100:
        estado = sistema_seguranca(energia)
        if estado == "CRÍTICO":
            print(" Falha de energia! Missão abortada.")
            break
        print(f"Distância: {distancia}km | Energia: {energia}%")
        opcao = input("1-Acelerar | 2-Recarregar: ")
        if opcao == "1":
            distancia = distancia + 25
            energia = energia - 15
            if evento_espacial() == 1:
                print(" Radiação detetada! Perda de energia.")
                energia = energia - 20
        elif opcao == "2":
            energia = energia + 30
            print(" Painéis solares ativos.")
        if distancia >= 100:
            print(" Sucesso! A sonda chegou a Júpiter.")
iniciar_missao()
