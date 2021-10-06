# 마라톤 참가는 했으나 완주하지 못한 선수 이름을 return 

def solution(participant, completion):
    answer = []
    part = sorted(participant)
    compl = sorted(completion)
    print(part, compl)
    while compl:
        if part[0] == compl[0]:
            compl.pop(0)
            part.pop(0)
        else:
            answer.append(part.pop(0))
    answer += part
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))