# 이것도 그래프라고 한다. 큰일이다. 그래프에게 스윕당하고 있다....
# 예시 답안

def isAdj(s1, s2):
    count = 0
    for c1, c2 in zip(s1, s2):
        print(c1, c2)
        if c1 != c2:
            count += 1
        if count > 1:
            return False
    return count == 1

def solution(beginWord, endWord, wordList):
    adjMap = {w: list(filter(lambda ww: isAdj(w, ww), wordList)) for w in wordList}
    
    adjList = list(filter(lambda w: isAdj(beginWord, w), wordList))
    visited = set()
    queue = list(map(lambda x: (1, x), adjList))

    while len(queue) > 0:
        count, word = queue.pop()

        if word == endWord:
            return count + 1

        if word not in visited:
            visited.add(word)
            queue = list(map(lambda x: (count + 1, x), adjMap[word])) + queue
    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(beginWord, endWord, wordList))

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
print(solution(beginWord, endWord, wordList))
