# Importando bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

# Dados fornecidos
data = {
    'x': np.arange(1, 16),
    'y': [11, 12, 24, 30, 31, 33, 61, 62, 70, 81, 84, 84, 92, 96, 97],
}
#print(data['x'])
# Criando DataFrame
df = pd.DataFrame(data)

# Parte 1: Cálculo da correlação
corr, _ = pearsonr(df['x'], df['y'])
print(f"Coeficiente de correlação: {corr}")

# Parte 2: Regressão Linear Simples
X = df['x'].values.reshape(-1, 1)
y = df['y'].values

# Ajustando o modelo
model = LinearRegression()
model.fit(X, y)

# Coeficientes
a = model.intercept_
b = model.coef_[0]
print(f"Equação de regressão: y = {a:.2f} + {b:.2f}x")

# Previsão para Gasto de Marketing de 260
#gasto_novo = np.array([[260]])
#vendas_previstas = model.predict(gasto_novo)
#print(f"Previsão de vendas para gasto de R$ 260 mil: {vendas_previstas[0]:.2f} mil")

# Parte 3: Visualização
fig, axs = plt.subplots(2)
axs[0].hist(X)
axs[1].scatter(df['x'], df['y'], color='blue', label='Dados')
axs[1].plot(df['x'], model.predict(X), color='red', label='Linha de Regressão')
fig.suptitle('Correlação:')
axs[1].legend()
plt.savefig("hello.png")
