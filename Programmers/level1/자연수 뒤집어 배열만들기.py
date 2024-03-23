def solution(n):
    answer = []
    tostr = str(n)
    for i in range(1,len(tostr)+1):
        answer.append(int(tostr[len(tostr)-i]))
    return answer