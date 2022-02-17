class Mode:
    
    def __init__(self):
        self.mode_dict = {}

    def add(self, x):
        if x not in self.mode_dict:
            self.mode_dict[x] = 1
        elif x in self.mode_dict:
            self.mode_dict[x] += 1
    
        for key in self.mode_dict:
            if self.mode_dict[x] > self.mode_dict[key]:
                return x
            elif self.mode_dict[x] == self.mode_dict[key] and key < x:
                return key
        return x
       

if __name__ == "__main__":
    m = Mode()
    print(m.add(3)) # 1
    print(m.add(2)) # 1
    print(m.add(1)) # 2
