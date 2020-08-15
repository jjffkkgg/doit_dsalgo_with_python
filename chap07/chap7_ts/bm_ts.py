#%%
def bm_match(txt:str, pat:str) -> int:
    skip = [None] * 256

    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1      # 중복되지 않는 C는?

    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp else len(pat) - pp  # 표만큼 넘어가는데, 그조건이...?

    return -1

if __name__ == "__main__":
    s1 = input('텍스트: ')
    s2 = input('패턴: ')

    idx = bm_match(s1,s2)

    if idx == -1:
        print('검색 결과가 없음')
    else:
        print(f'{(idx + 1)} 번째 문자 일치')
