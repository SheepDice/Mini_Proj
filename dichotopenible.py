import random

class Dichorelou():
    def __init__(self):
        self.tableau_1 = []
        self.tableau_2 = []
        for i in range(0, 50):
            self.tableau_1.append(random.randint(0, 10))
        self.tableau_1.sort()
        self.whattofind = -1

    def defWhattofind(self):
        self.whattofind = int(input("Dicotocombien ? (< 10 000"))

    def dichofind(self):
        while(True):
            print("\n")
            self.tableau_2 = self.tableau_1[:int(len(self.tableau_1)/2)]
            self.tableau_1 = self.tableau_1[int(len(self.tableau_1)/2):]
            print(self.tableau_2)
            print(self.tableau_1)

            if self.whattofind <= self.tableau_2[-1]:
                self.tableau_1 = self.tableau_2
            if len(self.tableau_1) == 1:
                print(self.tableau_1[0])
                break


    def exec(self):
        self.defWhattofind()
        self.dichofind()

