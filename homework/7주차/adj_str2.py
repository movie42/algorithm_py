# 풀어보기 

# 문제의 요구사항은 단어들을 인접한 그래프로 표현해서 탐색할 수 있는지를 보는 것이다.

# 1. 일단 단어를 그래프로 만든다. 단어를 노드라고 생각하면 인접한 노드들을 연결해야한다. 
# 2. 노드들끼리 인접한 조건은 단어 안에 포함된 글자 하나가 같으면 인접 노드다. 
# 3. 만약 각 단어의 글자가 2글자 이상 같으면 인접노드로 보지 않는다.
# 주어진 단어 리스트를 그래프로 먼저 만들어야한다.
# 그래프를 만들고나면 주어진 글자가 그래프 탐색의 시작점이 된다. 그럼 그 다음 인접노드인지를 확인한다. 
# 인접 노드를 리스트에 넣고 큐에서 시작 노드부터 찾고자하는 단어까지 몇번 탐색했는지 숫자를 센다.
# 나머지는 dijkstra?알고리즘 과정을 거치면 된다.

def isAdj(s1, s2):
    count = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            count += 1
        if count > 1:
            return False
    return count == 1

def solition(beginWord, endWord, wordList):
    adjWordList = {x: list(filter(lambda xx: isAdj(x, xx), wordList)) for x in wordList}
    adjList = list(filter(lambda x: isAdj(beginWord, x), wordList))
    queue = list(map(lambda x: (1, x), adjList))

    visited = set()
    while queue:
        count, word = queue.pop() 
        if word == endWord:
            return count + 1
        if word not in visited:
            visited.add(word)
            queue = list(map(lambda x: (count+1, x), adjWordList[word])) + queue
    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solition(beginWord, endWord, wordList))
