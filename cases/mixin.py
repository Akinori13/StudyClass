from typing import Protocol


class AnimalProtocol(Protocol):
    @property
    def name(self) -> str:
        ...

    def super_dash(self) -> None:
        ...

    def heal_self(self) -> None:
        ...


class AbstractAnimal:
    """
    ベースになる動物クラス
    """

    def __init__(self, name):
        self.name = name

    def dash(self):
        print(self.name + "がダッシュした!")


class SuperAnimalMixin:
    """
    スーパーなアニマル機能を提供するミックスイン
    """

    def super_dash(self: AnimalProtocol):
        print(self.name + "が100km/時速でダッシュ!")

    def heal_self(self: AnimalProtocol):
        print(self.name + "が自信を回復した!")


class Human(AbstractAnimal):
    """
    人クラス
    """

    def introduce(self):
        print(self.name + "が自己紹介した!")


class Dragon(AbstractAnimal, SuperAnimalMixin):
    """
    竜クラス
    """

    def fly(self):
        print(self.name + "が空を飛んだ!")


if __name__ == "__main__":
    me = Human("me")
    me.dash()
    me.introduce()

    dragon1 = Dragon("dragon1")
    dragon1.dash()
    dragon1.super_dash()
    dragon1.fly()
