from statistics import *
#from matplotlib.pyplot import *

def print_relatorio(arr: list[float]):
	print(f"""
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


## Dataset
arr = [291, 10.9, 47, 86, 44, 18.9, 1, 50, 190.4, 45.7, 28.5, 18.9, 16, 34, 8.6, 9.6]

arr.sort()
print_relatorio(arr)


print("===================")



import csv
import sys

data_arr =[]
with open("./Video_Games_Sales_as_at_22_Dec_2016.csv") as csvfile:
	data = csv.DictReader(csvfile, delimiter=",")
	for i in data:
		data_arr.append(float(i["Global_Sales"]))

print_relatorio(data_arr)
