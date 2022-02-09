from collections import deque


def count(s):
    pino = deque()
    pino.append(s[0])
    i = 1
    j = 0
    while i < len(s):
        if not pino:
            pino.append(s[i]) 
            i += 1
            j = 0
            continue
        if s[i] != pino[j] and s[i] == ")": 
            pino.pop()
            j-=1
        else: 
            pino.append(s[i])
            j+=1
        i += 1
        
    return len(pino)



if __name__ == "__main__":
    print(count("(()())")) # 0
    print(count(")))))")) # 5
    print(count("((())(")) # 2
    print(count("(()()())()()")) # 0
    print(count("))))))((((((")) # 12