# 부르트 포스법 brute force method
def bf_match(txt:str, pat:str)->int:
    pt = 0  # 텍스트를 이동하는 인덱스
    pp = 0  # 패턴을 이동하는 인덱스

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0

    return pt-pp if pp == len(pat) else -1

s1 = 'ABABCDEFGHA'
s2 = 'ABC'
idx = bf_match(s1,s2)
print(idx)
