class Dog:
    #コンストラクタ
    def __init__(self):
        self.name = "ポチ"
        self.__genki = 3

    @property
    def genki(self):
        return self.__genki

    def bark(self):
        return "ワン"

if __name__ == "__main__":
    pochi = Dog()
    print(pochi.name)
    print(pochi.genki)
    print(pochi.bark())
