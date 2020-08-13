#%%
from typing import MutableSequence

#%%
def merge_sort(a: MutableSequence) -> None:

    def _merge_sort(a: MutableSequence,left: int, right: int) -> None:
        if left < right:
            center = (left + right) // 2

            _merge_sort(a,left,center)
            _merge_sort(a,center + 1,right)
            
            buff_index,pl = 0,0
            merge_index,pr = left, left
            while pr <= center:
                buff[buff_index] = a[pr]
                buff_index += 1
                pr += 1

            while (pl < buff_index) and (pr <= right):
                if buff[pl] <= a[pr]:
                    a[merge_index] = buff[pl]
                    pl += 1
                else:
                    a[merge_index] = a[pr]
                    pr += 1
                merge_index += 1

            while pl < buff_index:
                a[merge_index] = buff[pl]
                pl += 1
                merge_index += 1

    n = len(a)
    buff = [None] * n
    _merge_sort(a, 0, n - 1)
    del buff

#%%
if __name__ == "__main__":
    lst = [5,8,4,2,6,1,3,9,7]
    print(f'원본: {lst}')
    merge_sort(lst)
    print(f'결과: {lst}')