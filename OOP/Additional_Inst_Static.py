class FixedFloat:
    def __init__(self, amount):
        self.amount=amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"    # :.2f is used to print upto 2 decimal places

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1+value2)

new_number=FixedFloat.from_sum(20.364,32.946)
print(new_number)

class Dollar(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol='$'
    
    def __repr__(self):
        return f"<Dollar {self.symbol}{self.amount:.2f}>"
    
money= Dollar.from_sum(65.256,98.258)
print(money)