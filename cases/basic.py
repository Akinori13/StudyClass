class Alphabet:
    def __init__(self, name):
        self.name = name

    def explain(self):
        print(self.name)


class A(Alphabet):
    def __init__(self, name, japanese):
        super().__init__(name)
        self.__japanese = japanese

    def echo_english_and_japanese(self):
        print(self.name + self.__japanese)


if __name__ == "__main__":
    alphabet = Alphabet("alphabet")
    alphabet.explain()  # alphabet

    a = A("A", "エー")
    a.explain()  # A
    a.echo_english_and_japanese()  # Aエー
