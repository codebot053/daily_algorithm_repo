def solution(babbling):
    '''
    https://school.programmers.co.kr/learn/courses/30/lessons/120956
    옹알이(1)
    '''
    answer = 0

    available = ["aya", "ye", "woo", "ma"]
    for i in babbling: # 변수로 받은 옹알이 리스트에서 하나씩 꺼내 i 로 할당
        for j in available:
            if j + j in i: # 중복일때 루프 out
                break
            else:
                i = i.replace(j, " ")
        i = i.strip()
        if i: # i가 True 이면 pass False 이면 answer 1씩 증가
            continue
        else:
            answer += 1
    return answer

b = ["aya", "yee", "u", "maa", "wyeoo"]
print(solution(b))
