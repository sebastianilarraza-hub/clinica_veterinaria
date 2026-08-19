class ClinicaVeterinaria:

    def __init__(self):
        self.tutores = []
        self.animais = []

    def cadastrar_tutor(self, tutor):
        if self.buscar_tutor(tutor.nome) is not None:
            return False

        self.tutores.append(tutor)
        return True

    def cadastrar_animal(self, animal):
        if self.buscar_animal(animal.nome) is not None:
            return False

        self.animais.append(animal)
        if animal not in animal.tutor.animais:
            animal.tutor.adicionar_animal(animal)
        return True

    def listar_tutores(self):
        if len(self.tutores) == 0:
            print("Nenhum tutor cadastrado.")
            return

        print("\n===== TUTORES =====")
        for tutor in self.tutores:
            tutor.mostrar_dados()
            print("-" * 40)

    def listar_animais(self):
        if len(self.animais) == 0:
            print("Nenhum animal cadastrado.")
            return

        print("\n===== ANIMAIS =====")
        for animal in self.animais:
            animal.mostrar_dados()
            print("-" * 40)

    def buscar_tutor(self, nome):
        for tutor in self.tutores:
            if tutor.nome.lower() == nome.lower():
                return tutor
        return None

    def buscar_animal(self, nome):
        for animal in self.animais:
            if animal.nome.lower() == nome.lower():
                return animal
        return None

    def listar_animais_tutor(self, nome_tutor):
        tutor = self.buscar_tutor(nome_tutor)

        if tutor is None:
            print("Tutor não encontrado.")
            return

        tutor.listar_animais()

    def listar_atencao_especial(self):
        encontrou = False

        print("\n===== ATENÇÃO ESPECIAL =====")

        for animal in self.animais:
            if animal.precisa_atencao_especial():
                animal.mostrar_dados()
                print("-" * 40)
                encontrou = True

        if not encontrou:
            print("Nenhum animal em atenção especial.")
