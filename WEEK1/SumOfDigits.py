def solution(n):
    answer = 0
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    answer = total
    return answer