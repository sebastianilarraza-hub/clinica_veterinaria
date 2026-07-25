from animal import Animal


class Ave(Animal):

    idade_limite_especial = 6

    def __init__(self, nome, idade, peso, tutor, checkup_respiratorio_em_dia):
        super().__init__(nome, idade, peso, tutor)
        self.checkup_respiratorio_em_dia = checkup_respiratorio_em_dia

    def fazer_som(self):
        return "Piu piu!"

    def cuidados_especiais(self):
        cuidados = ["Check-up respiratório obrigatório a cada 6 meses"]

        if self.precisa_atencao_especial():
            cuidados.append("Animal em atenção especial devido à idade.")

        return cuidados

    def protocolo_atendimento(self):
        if self.checkup_respiratorio_em_dia:
            return "Check-up respiratório em dia."
        else:
            return "ALERTA: Check-up respiratório atrasado ou não informado."
    