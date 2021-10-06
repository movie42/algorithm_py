def solution(words, queries):
    answer = []
    for quer in queries:
        count = 0
        for word in words:
            if len(quer) == len(word):
                isTrue = True
                for i in range(len(quer)):
                    if quer[i] == "?":
                        continue
                    if quer[i] != word[i]:
                        isTrue = False
                        break
                if isTrue:
                    count += 1
        answer.append(count)
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
