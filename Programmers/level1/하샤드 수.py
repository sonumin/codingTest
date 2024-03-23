def solution(x):
    answer = True
    sum = 0
    tostr= str(x)
    for i in tostr:
        sum+= int(i)
    if(x%sum!=0):
        return False
    return answer