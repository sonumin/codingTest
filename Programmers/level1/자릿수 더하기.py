def solution(n):
    answer = 0
    tostr= str(n)
    for i in tostr:
        answer+=int(i)
    return answer