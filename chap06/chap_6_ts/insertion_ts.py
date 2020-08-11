#%%
from typing import MutableSequence
#%%
def insertion(a: MutableSequence) -> None:
    global countC, swap
    swap = 0
    countC = 0
    n = len(a)
    for i in range(1, n):
        tmp = a[i]
        j = i
        while (a[j - 1] > tmp) and (j > 0):
            a[j] = a[j - 1]
            j -= 1
            countC += 1
        a[j] = tmp
        swap += 1

#%%
if __name__ == "__main__":
    #size = int(input("리스트 사이즈: "))
	#lst = [None]*size
	#for i in range(size):
	#	lst[i] = random.randint(0,15)
	lst = [6,4,3,7,1,9,8]
	print(f'원본: {lst}')
	insertion(lst)

	print(f'결과: {lst}')
	print(f"비교횟수: {countC}")
	print(f"스왑횟수: {swap}")