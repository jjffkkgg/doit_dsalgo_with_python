#%%
from typing import MutableSequence
#%%
def shell(a: MutableSequence) -> None:
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h,n):
            j = i - h
            tmp = a[i]
            while (a[j] > tmp) and (j >= 0):
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 2
#%%
if __name__ == "__main__":
	#size = int(input("리스트 사이즈: "))
	#lst = [None]*size
	#for i in range(size):
	#	lst[i] = random.randint(0,15)
	lst = [8,1,4,2,7,6,3,5]
	print(f'원본: {lst}')
	shell(lst)

	print(f'결과: {lst}')
	#print(f"비교횟수: {countC}")
	#print(f"스왑횟수: {swap}")