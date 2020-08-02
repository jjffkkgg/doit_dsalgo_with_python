#%%
n = int(input("별의 갯수"))
w = int(input("몇개마다 줄바꿈"))

q = n // w
r = n % w

#%%
for _ in range(q):
#	for _ in range(w):
#		print("*", end="")
#	print(end="\n")
	print("*" * w)
#for _ in range(r):
#	print("*")
print("*" * r)