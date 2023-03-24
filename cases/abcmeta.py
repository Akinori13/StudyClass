from abc import ABCMeta, abstractmethod


class AbstractAnimal(metaclass=ABCMeta):
    """
    継承しなければ"インスタンス化"できないクラス
    継承せずとも、クラス変数、クラスメソッド、ステイティックメソッドは利用可能である。
    ただし、継承しない場合は、抽象クラスのクラス変数、クラスメソッドである。クラス変数の変更後に継承する場合、そのクラス変数の値は継承される。
    """

    IS_ANIMAL = True  # 継承せずともクラス変数は利用可能である
    EVOLUTION_LEVEL = 0

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        """
        プロパティ
        """
        return self.__name

    def say_name(self):
        """
        インスタンスメソッド
        """
        print(f"I am {self.__name}")

    @classmethod
    def set_evolution_level(cls, value):
        """
        クラスメソッド
        """
        print(f"This Animal Level was {cls.EVOLUTION_LEVEL}. Now, {value}")
        cls.EVOLUTION_LEVEL = value

    @staticmethod
    def say_groans():
        """
        ステイティックメソッド
        """
        print("hoooooo!!")

    @abstractmethod
    def introduce(self):
        """
        継承先で実装されなければならない、インスタンスメソッド
        """
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def say_animal_type_and_place(cls, place):
        """
        継承先で実装されなければならない、クラスメソッド
        """
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def say_hello():
        """
        継承先で実装されなければならない、クラスメソッド
        """
        raise NotImplementedError()


class Human(AbstractAnimal):
    ANIMAL_TYPE = "HumanType"

    def __init__(self, name, age):
        super().__init__(name)
        self.__age = age  # Humanクラスのみのインスタンス変数を定義

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if type(value) == int:
            self.__age = value
            return
        raise ValueError("年齢は0以上の整数を指定してください")

    def introduce(self):
        """
        インスタンスメソッド：クラス変数△、インスタンス変数〇
        「self.ANIMAL_TYPE」でクラス変数にアクセス可能。ただし可変にした場合に同名のインスタンス変数を定義するバグが発生するリスクがある。
        """
        print(f"I am {self.name}, {self.age} old.")

    @classmethod
    def say_animal_type_and_place(cls, place):
        """
        クラスメソッド：クラス変数〇、インスタンス変数×
        """
        print(f"Animal Type {cls.ANIMAL_TYPE} in {place}!!")

    @staticmethod
    def say_hello(world_name):
        """
        ステイティックメソッド：クラス変数×、インスタンス変数×
        """
        print(f"Hello, {world_name}!!")


if __name__ == "__main__":
    # インスタンス生成
    bob = Human("Bob", 20)

    # クラスプロパティ呼び出し
    print(Human.ANIMAL_TYPE)
    print(Human.IS_ANIMAL)

    # インスタンスプロパティ呼び出し
    print(bob.name)

    # インスタンスプロパティの更新
    bob.age = 12
    print(bob.age)

    # インスタンスメソッド実行
    bob.introduce()

    # クラスメソッド実行
    Human.set_evolution_level(12)

    # ステイティックメソッド実行
    Human.say_groans()

    print("====== 継承時実装必須 メソッド =====")

    # 継承時実装必須のインスタンスメソッド実行
    bob.say_name()

    # 継承時実装必須のクラスメソッド実行
    Human.say_animal_type_and_place("grassland")

    # 継承時実装必須のステイティックメソッド実行
    Human.say_hello("World1")
