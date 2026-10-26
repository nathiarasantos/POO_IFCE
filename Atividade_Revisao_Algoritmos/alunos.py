def exibir_menu():
    print("\n===== CADASTRO DE ALUNOS =====")
    print("1 - Adicionar aluno")
    print("2 - Atualizar notas")
    print("3 - Remover aluno")
    print("4 - Exibir alunos e notas")
    print("5 - Exibir medias")
    print("0 - Sair")


def ler_nota():
    while True:
        try:
            nota = float(input("Digite a nota (0 a 10): "))

            if 0 <= nota <= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Digite uma nota numerica valida.")


def ler_quatro_notas():
    notas = []

    for i in range(4):
        print(f"Nota {i + 1}:")
        nota = ler_nota()
        notas.append(nota)

    return notas


def adicionar_aluno(alunos, nome, notas):
    nome = nome.strip().title()

    if nome == "":
        print("O nome nao pode ficar vazio.")
    elif nome in alunos:
        print("Esse aluno ja esta cadastrado!")
    else:
        alunos[nome] = notas
        print("Aluno cadastrado com sucesso!")


def atualizar_notas(alunos, nome, notas):
    nome = nome.strip().title()

    if nome in alunos:
        alunos[nome] = notas
        print("Notas atualizadas com sucesso!")
    else:
        print("Aluno nao encontrado.")


def remover_aluno(alunos, nome):
    nome = nome.strip().title()

    if nome in alunos:
        del alunos[nome]
        print("Aluno removido com sucesso!")
    else:
        print("Aluno nao encontrado.")


def calcular_media(notas):
    return sum(notas) / len(notas)


def exibir_alunos(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n===== ALUNOS E NOTAS =====")

        for nome, notas in alunos.items():
            print(f"\nAluno: {nome}")
            print(f"Notas: {notas}")


def exibir_medias(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n===== MEDIAS DOS ALUNOS =====")

        for nome, notas in alunos.items():
            media = calcular_media(notas)
            print(f"{nome}: media {media:.2f}")


def main():
    alunos = {}

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            notas = ler_quatro_notas()
            adicionar_aluno(alunos, nome, notas)

        elif opcao == "2":
            nome = input("Nome do aluno: ")

            if nome.strip().title() in alunos:
                notas = ler_quatro_notas()
                atualizar_notas(alunos, nome, notas)
            else:
                print("Aluno nao encontrado.")

        elif opcao == "3":
            nome = input("Nome do aluno que deseja remover: ")
            remover_aluno(alunos, nome)

        elif opcao == "4":
            exibir_alunos(alunos)

        elif opcao == "5":
            exibir_medias(alunos)

        elif opcao == "0":
            print("Programa encerrado!")
            break

        else:
            print("Opcao invalida. Tente novamente.")


main()