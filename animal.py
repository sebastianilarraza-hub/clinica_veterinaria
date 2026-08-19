from abc import ABC, abstractmethod


class Animal(ABC):
    
    idade_limite_especial = 0

    def __init__(self, nome, idade, peso, tutor):
        self.nome = nome.strip()
        self.idade = idade
        self.peso = peso
        self.tutor = tutor

    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def cuidados_especiais(self):
        pass

    @abstractmethod
    def protocolo_atendimento(self):
        pass

    def precisa_atencao_especial(self):
        return self.idade >= self.idade_limite_especial

    def mostrar_dados(self):
        print("Tipo:", self.__class__.__name__)
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Peso:", self.peso)
        print("Tutor:", self.tutor.nome)
        print("Som:", self.fazer_som())

        if self.precisa_atencao_especial():
            print("Categoria: ATENÇÃO ESPECIAL")
        else:
            print("Categoria: Normal")

        print("Protocolo:", self.protocolo_atendimento())

        print("Cuidados Especiais:")
        for cuidado in self.cuidados_especiais():
            print("-", cuidado)
