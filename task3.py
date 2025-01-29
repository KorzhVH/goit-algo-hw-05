from kmp import kmp_search
from bms import boyer_moore_search
from rks import rabin_karp_search
import timeit

with open("text1.txt", "r", encoding="utf-8") as file:
    content1 = file.read()
with open("text2.txt", "r", encoding="utf-8") as file:
    content2 = file.read()

kmp_txt1 = timeit.timeit('kmp_search(content1, "Пошук")', globals=globals(), number=1000)
kmp_txt2 = timeit.timeit('kmp_search(content2, "Постановка")', globals=globals(), number=1000)
kmp_odd_word = timeit.timeit('kmp_search(content1, "qdkqdioq")', globals=globals(), number=1000)
bms_txt1 = timeit.timeit('boyer_moore_search(content1, "Пошук")', globals=globals(), number=1000)
bms_txt2 = timeit.timeit('boyer_moore_search(content2, "Постановка")', globals=globals(), number=1000)
bms_odd_word = timeit.timeit('boyer_moore_search(content1, "qdkqdioq")', globals=globals(), number=1000)
rbs_txt1 = timeit.timeit('rabin_karp_search(content1, "Пошук")',globals=globals(), number=1000)
rbs_txt2 = timeit.timeit('rabin_karp_search(content2, "Постановка")',globals=globals(), number=1000)
rbs_odd_word = timeit.timeit('rabin_karp_search(content1, "qdkqdioq")',globals=globals(), number=1000)


print(f"Knutt-Morris-Pratt' search time for text1: {kmp_txt1}, for text2: {kmp_txt2}, for nonexistent: {kmp_odd_word}")
print(f"Boer-Mur' search time for text1: {bms_txt1}, for text2: {bms_txt2}, for nonexistent: {bms_odd_word}")
print(f"Rabin-Karp' search time for text1: {rbs_txt1}, for text2: {rbs_txt2}, for nonexistent: {rbs_odd_word}")