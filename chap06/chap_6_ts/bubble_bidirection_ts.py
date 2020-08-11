#%%
from typing import MutableSequence
countC = 0
swap = 0
#%%
def shaker_sort(a: MutableSequence) -> None:
	global swap, countC
	right = len(a) - 1
	left = 0
	i = 0
	last = right
	while left < right:
		#swap_loop = 0
		for j in range(right,left, -1):
			if a[j] < a[j - 1]:
				a[j],a[j - 1] = a[j - 1],a[j]
				swap += 1
				#swap_loop += 1
				last = j
			countC += 1
		left = last
		#if swap_loop == 0:
		#	break
		for j in range(left, right):
			if a[j] > a[j + 1]:
				a[j],a[j + 1] = a[j + 1],a[j]
				swap += 1
				last = j
			countC += 1
		right = last

#%%
if __name__ == "__main__":
	#size = int(input("리스트 사이즈: "))
	#lst = [None]*size
	#for i in range(size):
	#	lst[i] = random.randint(0,15)
	lst = [9,1,3,4,6,7,8]
	print(f'원본: {lst}')
	shaker_sort(lst)

	print(f'결과: {lst}')
	print(f"비교횟수: {countC}")
	print(f"스왑횟수: {swap}")