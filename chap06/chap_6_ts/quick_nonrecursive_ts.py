#%%
from typing import MutableSequence
from stack import stack
#%%
def quick(a: MutableSequence, left: int, right: int) -> None:
    range = stack(right - left + 1)

    range.push((left, right))

    while not range.is_empty():
        pl = left
        pr = right
        pl,pr = left, right = range.pop()

        while pl <= pr:
            while a[pl] < a[pv]:
                pl += 1
            while a[pr] > a[pv]:
                pr -= 1
            if pl <= pr:
                a[pl],a[pr] = a[pr],a[pl]
                pl += 1
                pr -= 1
        if left < pr: range.push((left,pr))
        if pl < right: range.push((pl,right))

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