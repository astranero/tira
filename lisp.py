from collections import deque
from unittest import result


def eval(s):
    value = 0
    j=0
    pino = deque([])
    if s[1] == "+":
        sum(s, pino, 2)
        j = pino.pop()
        value += pino.pop()

    if s[1] == "*":
        value += 1
        mul(s, pino, 2)
        j = pino.pop()
        value *= pino.pop()
    return value

def sum(s, pino, i):
    num = "1234567890"
    result = 0
    j = i
    
    int_result = ""
    while j < len(s):
        if s[j] == ")":
            if int_result != "":
                result += int(int_result)
            pino.append(result)
            pino.append(j)
            return
        
        if (s[j]) == "*": 
            mul(s,pino, j+1)
            j = pino.pop()
            result += pino.pop()

        elif s[j] == "+":
            sum(s, pino, j+1) 
            j = pino.pop()
            result += pino.pop()
        
        elif s[j] == " " and int_result != "":
            result += int(int_result)
            int_result = ""

        elif s[j] in num:
            int_result += s[j]
        j+=1
       
def mul(s, pino, i):
    num = "1234567890"
    result = 1
    j = i

    int_result = ""
    while j < len(s): 
        if s[j] == ")":
            if int_result != "":
                result *= int(int_result)
            pino.append(result)
            pino.append(j)
            return

        if s[j] == "+":
            sum(s,pino,j+1) 
            j = pino.pop()
            result *= pino.pop()

        elif s[j] == "*":
            mul(s,pino, j+1)
            j = pino.pop()
            result *= pino.pop()
        
        elif s[j] == " " and int_result != "":
            result *= int(int_result)
            int_result = ""
            
        elif s[j] in num:
            int_result += s[j]
        j +=1

if __name__ == "__main__":
    print(eval("(* (+ (+ 1 2) 3) (+ (* 4 5) 6 2))"))
    print(eval("(+ 123 456)")) # 579