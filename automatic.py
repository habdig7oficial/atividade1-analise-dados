from statistics import *
from matplotlib.pyplot import *

def print_relatorio(arr: list[float], name: str, title: str):
	print(f"""
Arr: {arr if len(arr) < 40 else 'grande pra caramba'}
Max Index: {arr.index(max(arr))}
Média: {mean(arr)}
Mediana: {median(arr)}

Variância Populacional: {pvariance(arr)}
Variância Amostral: {variance(arr)}
Desvio Padrão Populacional: {pstdev(arr)}
Desvio Padrão Amostral: {stdev(arr)}

Coeficiente de Variação Populacional: {pstdev(arr)/mean(arr)}
Coeficiente de Variação Amostral: {stdev(arr)/mean(arr)}

1° quartil: {median(arr[0:int(len(arr) /2)])}
3° quartil: {median(arr[int(len(arr) /2):len(arr)])}
""")
	fig, axs = subplots(2)
	fig.suptitle(title)
	axs[0].set_yscale("log" if len(arr) > 100 else "linear")
	axs[0].hist(arr)
	axs[1].boxplot(arr)
	savefig(name)


## Dataset
arr = [11, 12, 24, 30, 31, 33, 61, 62, 70, 81, 84, 84, 92, 96, 97]
arr.sort()
print_relatorio(arr, "manual_dataset.png", "Dataset EMPÍRICO (obrigado borba)")


print("===================")



import csv
import sys

data_arr =[]
with open("./Video_Games_Sales_as_at_22_Dec_2016.csv") as csvfile:
	data = csv.DictReader(csvfile, delimiter=",")
	for i in data:
		data_arr.append(float(i["EU_Sales"]))

print_relatorio(data_arr, "real_dataset.png", "Vendas de jogos em 22 de dezembro de 2016")
