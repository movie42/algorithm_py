# 마라톤 참가는 했으나 완주하지 못한 선수 이름을 return
# 해쉬테이블 문제라고한다. 나의 풀이는 O(nlogn)
# def solution(participant, completion):
#     answer = []
#     part = sorted(participant)
#     compl = sorted(completion)
#     print(part, compl)
#     while compl:
#         if part[0] == compl[0]:
#             compl.pop(0)
#             part.pop(0)
#         else:
#             answer.append(part.pop(0))
#     answer += part
#     return answer

# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]
# print(solution(participant, completion))

# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]
# print(solution(participant, completion))

# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]
# print(solution(participant, completion))

# 다시풀어보기


def maraton(participant, completion):
    dict = {}

    for x in participant:
        dict[x] = dict.get(x, 0)+1

    for x in completion:
        dict[x] -= 1

    com_list = [human for human, complete in dict.items() if complete > 0]
    return com_list


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(maraton(participant, completion))

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(maraton(participant, completion))

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(maraton(participant, completion))
