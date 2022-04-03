def func(x):
    if x == 0: return 1
    if x < 0: return 0 
    value = func(x-1) + func(x-2) + 1
    return value

if __name__ == "__main__":
    print(func(3))
    22
    27
    32