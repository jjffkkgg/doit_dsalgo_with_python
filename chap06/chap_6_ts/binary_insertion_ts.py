#%%
from typing import MutableSequence
import bisect as bi

def bin_insertion(a: MutableSequence) -> None:
	n = len(a)
	for i in range(1,n):
		bi.insort(a,a.pop(i),0,i)

#%%
if __name__ == "__main__":
	#size = int(input("리스트 사이즈: "))
	#lst = [None]*size
	#for i in range(size):
	#	lst[i] = random.randint(0,15)
	lst = [6,4,3,7,1,9,8]
	print(f'원본: {lst}')
	bin_insertion(lst)

	print(f'결과: {lst}')
	#print(f"비교횟수: {countC}")
	#print(f"스왑횟수: {swap}")