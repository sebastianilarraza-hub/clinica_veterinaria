from tutor import Tutor
from cachorro import Cachorro
from gato import Gato
from ave import Ave
from clinica import ClinicaVeterinaria


def menu():
    print("\n===== CLÍNICA VETERINÁRIA =====")
    print("1 - Cadastrar Tutor")
    print("2 - Cadastrar Animal")
    print("3 - Listar Tutores")
    print("4 - Listar Animais")
    print("5 - Buscar Tutor")
    print("6 - Buscar Animal")
    print("7 - Listar Animais de um Tutor")
    print("8 - Animais em Atenção Especial")
    print("9 - Sair")


def escolher_tutor(clinica):
    if len(clinica.tutores) == 0:
        print("Nenhum tutor cadastrado.")
        return None

    print("\nTutores cadastrados:")
    for i, tutor in enumerate(clinica.tutores):
        print(f"{i + 1} - {tutor.nome}")

    try:
        opcao = int(input("Escolha o tutor: "))
        if opcao < 1 or opcao > len(clinica.tutores):
            print("Opção inválida.")
            return None
        return clinica.tutores[opcao - 1]
    except ValueError:
        print("Entrada inválida. Digite o número do tutor.")
        return None


def ler_idade():
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0:
                print("A idade não pode ser negativa.")
                continue
            return idade
        except ValueError:
            print("Digite uma idade válida usando apenas números.")


def ler_peso():
    while True:
        try:
            peso = float(input("Peso: "))
            if peso <= 0:
                print("O peso deve ser maior que zero.")
                continue
            return peso
        except ValueError:
            print("Digite um peso válido. Exemplo: 12.5")


def ler_nome(mensagem):
    while True:
        nome = input(mensagem).strip()
        if nome:
            return nome
        print("O nome não pode ficar vazio.")


def main():
    clinica = ClinicaVeterinaria()

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = ler_nome("Nome: ")
            telefone = input("Telefone: ").strip()
            endereco = input("Endereço: ").strip()

            if clinica.buscar_tutor(nome) is not None:
                print("Já existe um tutor cadastrado com esse nome.")
                continue

            tutor = Tutor(nome, telefone, endereco)
            clinica.cadastrar_tutor(tutor)
            print("Tutor cadastrado com sucesso!")

        elif opcao == "2":
            tutor = escolher_tutor(clinica)

            if tutor is None:
                continue

            print("\nTipos de animal:")
            print("1 - Cachorro")
            print("2 - Gato")
            print("3 - Ave")

            tipo = input("Escolha: ").strip()
            if tipo not in ("1", "2", "3"):
                print("Tipo inválido.")
                continue

            nome = ler_nome("Nome do animal: ")
            if clinica.buscar_animal(nome) is not None:
                print("Já existe um animal cadastrado com esse nome.")
                continue

            idade = ler_idade()
            peso = ler_peso()

            if tipo == "1":
                vacina = input("Vacina antirrábica em dia? (s/n): ").strip().lower() == "s"
                animal = Cachorro(nome, idade, peso, tutor, vacina)

            elif tipo == "2":
                vacina = input("Vacina antirrábica em dia? (s/n): ").strip().lower() == "s"
                animal = Gato(nome, idade, peso, tutor, vacina)

            else:
                checkup = input("Check-up respiratório em dia? (s/n): ").strip().lower() == "s"
                animal = Ave(nome, idade, peso, tutor, checkup)

            if clinica.cadastrar_animal(animal):
                print("Animal cadastrado com sucesso!")
            else:
                print("Não foi possível cadastrar o animal.")

        elif opcao == "3":
            clinica.listar_tutores()

        elif opcao == "4":
            clinica.listar_animais()

        elif opcao == "5":
            nome = input("Nome do tutor: ").strip()
            tutor = clinica.buscar_tutor(nome)

            if tutor:
                tutor.mostrar_dados()
            else:
                print("Tutor não encontrado.")

        elif opcao == "6":
            nome = input("Nome do animal: ").strip()
            animal = clinica.buscar_animal(nome)

            if animal:
                animal.mostrar_dados()
            else:
                print("Animal não encontrado.")

        elif opcao == "7":
            nome = input("Nome do tutor: ").strip()
            clinica.listar_animais_tutor(nome)

        elif opcao == "8":
            clinica.listar_atencao_especial()

        elif opcao == "9":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Escolha uma opção de 1 a 9.")


if __name__ == "__main__":
    main()
