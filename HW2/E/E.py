import sys

sys.setrecursionlimit(1200)


def solution(a, b):
    if a == 0:
        return b
    return solution(a-1, b+1)
