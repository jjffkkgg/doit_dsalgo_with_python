#%%

counter = 0
prime = []
prime.append(2)
prime.append(3)

max = 1001
j = 0

for i in range(5,max,2):
    while (i ** 0.5) >= prime[j]:
        counter += 2
        j += 1
        if i % prime[j] == 0:
            break
    else:
        prime.append(i)
        j = 0
#        elif i % j != 0 and j == prime[-1]:
#           prime.append(i)
print(f"1부터 {max}까지 소수: {prime}")
print(f"나눗셈 횟수: {counter}")