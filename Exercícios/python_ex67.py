salario_bruto = int(input('Insira o salário bruto para calcular o líquido: '))
desconto_IRS_SS = 28.3
horas_extra = 293.20 
salario_liquido = salario_bruto - desconto_IRS_SS + horas_extra
print(f'O resultado de salario_liquido: {salario_liquido}')
print(f'O resultado do salário líquido sem taxas: {salario_liquido * 0.283 }')
print(f'O resultado se sb {salario_liquido}')
