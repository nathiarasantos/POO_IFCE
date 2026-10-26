def exibir_menu():
    print("\n===== ESTOQUE DA LOJA =====")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Atualizar quantidade")
    print("4 - Exibir estoque")
    print("0 - Sair")


def ler_quantidade(mensagem):
    while True:
        try:
            quantidade = int(input(mensagem))

            if quantidade >= 0:
                return quantidade
            else:
                print("Digite uma quantidade maior ou igual a zero.")

        except ValueError:
            print("Digite um numero inteiro valido.")


def adicionar_produto(estoque, nome, quantidade):
    nome = nome.strip().title()

    if nome == "":
        print("O nome do produto nao pode ficar vazio.")

    elif nome in estoque:
        print("Esse produto ja esta cadastrado!")

    else:
        estoque[nome] = quantidade
        print("Produto cadastrado com sucesso!")


def remover_produto(estoque, nome):
    nome = nome.strip().title()

    if nome in estoque:
        del estoque[nome]
        print("Produto removido com sucesso!")

    else:
        print("Produto nao encontrado.")


def atualizar_quantidade(estoque, nome, quantidade):
    nome = nome.strip().title()

    if nome in estoque:
        estoque[nome] = quantidade
        print("Quantidade atualizada com sucesso!")

    else:
        print("Produto nao encontrado.")


def exibir_estoque(estoque):
    if len(estoque) == 0:
        print("O estoque esta vazio.")

    else:
        print("\n===== PRODUTOS EM ESTOQUE =====")

        for nome, quantidade in estoque.items():
            print(f"{nome}: {quantidade} unidade(s)")


def main():
    estoque = {}

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade = ler_quantidade("Quantidade: ")
            adicionar_produto(estoque, nome, quantidade)

        elif opcao == "2":
            nome = input("Nome do produto que deseja remover: ")
            remover_produto(estoque, nome)

        elif opcao == "3":
            nome = input("Nome do produto que deseja atualizar: ")
            quantidade = ler_quantidade("Nova quantidade: ")
            atualizar_quantidade(estoque, nome, quantidade)

        elif opcao == "4":
            exibir_estoque(estoque)

        elif opcao == "0":
            print("Programa encerrado!")
            break

        else:
            print("Opcao invalida. Tente novamente.")


main()