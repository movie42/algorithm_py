# 문자열을 뒤에서부터 읽어도 원래 문자열과 같은 단어를 팰린드롬이라 한다.
# 입력으로 주어진 문자열이 팰린드롬인지 판별한 뒤, 팰린드롬이면 빈 문자열을 출력한다.
# 입력된 문자열이 팰린드롬이 아닐 경우 문자열을 반으로 나누어 앞 부분의 
# 단어를 기준으로 팰린드롬 단어로 만드는 함수를 작성하시오.


def solution(s):
    str_list = list(s)
    reverse_list = list(reversed(str_list))
    if "".join(str_list) != "".join(reverse_list):
        mid = len(str_list) // 2
        answer = ''
        for i in range(0, mid):
            answer += str_list[i]
        for i in range(mid - 1 , -1, -1):
            answer += str_list[i]
        return answer
    return ''


print(solution('abcdcba'))
print(solution('bannana'))
print(solution('wabe'))