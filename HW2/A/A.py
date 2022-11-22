def solution(arr):
    largest = -10
    ch = 0
    maximus_ch = 0
    for i in arr:
        if largest == i:
            ch += 1
        else:
            largest = i
            maximus_ch = max(ch, maximus_ch)
            ch = 1
    maximus_ch = max(ch, maximus_ch)

    return maximus_ch
