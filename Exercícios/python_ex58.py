def media_fixa():
    num1 = float(input("Digite a primeira nota: "))
    num2 = float(input("Digite a segunda nota: "))
    num3 = float(input("Digite a terceira nota: "))
    media = (num1 + num2 + num3) / 3
    print(f"A média das notas {num1}, {num2} e {num3} é: {media}")
    return media
media_fixa()