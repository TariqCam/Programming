### Credit card validation

class CreditCard(object):
    def __init__(self, num) -> None:
        self.unvalid = num
        self.num = self.normalise() if self.valid() else None
    
    def normalise(self):
        num = self.unvalid.replace("-", "")
        return int(num)

    def valid(self ):
        if "_" in self.unvalid or " " in self.unvalid:
            return False
        return True

    def validate(self) -> bool:
        pass

if __name__ == "__main__":
    cc = CreditCard("5122-2368-7954-3214")
    print(cc.num)