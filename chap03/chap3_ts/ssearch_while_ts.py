#%%
from typing import Any,Sequence
#%%
def sqsearch(lst: Sequence, key: Any) -> int:
    j = 0
    while True:
        if j == len(lst):
            return -1
        if key == lst[j]:
            return j
        j += 1
    
#%%
if __name__ == "__main__":
    
    n = int(input("원소 수 입력: "))
    x = [None]*n
    for i in range(n):
        x[i] = int(input(f"x[{i}]: "))

    f = int(input("검색할 값 입력: "))

    print(f"검색값의 인덱스는 {sqsearch(x,f)}")
