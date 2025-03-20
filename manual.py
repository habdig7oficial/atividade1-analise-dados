from lib.funcs import *
from math import *

arr = [291, 10.9, 47, 86, 44, 18.9, 1, 50, 190.4, 45.7, 28.5, 18.9, 16, 34, 8.6, 9.6]
select_sort(arr)

print(f"""
Testes Básicos:
Min: {get_min(arr)}
Sort: {arr}

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
