def solution(a, b):
    new_b = [value for value in b if value not in a]
    new_list = a + new_b
    for i in range(0, len(new_list)-1, 1):
        for j in range(0, len(new_list)-1-i, 1):
            if new_list[j] > new_list[j+1]:
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
    return new_list
