def solution(n):
    powers = []
    number = 1
    while number <= n:
        powers.append(number)
        number*=2  
    return powers
