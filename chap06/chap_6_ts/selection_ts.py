#%%
from typing import MutableSequence

#%%
def selection(a: MutableSequence) -> None:
	global countC, swap
	countC = 0
	swap = 0
	n = len(a)
	for i in range(n - 1):
		min = i
		for j in range(i + 1, n - 1):
			if a[min] > a[j]:
				min = j
			countC += 1
		a[i],a[min] = a[min],a[i]
		swap += 1

#%%
if __name__ == "__main__":
	#size = int(input("리스트 사이즈: "))
	#lst = [None]*size
	#for i in range(size):
	#	lst[i] = random.randint(0,15)
	lst = [1,3,4,6,7,8,9]
	print(f'원본: {lst}')
	selection(lst)

	print(f'결과: {lst}')
	print(f"비교횟수: {countC}")
	print(f"스왑횟수: {swap}")