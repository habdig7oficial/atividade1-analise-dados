# Importando bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

# Dados fornecidos
data = {
    'x': np.arange(1, 16),
    'y': [200, 250, 300, 150, 180, 220, 270, 210, 230, 190, 280, 240],
}

# Criando DataFrame
df = pd.DataFrame(data)

# Parte 1: Cálculo da correlação
corr, _ = pearsonr(df['x'], df['y'])
print(f"Coeficiente de correlação: {corr}")

# Parte 2: Regressão Linear Simples
X = df['Gasto_Marketing'].values.reshape(-1, 1)
y = df['Vendas'].values

# Ajustando o modelo
model = LinearRegression()
model.fit(X, y)

# Coeficientes
a = model.intercept_
b = model.coef_[0]
print(f"Equação de regressão: y = {a:.2f} + {b:.2f}x")

# Previsão para Gasto de Marketing de 260
gasto_novo = np.array([[260]])
vendas_previstas = model.predict(gasto_novo)
print(f"Previsão de vendas para gasto de R$ 260 mil: {vendas_previstas[0]:.2f} mil")

# Parte 3: Visualização
plt.scatter(df['Gasto_Marketing'], df['Vendas'], color='blue', label='Dados')
plt.plot(df['Gasto_Marketing'], model.predict(X), color='red', label='Linha de Regressão')
plt.xlabel('Gasto em Marketing (R$ mil)')
plt.ylabel('Vendas (mil)')
plt.title('Gasto em Marketing vs Vendas')
plt.legend()
plt.show()