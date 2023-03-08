import gym
import numpy as np

ambiente = gym.make("LunarLander-v2", render_mode="human")

class ModeloDecisao():
    def __init__(self, n_entradas, n_saidas, taxa_aprendizado=0.5):
        self.pesos = np.zeros((n_entradas, n_saidas))
        self.taxa_aprendizado = taxa_aprendizado
    def prever(self, estado):
        return np.dot(estado, self.pesos)

    def atualizar(self, estado, acao, recompensa, proximo_estado):
        alvo = recompensa + np.max(self.prever(proximo_estado))
        delta = alvo - self.prever(estado)[acao]
        indices_estado = tuple(estado.astype(int))
        self.pesos[indices_estado, acao] += self.taxa_aprendizado * delta



modelo = ModeloDecisao(ambiente.observation_space.shape[0], ambiente.action_space.n)
observacao, informacao = ambiente.reset()

while True:
    acao = np.argmax(modelo.prever(observacao))


    proxima_observacao, recompensa, feito, informacao, _  = ambiente.step(acao)


    modelo.atualizar(observacao, acao, recompensa, proxima_observacao)


    observacao = proxima_observacao


    if feito:
        print("Episódio finalizado ")
        observacao, informacao = ambiente.reset()

ambiente.close()