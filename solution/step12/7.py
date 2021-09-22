# 백준 온라인 저지 단계별 문제풀이 12단계 정렬
# https://www.acmicpc.net/step/9
# 1181
# https://www.acmicpc.net/problem/1181

from operator import itemgetter

N = int(input())
words = []

for i in range(N):
    word = input()
    words.append((word, len(word)))

set_words = set(words)
sorted_words = sorted(set_words, key=itemgetter(1, 0))

for i in sorted_words:
    print(i[0])

