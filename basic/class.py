# -------------- classの初期化とクラス変数 --------------
"""
class Person(object):
    def __init__(self, name):   # コンストラクター
        self.name = name
        # print(self.name)

    def say_something(self):
        print(f'I am {self.name}. hello')
        self.run(10)

    def run(self, num):
        print('run' * num)

    def __del__(self):   # デストラクタ
        print('good bye')


person = Person('Mike')
person.say_something()

del person  # 明示的に呼び出す場合

print('#########')
"""

# コンストラクタ / デストラクタ
"""
object を作成する時に一番初めに呼ばれるもの
object を最後に破壊・無くすモノ
"""

# -------------- class の継承 --------------
""""
base となる機能を一番最初の classに入れて
その後の class は baseの機能を継承して + 補完機能をつけ加える形にする
そうする事によって code とても綺麗にスッキリする
継承しないと、同じ code を何度も記述する事になる
"""


"""
class Person(object):  # --------- ダックタイピング(object指向の class の使い方) ----------
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError


baby = Baby()
adult = Adult()


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()


car = Car()
car.ride(adult)
"""

# ------------------------------ 抽象 class ------------------------------

"""
import abc  # あまり抽象 class 作らない方が良い
class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractclassmethod  # drive という関数を継承する class で必ず実行
    def drive(self):
        pass


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No drive')


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('ok')


baby = Baby()
# baby.drive()
adult = Adult()
adult.drive()


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()


class ToyotaCar(Car):
    def run(self):
        print('fast')


class TeslaCar(Car):
    def __init__(self, model='Model s',
                 enable_auto_run=False,
                 passwd='123'):
        # self.model = model
        super().__init__(model)  # 親の関数を呼び出す
        self.__enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property  # 　(1)読み込む事はできるが書き換える事はできない
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter  # (2)prooerty名 + setter を使うことで書き換えることができる
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable

    def run(self):
        print(self.__enable_auto_run)
        print('super fast')

    def auto_run(self):
        print('auto run')


tesla_car = TeslaCar('Model s')
"""
# tesla_car.enable_auto_run = True
# tesla_car.__enable_auto_run = 'XXXXXXXXXXX'
# print(tesla_car.__enable_auto_run)

"""
何か制限をさせたい時に、 (1)getter, (2)setter を使用する
"""


class T(object):
    pass


t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)

"""
上記のように関数を定義した後に書き換える事もできる
便利であるが bug にも繋がる可能性があるので function の中身を確認して使用する
"""


# ------------------------------ 多重 class ------------------------------
"""
class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('person run')


class Car(object):
    def run(self):
        print('car run')


class PersonCarRobot(Car, Person):  # ここが point 左が優先される！！
    def fly(self):
        print('fly')


person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()
"""
"""
多重継承もあまり使用しなほうが良い。 Car, Person 順番を知らないで
run( ) を使用してしまった時に bug に繋がる
"""
# ------------------------------ class 変数 ------------------------------

"""
class Person(object):

    kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)


a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()


class T(object):

    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)


c = T()
c.add_word('add 1')
c.add_word('add 2')
print(c.words)

d = T()
d.add_word('add 3')
d.add_word('add 4')
print(d.words)
"""

"""
class変数は, 全ての class object で共有されるという認識で使用する事
"""

# -------------------- class method/ static method --------------------


class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(year):
        print(f'about human : {year}')


a = Person()
print(a.x)
print(a.what_is_your_kind())

b = Person   # パレンティス ( ) : をつけてないので object を生成していない
# print(b.x)
print(b.kind)

Person.kind
print(Person.what_is_your_kind())

# Person.about()
Person.about(1990)

"""
object を生成していなくても、上記のような @classmethod で class変数や method を
使用・Access する事ができる
"""


# -------------------- 特殊 method --------------------
"""
__ (アンダースコア)が２つ前後についているものが特殊 method
"""


class Word(object):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Word!!!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()


w = Word('test')
w2 = Word('test')

print(id(w))
print(id(w2))

print(w == w2)
