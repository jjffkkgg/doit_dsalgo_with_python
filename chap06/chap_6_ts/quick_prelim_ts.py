#%%
from typing import MutableSequence
#%%
def partition(a: MutableSequence) -> None:
    n = len(a)
    pl = 0
    pr = n - 1
    pv = (pl + pr) // 2
    while pl <= pr:
        while a[pl] < a[pv]:
            pl += 1
        while a[pr] > a[pv]:
            pr -= 1
        if pl <= pr:
            a[pl],a[pr] = a[pr],a[pl]
            pl += 1
            pr -= 1
    print(f'pl: {pl}')
    print(f'pr: {pr}')
#%% 
if __name__ == "__main__":
    #lst = [5,7,1,4,6,2,3,9,8]
    lst = [1,8,7,4,5,2,6,3,9]
    partition(lst)
    print(f'lst: {lst}')