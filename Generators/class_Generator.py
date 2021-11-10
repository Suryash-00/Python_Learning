class Prime_Generator:
    def __init__(self, stop):
        self.stop=stop
        self.start=2
    def __next__(self):
        for n in range(self.start, self.stop):
            for x in range(2, n):
                if n%x==0:
                    break
            else:
                self.start=n+1
                return n

        raise StopIteration()