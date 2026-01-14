# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         res =  fibonacci(n - 1) + fibonacci(n - 2)
#         print(res)
#         return res 

# n = int(input('Digite o nº de termos: '))
# print(fibonacci(n))

#---------------------------------------------------------------------

# FOR 
n = int(input("Digite o número de termos: "))

a = 0
b = 1

for i in range(n):
    print(a)
    a, b = b, a + b

# WHILE

termos = int(input('Quantos termos você quer mostrar? '))

a = 0
b = 1
contador = 0

while contador < termos:
    print(f'{a} -> ', end=' ')
    proximo = a + b
    a = b
    b = proximo
    contador += 1