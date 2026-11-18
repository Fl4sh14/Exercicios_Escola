
class Utilizador:
    def __init__(self, username, idade_inicial):
        self.username = username  # Atributo Público (+)
        self.__idade = idade_inicial  # Atributo Privado (-)

    # -------------------------------------------------------------
    # GETTER: Permite ler a idade privada
    # -------------------------------------------------------------
    def get_idade(self):
        return self.__idade

    # -------------------------------------------------------------
    # SETTER: Permite alterar a idade com validação de segurança
    # -------------------------------------------------------------
    def set_idade(self, nova_idade):
        # Validação: a idade deve ser um valor coerente
        if nova_idade > 0 and nova_idade < 120:
            self.__idade = nova_idade
            print(f'Idade de {self.username} atualizada para {self.__idade} anos.')
        else:
            print('Erro: Idade inválida! O valor não foi alterado.')


# =================================================================
# TESTE DO CÓDIGO
# =================================================================

# Criar um objeto da classe Utilizador
aluno = Utilizador('Tiago', 16)

# Acesso direto ao atributo privado (Gera erro no Python):
# print(aluno.__idade)

# USAR O GETTER (Ler o valor):
print(f'Idade atual: {aluno.get_idade()} anos.')

# USAR O SETTER (Alterar com validação):
aluno.set_idade(17)  # Funciona! Cumpre os requisitos da validação.
aluno.set_idade(-5)  # Recusado! O programa ignora o valor e dá um aviso.
