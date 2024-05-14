# HUGO OTÁVIO E ANA CLARISSE
# 12. Escreva um programa em Python que gere uma lista com 6 números inteiros aleatórios, entre 1 e 60, e exiba estes números para o usuário.


import random

class Numeros:

    def init(self, numeros_aleatorio):
        self.numeros_aleatorio = []

    def gerar_numeros(self):
        self.numeros_aleatorio = random.sample(range(1, 61), 6)
        self.numeros_aleatorio.sort()

    def resultado(self):
        return self.numeros_aleatorio

numeros1 = Numeros()
numeros1.gerar_numeros()
numeros_aleatorio = numeros1.resultado()

print("Os números aleatorios foram :", numeros_aleatorio)

maior = max(numeros_aleatorio)
menor = min(numeros_aleatorio)

print("O maior número é:", maior)
print("O menor número é:", menor)