def check(n):
    listificate = map(int, str(n))
    list_sum = sum(listificate)
    if list_sum % 7 == 0:
        return True
    return False

if __name__ == "__main__":
    print(check(14)) # False
    print(check(16)) # True
    print(check(123)) # False
    print(check(777)) # True
    print(check(9999999)) # True