class Tutor:

    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def listar_animais(self):
        if len(self.animais) == 0:
            print("Este tutor não possui animais cadastrados.")
            return

        for animal in self.animais:
            animal.mostrar_dados()
            print("-" * 40)

    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("Telefone:", self.telefone)
        print("Endereço:", self.endereco)
        print("Quantidade de animais:", len(self.animais))