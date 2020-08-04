#%%
from typing import Any, Sequence
import sys
#%%
def max_of_ts(a: Sequence) -> Any:
    maxi = a[0]
    for i in range(1, len(a)):
        if a[i]>maxi:
            maxi = a[i]
    return maxi

#%%
if __name__ == "__main__":
    print("배열의 최댓값")
    n = int(input("원소 갯수 설정"))

    x = [None]*n

    for j in range(n):
        x[j] = int(input(f"x[{j}] 값 입력:"))

    print(f"최댓값:{max_of_ts(x)}")