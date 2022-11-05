import random
class Class:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __shifr(self):
        n = random.randint(1,4)
        if n == 1:
            return self.a + self.b
        if n == 2:
            return self.a - self.b
        if n == 3:
            return self.a * self.b
        if n == 4:
            return self.a / self.b



    def get_shifr(self):
        print('your result is: ', self.__shifr())


s = Class(a=2, b=7)
s.get_shifr()