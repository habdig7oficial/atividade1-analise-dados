from lib.funcs import *
from math import *


def print_relatorio(arr: list[float]) -> None:
    select_sort(arr)

    print(f"""
Testes Básicos:
Min: {get_min(arr)}
Sort: {arr if len(arr) < 40 else len(arr)}

Média:  {media(arr)}
Mediana: {mediana(arr)}

Variâcia Amostral: {variancia(arr)}
ariâcia Populacional: {variancia(arr, is_amostral=False)}
Desvio Padrão Amostral: {sqrt(variancia(arr))}
Desvio Padrão Populacional: {sqrt(variancia(arr, is_amostral=False))}
Coeficienciente de Variação Amostral: {sqrt(variancia(arr)) / media(arr)}
Coeficienciente de Variação Populacional: {sqrt(variancia(arr, is_amostral=False)) / media(arr)}

1° quartil: {mediana(arr[0:int(len(arr)/2)])}
3° quartil: {mediana(arr[int(len(arr) /2):len(arr)])}

    """)

arr = [291, 10.9, 47, 86, 44, 18.9, 1, 50, 190.4, 45.7, 28.5, 18.9, 16, 34, 8.6, 9.6]

print_relatorio(arr)

import csv
import sys

data_arr =[]
with open("./Video_Games_Sales_as_at_22_Dec_2016.csv") as csvfile:
	data = csv.DictReader(csvfile, delimiter=",")
	for i in data:
		data_arr.append(float(i["Global_Sales"]))

print_relatorio(data_arr)