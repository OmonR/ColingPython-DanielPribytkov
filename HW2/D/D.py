def solution(n,k):
    k -= 1
    killing_number = k
    people= list(range(1,n+1))
    while len(people) > 1:
        if killing_number > n:
            killing_number = (k-n) % len(people)
        people.pop(killing_number)
        killing_number = (killing_number + k) % len(people)
    survive=people[0]
    return survive

