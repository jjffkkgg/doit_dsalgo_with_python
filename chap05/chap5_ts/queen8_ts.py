
#class flag:
    
#    def __init__(self, i: int, j:int) -> None:
#        self.i = i
#        self.j = j

#    def flag_a(self, i:int, j:int) -> bool:
        

#%%
count = 0
pos = [0] * 8
flag_a = [False] * 8
flag_b = [False] * 15
flag_c = [False] * 15

#%%
def put() -> None:
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print(end = '\n')

#%%
def set(i: int) -> None:
    global count
    for j in range(8):
        if (not flag_a[j]) and (not flag_b[i+j]) and (not flag_c[i-j+7]):
            pos[i] = j
            if i == 7:
                count += 1
                put()
            else:
                flag_a[j] = True
                flag_b[i+j] = True
                flag_c[i-j+7] = True
                set(i+1)
                flag_a[j] = False
                flag_b[i+j] = False
                flag_c[i-j+7] = False
#%%
if __name__ == '__main__':
    set(0)
    print(f'solution 갯수: {count}')
