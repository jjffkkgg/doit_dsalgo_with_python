#%%
from typing import Any, MutableSequence
#%%
def reverse_array_ts(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2):
        a[i],a[n-i-1] = a[n-1-i],a[i]

#%%

if __name__ == "__main__":
    nx = int(input("원소수:"))
    x = [None]*nx
    for j in range(nx):
        x[j] = int(input(f"x[{j}] = "))
        
    reverse_array_ts(x)

    print(f"x_r = {x}")