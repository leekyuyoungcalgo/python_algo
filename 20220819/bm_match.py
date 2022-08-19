def bm_match(txt:str, pat:str)->int:
    skip = [None] * 256 # skip table 해당문자열의 ascii 코드값을 index로 사용하기위해 'a'  97
    # 건너뛰기표
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    #검색
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) else len(pat) - pp
    return -1

if __name__ == "__main__":
    txt = 'ABCXDEZCABACABAC'
    pat = 'ABAC'
    idx = bm_match(txt,pat)
    print(f"idx = {idx}")
