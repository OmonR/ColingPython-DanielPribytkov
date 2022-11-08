def solution(a, b):
    A = a
    B = b
    for a in A:
        for b in B:
            U = A + B
            if b in A:
                del b #не могу понять как удалить именно элементы которые повторяются в A
    return U
