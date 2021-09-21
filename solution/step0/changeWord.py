# 과제
# 2개의 단어 beginWord와 endWord,
# 그리고 여러개의 단어 wordList가 주어졌을 때,
# beginWord에서 endWord로 변환하기 위해 필요한 가장 적은 변환 횟수를 구하시오.


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]


def solution(begin, end, word_list):
    count = 0
    splitBeginWord = list(begin)
    splitWordList = [list(x) for x in word_list]

    if end not in word_list:
        return 0

    for idx, i in enumerate(splitWordList):
        for idx, j in enumerate(splitBeginWord):
            if i != j:
                break

    return count


print(solution(beginWord, endWord, wordList))
