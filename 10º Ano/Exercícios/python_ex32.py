senha = 1234
tentati = 0

# tem que se usar while porque no python não existe repeat
while True:  
    senha = input("Digite a senha: ")
    if senha == senha:
        print("Acesso permitido")
        break
    else:
        tentati += 1

print(f"Quantidade de tentativas erradas: {tentati}")
