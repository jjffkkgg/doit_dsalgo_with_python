#%%
def gcd(x: int, y: int) -> int:
	if y == 0:
		return x
	else:
		return gcd(y, x % y)
#%%
if __name__ == '__main__':
	print("최대공약수 출력")
	x = int(input('1번째 정수'))
	y = int(input('2번째 정수'))

	print(f"최대공약수:{gcd(x,y)}")