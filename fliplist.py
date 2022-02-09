from collections import deque


class FlipList:
    def __init__(self):
        self.lista = deque()
        self.indicator = False

    def push_last(self,x):
        if self.indicator:
            self.lista.appendleft(x)
        else: self.lista.append(x)

    def push_first(self,x):
        if self.indicator:
            self.lista.append(x)
        else:self.lista.appendleft(x)

    def pop_last(self):
        if self.indicator:
            return self.lista.popleft()
        else:   
            return self.lista.pop()

    def pop_first(self):
        if self.indicator:
            return self.lista.pop()
        else:
            return self.lista.popleft()

    def flip(self):
        if self.indicator:
            self.indicator = False
        else:
            self.indicator = True

if __name__ == "__main__":
    f = FlipList()
    f.push_last(1)
    f.push_last(5)
    f.push_last(3)
    f.flip()
    print(f.pop_last())
    print(f.pop_last())
    print(f.pop_last())