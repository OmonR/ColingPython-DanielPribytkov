def solution(arr):
    largest = -1000
    ch = 0
    maximum_ch = 0
    for element in arr:
        if prev == element:
            curr_rep_len += 1
        else:
            prev = element
            max_rep_len = max(max_rep_len, curr_rep_len)
            curr_rep_len = 1

    return max_rep_len
