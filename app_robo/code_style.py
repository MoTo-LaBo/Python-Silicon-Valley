import os

y = 1
x = y

x = "aaaaaaaaaaa"  # 80文字が良いと言われている


d = {'key1': 'value1', 'key2': 'value2'}
if 'key1' in d:
    print('test')


ranking = {'key1': 'value1', 'key2': 'value2'}

for name, count in ranking.items():
    """
    kfjalkjf;la
    dkfja;sf
    kadfj;al
    kdafljf
    このように大量に記述されて分からなくなるので...
    変数は１行、２行であれば 1文字 or 2文字でも問題ない
    実際 App 開発は code 長くなるので使用しない
    変数は分かりやすい名前にする
    """
    print(name, count)

# ---------------- ジェネレーター使用する ------------------
"""
ジェネレーターを使用できる場合は使用する = 処理が早いから
メモリ上早く処理できるので、for文で同じ処理をするのであれば
ジェネレーターで code を記述する
"""

"""
def t():
    # num = []
    for i in range(10):
        yield i
        # num.append(i)
    # return num


for i in t():
    print(i)
"""

# ---------------- lambda(ラムダ) ------------------
"""
lambda を使用する時は下記のように関数を省略したい時など
"""


def other_func(f):
    print(f(10))


def test_func(x):
    return x * 2


lambda x: x * 2

other_func(test_func)
other_func(lambda x: x * 2)


# ------------ if文を list内包のように使用 --------------
"""
もし y の中に何か入っているようであれば、 x = 1 : 1 を使用する
"""
# y = None
y = 'kdfjsoij'
x = 1 if y else 2
print(x)


# ----------------- クロージャー -------------------
def base(x):
    def plus(y):
        return x + y
    return plus


plus = base(10)  # 1番最初に１０が入るが、計算されない。値だけ保持
print(plus(10))  # 最初の y=10, 次の x=10 で　２０が返される
print(plus(30))  # 上記と同じく 40が返される


"""
クロージャーを使用する場合は、global変数を扱うと誰かに書き換えられる
可能性がるので…
上記のように記述して使用する
"""

# i = 0


# def add_num():
#     def plus(y):
#         return i + y
#     return plus


# i = 10
# plus = add_num()
# print(plus(10))
# print(plus(30))
