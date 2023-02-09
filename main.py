class Test:
    def __init__(self, a, b):
        self.name = a
        self.surname = b
        self.__pi = 3.14

    def output(self):
        print(f"{self.name} {self.surname} pi: {self.__pi}")

    def output2(self):
        print("GET OUT YE BLACK AND TANS")
        self.output()


niko = Test("Nikodem", "Majzner")
niko.output()
niko.output2()
niko.__pi=6
niko.output()

