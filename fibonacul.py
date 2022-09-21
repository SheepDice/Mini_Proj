class Fibonacul():
    def __init__(self):
        self.fibonumber = 0
        self.fibonautrenumber = 1
        self.fibonamax = 0
        self.fibonalog = ""

    def fibonarmistice(self):
        self.fibonamax = int(input("Jusqu'à fibona-où ?"))

    def fibonalcul(self):
        self.fibonalog += str(self.fibonumber) + " "
        if self.fibonautrenumber > self.fibonamax:
            return
        temp = self.fibonautrenumber
        self.fibonautrenumber += self.fibonumber
        self.fibonumber = temp
        self.fibonalcul()

    def fibonerateur(self):
        self.fibonarmistice()
        self.fibonalcul()
        print(self.fibonumber)
        print(self.fibonalog)
