#%%
from typing import MutableSequence

#%%
def heap_sort(a: MutableSequence) -> None:

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        temp = a[left]
        parent = left

        while parent < (right + 1) // 2:
            cl = parent * 2 + 1
            cr = cl + 1
            child = cr if cr <= right and a[cl] < a[cr] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n - 1) // 2, -1, -1):
        down_heap(a,i,n - 1)

    for j in range(n - 1, 0, -1):
        a[0],a[j] = a[j],a[0]
        down_heap(a,0,j - 1)
#%%
if __name__ == "__main__":

	lst = [6,4,3,7,1,9,8]
	print(f'원본: {lst}')
	heap_sort(lst)

	print(f'결과: {lst}')

