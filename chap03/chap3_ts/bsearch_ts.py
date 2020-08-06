#%%
from typing import Any,Sequence
#%%
def bin_search_ts(lst: Sequence, key: Any) -> int:
    pl = 0
    pr = len(lst) - 1
    pc = (pl + pr) // 2
    while lst[pc] != key and pl != pr:
        pc = (pl + pr) // 2
        if key > lst[pc]:
            pl = pc + 1
        elif key < lst[pc]:
            pr = pc - 1
        else:
            return pc
    if lst[pc] == key:
        return pc
    else:
        return -1
#%%
if __name__ == "__main__":
    n = int(input("원소 수 입력: "))
    x = [None] * n
    print("배열 데이터 오름차순 입력")
    for i in range(n):
        x[i] = int(input(f"x[{i}]: "))

    f = int(input("찾는값: "))
    
    print(f"찾는값의 인덱스: {bin_search_ts(x,f)}")