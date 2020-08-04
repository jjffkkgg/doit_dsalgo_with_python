#%%
def card_conv_ts(a,b) -> str:
    
    d = ""
    dchar = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while True:
        r = a % b
        a = a // b
        d += dchar[r]
        if a < b:
            d += dchar[a]
            break
    return d[::-1]
#%%
if __name__ == "__main__":
    print("10진수를 n진수로 변환.")
    while True:
        while True:
            x = int(input("음이 아닌 10진수 정수 입력:"))
            if x>0:
                break
        while True:
            n = int(input("변환할 진수 입력(2~36):"))
            if 2 <= n <= 36:
                break
        print(f"{n}진수로 변환: {card_conv_ts(x,n)}")

        retry = input("한번 더 시행할까요?(Y.....예/N.....아니오)")
        if retry in {"N","n"}:
            break
