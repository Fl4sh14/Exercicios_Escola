def km_para_milhas(km):
    """Converte quilómetros para milhas."""
    milhas = km * 0.621371
    return milhas

km = float(input("Introduza a distância em quilómetros: "))
resultado = km_para_milhas(km)

print(f"{km} quilómetros equivalem a {resultado} milhas.")
