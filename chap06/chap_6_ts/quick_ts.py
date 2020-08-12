#%%
from typing import MutableSequence
#%%
def quick(a: MutableSequence, left: int, right: int) -> None:
    pl = left
    pr = right
    pv = (left + right) // 2
    while pl <= pr:
        while a[pl] < a[pv]:
            pl += 1
        while a[pr] > a[pv]:
            pr -= 1
        if pl <= pr:
            a[pl],a[pr] = a[pr],a[pl]
            pl += 1
            pr -= 1
    if pr > left:
        quick(a, left, pr)
    if pl < right:
        quick(a, pl, right)
#%% 
if __name__ == "__main__":
    lst = [5,8,4,2,6,1,3,9,7]
    print(f'원본: {lst}')
    quick(lst,0,len(lst) - 1)
    print(f'결과: {lst}')