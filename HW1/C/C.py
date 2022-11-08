def solution(n, k):
    result = k//n
    remains = k%n
    return result, remains
