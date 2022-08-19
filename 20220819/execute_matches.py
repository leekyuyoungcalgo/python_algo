# 검색알고리즘  사용
import bm_match as bm
from bm_match import bm_match
from kmp_match import kmp_match
from bf_match import bf_match

txt = 'ABCXDEZCABACABAC'
pat = 'ABAC'

# 1 bf_match
# 3 kmp_match
# 4 bm_match

print(f"bf_match(txt,pat) ={bf_match(txt,pat)}")
print(f"kmp_match(txt,pat) ={kmp_match(txt,pat)}")
print(f"bm_match(txt,pat) ={bm_match(txt,pat)}")