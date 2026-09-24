import random

def gerar_numero():
    return random.randint(1, 20)

def pedir_tentativa():
    return int(input("Adivinha o número (1 a 20): "))

def verificar_tentativa(numero_secreto, tentativa):
    if tentativa < numero_secreto:
        print("O número secreto é maior.")
        return False
    elif tentativa > numero_secreto:
        print("O número secreto é menor.")
        return False
    else:
        print("Parabéns! Acertaste no número.")
        return True

def mostrar_resumo(tentativas):
    print("\nResumo do jogo:")
    print("Tentativas feitas:", tentativas)
    print("Número de tentativas:", len(tentativas))

numero_secreto = gerar_numero()
tentativas = []
acertou = False

print("=== JOGO: ADIVINHA O NÚMERO ===")

while not acertou:
    tentativa = pedir_tentativa()
    tentativas.append(tentativa)
    acertou = verificar_tentativa(numero_secreto, tentativa)

mostrar_resumo(tentativas)
