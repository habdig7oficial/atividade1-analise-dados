from math import *

def media(arr: list[float]) -> float:
	sum = 0
	for i in arr:
		sum += i
	return sum / len(arr)

def get_min(arr: list[float]) -> tuple[float, int]:
	v_min = arr[0]
	index = 0
	for i in range(len(arr)):
		if arr[i] < v_min:
			v_min = arr[i]
			index = i
	return v_min, index

def select_sort(arr: list[float]) -> None:
	for i in range(len(arr)):
		elem, pos = get_min(arr[i:len(arr)])
		arr[pos + i] = arr[i]
		arr[i] = elem

def mediana(arr: list[float]) -> float:
	select_sort(arr)

	if len(arr) % 2 == 0:
		m = int(len(arr) / 2)
		return (arr[m] + arr[m-1]) / 2
	else:
		return arr[int(len(arr) / 2)]

def soma_arr(arr: list[float]) -> float:
	acc = 0
	for i in arr:
		acc += i
	return acc

def variancia(arr: list[float], is_amostral: bool = True) -> float:
	med = media(arr)
	s_arr = []
	for i in arr:
		s_arr.append((i - med) ** 2)
	if is_amostral == True:
		return soma_arr(s_arr) / (len(arr) - 1)
	else:
		return soma_arr(s_arr) / len(arr)


def mul_arrs(arr1: list[float], arr2: list[float]) -> float:
	acc = 0
	for x, y in zip(arr1, arr2):
		acc += x * y
	return acc

def exp_arr(arr: list[float], exp: int) -> float:
	new_arr = [None] * len(arr)
	for i in range(0, len(arr)):
		new_arr[i] = arr[i] ** exp
	return new_arr
