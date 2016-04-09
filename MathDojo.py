
class MathDojo(object):
    def __init__(self):
        self.sum = 0
        self.sub = 0

    def add(self, *rest):
        for arg in rest:
            if type(arg) == list:
                for k in arg:
                    self.sum = self.sum + k
            else:
                self.sum = self.sum + arg
        return self

    def subtract(self, *rest):
        for i in rest:
            if type(i) == list:
                for k in i:
                    self.sub = self.sub + k
            else:
                self.sub = self.sub + i
        return self

    def result(self):
        print self.sum - self.sub


MathDojo().add([1],3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).result()


