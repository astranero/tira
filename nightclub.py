from collections import deque

class NightQueue:
    def __init__(self):
        self.new_queue = {}
        self.avain = 0
        self.toinen_avain = 0

    def lisääjonoon(self):
        self.new_queue[self.avain] = 0
        self.avain += 1

    def veloita(self, x):
        for key in self.new_queue:
            self.new_queue[key] += x

    def paastaSisaan(self):
        r = self.new_queue[self.toinen_avain]
        del self.new_queue[self.toinen_avain]
        self.avain += 1
        return r 

if __name__ == "__main__":
    jono = NightQueue()
    jono.lisääjonoon()
    jono.lisääjonoon()
    jono.lisääjonoon()
    jono.lisääjonoon()
    jono.veloita(10)
    jono.veloita(5)
    jono.lisääjonoon()
    jono.lisääjonoon()
    jono.veloita(12)
    print(jono.paastaSisaan())
    