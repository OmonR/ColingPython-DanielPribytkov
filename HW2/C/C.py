def solution(arr):
    snail_array = []
    while arr:
        snail_array.extend(list(arr.pop(0)))
        arr = list(zip(*arr))
        arr.reverse()
    return snail_array

