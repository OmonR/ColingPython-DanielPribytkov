def solution(total):
    hours = total % (60 * 24) // 60
    minutes = total % 60
    x = [hours, minutes]
    return  (" ".join(map(str, x)))
