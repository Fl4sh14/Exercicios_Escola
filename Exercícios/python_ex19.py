bruto = float(input("Insere o valor do teu salário bruto: "))

irs = bruto * 0.18
ss = bruto * 0.11

liquido = bruto - irs - ss

print(f"Desconto IRS (18%): {irs}€")
print(f"Desconto Segurança Social (11%): {ss}€")
print(f"Salário líquido: {liquido}€")
