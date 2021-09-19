# -------------- classの初期化とクラス変数 --------------

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


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')


class ToyotaCar(Car):
    def run(self):
        print('fast')


class TeslaCar(Car):
    def __init__(self, model='Model s',
                 enable_auto_run=False,
                 passwd='123'):
        # self.model = model
        super().__init__(model)  # 親の関数を呼び出す
        self._enable_auto_run = enable_auto_run
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
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)

"""
何か制限をさせたい時に、 (1)getter, (2)setter を使用する
"""
