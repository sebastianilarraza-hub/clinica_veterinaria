from animal import Animal


class Cachorro(Animal):

    idade_limite_especial = 8

    def __init__(self, nome, idade, peso, tutor, vacina_antirrabica_em_dia):
        super().__init__(nome, idade, peso, tutor)
        self.vacina_antirrabica_em_dia = vacina_antirrabica_em_dia

    def fazer_som(self):
        return "Au au!"

    def cuidados_especiais(self):
        cuidados = ["Vacina antirrábica anual obrigatória"]

        if self.precisa_atencao_especial():
            cuidados.append("Animal em atenção especial devido à idade.")

        return cuidados

    def protocolo_atendimento(self):
        if self.vacina_antirrabica_em_dia:
            return "Vacina antirrábica em dia."
        else:
            return "ALERTA: Vacina antirrábica atrasada ou não informada."
