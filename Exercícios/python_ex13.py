pb = float(input("Introduz o preço base do produto: "))

iva = pb * 0.23            
ml = pb * 0.25  

pf = pb + iva + ml

print(f"Acréscimo de IVA (23%): {iva}€")
print(f"Acréscimo da margem de lucro (25%): {ml}€")
print(f"Preço final do produto: {pf}€")
