#%%
def factorial(n: int) -> int:
    if n == 0:
        return 1

    elif n > 0:
        fac = factorial(n - 1) * n
        n -= 1
    return fac

#%%
if __name__ == "__main__":
    n = int(input("팩토리얼 할 값: "))
    print(f"{n}! = {factorial(n)}")