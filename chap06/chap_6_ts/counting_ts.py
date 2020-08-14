#%%
from typing import MutableSequence
#%%
def fsort(a: MutableSequence, max: int) -> None:
    n = len(a)
    f = [0] * (max + 1)
    b = [0] * n

    for i in a:
        f[i] += 1

    for j in range(1, max + 1):
        f[j] += f[j - 1]

    for k in range(n - 1, -1, -1):
        f[a[k]] -= 1
        b[f[a[k]]] = a[k]

    for m in range(n):
        a[m] = b[m]
#%%
def counting(a: MutableSequence) -> None:
    fsort(a,max(a))

#%%    
if __name__ == "__main__":
    
	lst = [22,5,11,32,99,68,70]
	print(f'원본: {lst}')
	counting(lst)
	print(f'결과: {lst}')