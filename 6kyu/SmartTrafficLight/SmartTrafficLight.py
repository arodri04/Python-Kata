class SmartTrafficLight:
    def __init__(self, st1, st2):
        
        self.st1 = st1
        self.st2 = st2

    def turngreen(self):
        if self.st1[0] == self.st2[0]:
            return None
        if self.st1[0] > self.st2[0]:
            self.st1[0] = 0
            return self.st1[1]
        else:
            self.st2[0] = 0
            return self.st2[1]