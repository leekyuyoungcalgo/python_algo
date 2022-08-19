def kmp_match(txt:str, pat:str)->int:
    pt = 1
    pp = 0
    skip = [0]*(len(pat) + 1)

    # skip table
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1; pp += 1 ; skip[pt] == pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]
    print(f"skip table : {skip}")

    # 검색
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt +=1; pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]
    return pt-pp if pp == len(pat)  else -1

if __name__=="__main__":
    txt = 'ABCABABFD'
    pat = 'ABF'
    idx = kmp_match(txt, pat)
    print(f"index = {idx}")
