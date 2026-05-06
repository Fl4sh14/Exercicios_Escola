# import csv

# with open("turma.csv", "r", encoding="utf-8") as f:
#     leitor = csv.reader(f) # cria o objeto leitor
#     next(leitor) # salta a 1.a linha (cabecalho)
#     for linha in leitor:
#         nome = linha[0] # 1.o campo
#         nota = linha[2] # 3.o campo
#         print(f"{nome} teve {nota}")

# import csv

# with open("turma.csv", "r", encoding="utf-8") as f:
#     leitor = csv.DictReader(f) # usa o cabeçalho automaticamente
#     for linha in leitor:
#         nome = linha["Nome"] # acesso pelo nome da coluna
#         nota = linha["Nota"]
#         print(f"{nome} teve {nota}")

# import csv
# # Ficheiro exportado do Excel portugues (usa ponto e virgula)
# with open("turma.csv", "r", encoding="utf-8") as f:
#     leitor = csv.reader(f, delimiter=";") # separador personalizado
#     for linha in leitor:
#         print(linha)

# import csv
# alunos = [
# ["Ana", "Silva", 18],
# ["Joao", "Costa", 15],
# ["Maria", "Lopes", 17]
# ]
# with open("turma.csv", "w", newline="", encoding="utf-8") as f:
#     escritor = csv.writer(f)
#     escritor.writerow(["Nome", "Apelido", "Nota"]) # cabecalho
#     escritor.writerows(alunos) # todas as linhas

# import csv
# alunos = [
# {"Nome": "Ana", "Nota": 18},
# {"Nome": "Joao", "Nota": 15},
# {"Nome": "Maria", "Nota": 17}
# ]
# campos = ["Nome", "Nota"]
# with open("turma.csv", "w", newline="", encoding="utf-8") as f:
#     escritor = csv.DictWriter(f, fieldnames=campos)
#     escritor.writeheader() # escreve o cabeçalho automaticamente
#     escritor.writerows(alunos) # escreve todos os dicionários

# import csv
# novo_aluno = ["Sofia", "Nunes", 19]
# with open("turma.csv", "a", newline="", encoding="utf-8") as f:
#     escritor = csv.writer(f)
#     escritor.writerow(novo_aluno) # acrescenta no fim do ficheiro

# import csv
# import os

# FICHEIRO = "turma.csv"
# CAMPOS = ["Nome", "Apelido", "Nota"]

# def criar_ficheiro():
#     """Cria o ficheiro com cabeçalho se ainda não existir."""
#     if not os.path.exists(FICHEIRO):
#         with open(FICHEIRO, "w", newline="", encoding="utf-8") as f:
#         csv.DictWriter(f, fieldnames=CAMPOS).writeheader()

# def adicionar_aluno(nome, apelido, nota):
#     """Adiciona um aluno ao ficheiro."""
#     with open(FICHEIRO, "a", newline="", encoding="utf-8") as f:
#         escritor = csv.DictWriter(f, fieldnames=CAMPOS)
#         escritor.writerow({"Nome": nome, "Apelido": apelido, "Nota": nota})

# def listar_alunos():
#     """Lê e apresenta todos os alunos ordenados por nota."""
#     with open(FICHEIRO, "r", encoding="utf-8") as f:
#         leitor = csv.DictReader(f)
#         alunos = list(leitor)
#         alunos_ord = sorted(alunos, key=lambda a: int(a["Nota"]), reverse=True)
#         print(f"\n{'Pos':<5} {'Nome':<15} {'Apelido':<15} {'Nota':>5}")
#         print("-" * 45)
#     for i, a in enumerate(alunos_ord, 1):
#         print(f"{i:<5} {a['Nome']:<15} {a['Apelido']:<15} {a['Nota']:>5}")

# # ── Programa principal ──────────────────────────────────────────
# criar_ficheiro()
# adicionar_aluno("Ana", "Silva", 18)
# adicionar_aluno("João", "Costa", 15)
# adicionar_aluno("Maria", "Lopes", 17)
# adicionar_aluno("Sofia", "Nunes", 19)
# listar_alunos()

