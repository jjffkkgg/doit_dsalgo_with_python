﻿#%%
from typing import MutableSequence
import random
countC = 0
swap = 0
#%%
def bubble_sort(a: MutableSequence) -> None:
	global swap, countC
	n = len(a)
	for i in range(n - 1):
		swap_loop = 0
		for j in range(n - i - 1):
			if a[j] > a[j + 1]:
				a[j],a[j + 1] = a[j + 1],a[j]
				swap += 1
				swap_loop += 1
			countC += 1
		if swap_loop == 0:
			break
#%%
if __name__ == "__main__":
	#size = int(input("리스트 사이즈: "))
	#lst = [None]*size
	#for i in range(size):
	#	lst[i] = random.randint(0,15)
	lst = [1,3,9,4,7,8,6]
	print(f'원본: {lst}')
	bubble_sort(lst)

	print(f'결과: {lst}')
	print(f"비교횟수: {countC}")
	print(f"스왑횟수: {swap}")