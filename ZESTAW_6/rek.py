

def is_prime(n) -> bool:
    if n < 2:
        return False
    if n in [2, 3]:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i == 0 or n %(i + 2) == 0:
            return False
        i += 6

    return True

def divide(number, result=0, cnt=0, i=1):
    if number == 0:
        if is_prime(result) and is_prime(cnt):
            print(result)
            print(cnt)
            return True
        else:
            return False

    return divide(number // 10, (number % 10) * i, cnt + 1, i * 10 ) or divide(number // 10, result, cnt + 1, i * 10 )

print(divide(122))