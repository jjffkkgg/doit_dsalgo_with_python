#%%
def move_ts(no:int, x:int, y:int) -> None:
    if no > 1:
        move_ts(no - 1, x, 6 - x - y)

    print(f'원반 [{no}]를 {x} 기둥에서 {y} 기둥으로 옮깁니다.')

    if no > 1:
        move_ts(no - 1, 6 - x - y, y)
#%%
if __name__ == "__main__":

    n = int(input('하노이탑을 실행할 원반 갯수: '))
    move_ts(n,1,3)
