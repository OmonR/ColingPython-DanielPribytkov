def solution(x):
    s = x.replace('h', 'H', x.count('h') - 1)
    s = s.replace('H', 'h', 1)
    text_list = s.split()
    for elements in text_list:  #мб можно заменить map
        if len(elements) == 3:
            text_list.remove(elements)
    text = " ".join(text_list)
    s = text.replace('1', 'one')

    return s

