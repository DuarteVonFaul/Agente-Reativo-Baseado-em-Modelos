class ModeloDoAmbiente:
    def __init__(self):
        self.estado = {"posição": 0, "velocidade": 0}

    def executar_acao(self, acao):
        if acao == "acelerar":
            self.estado["velocidade"] += 1
        elif acao == "desacelerar":
            self.estado["velocidade"] -= 1
        self.estado["posição"] += self.estado["velocidade"]

    def get_estado(self):
        return self.estado

class AgenteReativoBaseadoEmModelos:
    def __init__(self):
        self.modelo = ModeloDoAmbiente()

    def escolher_acao(self):
        estado = self.modelo.get_estado()
        if estado["posição"] < 10:
            return "acelerar"
        elif estado["posição"] > 20:
            return "desacelerar"
        else:
            return "manter_velocidade"

    def executar_ciclo_de_vida(self):
        while True:
            acao = self.escolher_acao()
            self.modelo.executar_acao(acao)
            estado = self.modelo.get_estado()
            print("Posição: {}, Velocidade: {}".format(estado["posição"], estado["velocidade"]))
            if estado["posição"] >= 28:
                break

agente = AgenteReativoBaseadoEmModelos()
agente.executar_ciclo_de_vida()