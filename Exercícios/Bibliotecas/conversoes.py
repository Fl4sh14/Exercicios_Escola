def separador():
    print('-=' * 20)

def converter_celsius():
    celsius = float(input('ºC: '))
    fah = celsius * 1.8 + 32
    print(f'{celsius} ºC são {fah} ºF!')
    separador()

def converter_fahrenhiet():
    fah = float(input('ºF: '))
    celsius = (fah - 32) / 1.8
    print(f'{fah} ºF são {celsius} ºC!')
    separador()

def converter_quilometros():
    qui = float(input('Km: '))
    milhas = qui * 0.621371
    print(f'{qui} km são {milhas} mi!')
    separador()

def converter_milhas():
    mil = float(input('Milhas: '))
    km = mil / 0.621371
    print(f'{mil}mi são {km} km!')
    separador()
