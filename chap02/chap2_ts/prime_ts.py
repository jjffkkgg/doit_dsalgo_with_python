#%%

counter = 0
prime = []
prime.append(2)

max = 1001

for i in range(3,max,2):
    for j in prime[1:]:
        counter += 1
        if i % j == 0:
            break
    else:
        prime.append(i)
#        elif i % j != 0 and j == prime[-1]:
#           prime.append(i)
print(f"1부터 {max}까지 소수: {prime}")
print(f"나눗셈 횟수: {counter}")