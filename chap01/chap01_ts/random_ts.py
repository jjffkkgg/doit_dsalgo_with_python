#%%
import random
#%%
n = int(input("난수 갯수"))

for i in range(n):
    r = random.randint(10,99)
    print(r, end=" ")
    if r == 13:
        print("중단")
        break