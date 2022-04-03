from statistics import mode
from unittest import result


class Mode:
    
    def __init__(self):
        self.mode_dict = {}
        self.max_key = None
        self.max_val = 0

    def add(self, x):
        if x not in self.mode_dict:
            self.mode_dict[x] = 1
        if x in self.mode_dict:
            self.mode_dict[x] += 1

        if self.mode_dict[x] > self.max_val:
                self.max_val = self.mode_dict[x]
                self.max_key = x
        elif self.mode_dict[x] == self.max_val:
            if x < self.max_key:
                self.max_key = x
                
        return self.max_key
        
        

if __name__ == "__main__":
    m = Mode()
    print(m.add(1))
    print(m.add(2))
    print(m.add(3))