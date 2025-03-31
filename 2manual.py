from lib.funcs import *
from math import *
from matplotlib.pyplot import *

class RegressaoLinear:
    def __init__(self, x: list[float], y: list[float]):
        self.x = x
        self.y = y
        self.sx = sqrt(variancia(self.x, is_amostral=False))
        self.sy = sqrt(variancia(self.y, is_amostral=False))
        self.sxx = soma_arr(exp_arr(self.x, 2)) - soma_arr(self.x) ** 2 / len(self.x)
        self.sxy = mul_arrs(self.x, self.y) - (soma_arr(self.x) * soma_arr(self.y)) / len(self.x)
        self.b =  self.sxy / self.sxx
        self.a = (soma_arr(self.y) - self.b * soma_arr(self.x)) / len(self.x)

    def prever(self, nx: list[float]):
        return self.a + self.b * nx

    def plot(self, filename: str):
        fig, axs = subplots(2)
        axs[0].hist(self.x)
        axs[1].scatter(self.x, self.y, color='blue', label='Dados')
        axs[1].axline((self.x[0], self.y[0]), (self.x[-1], self.y[-1]), color='red', label='Linha de Regressão', marker='o')
        fig.suptitle('Correlação:')
        axs[1].legend()
        savefig(filename)


y = [11, 12, 24, 30, 31, 33, 61, 62, 70, 81, 84, 84, 92, 96, 97]
x = [i + 1 for i in range(0, len(y))]



regresao = RegressaoLinear(x, y)
print(regresao.sxx)
print(regresao.sxy)
print(f"b = {regresao.b}\na = {regresao.a}")

print(regresao.prever(1))
regresao.plot("2manual.png")