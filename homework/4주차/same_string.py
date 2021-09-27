def solution(a):
    max_str = 0
    count = 0
    for item in range(1, len(a)):
        for str_idx in range(len(a[0])):
            if a[0][str_idx] != a[item][str_idx]:
                break
            else:
                count += 1
        if item == 1:
            max_str = count
        if max_str > count:
            max_str = count
    return max_str


# Test code
print(solution(['abcd', 'abce', 'abchg', 'abcfwqw', 'abcdfg']))  # 3
print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg']))  # 0
