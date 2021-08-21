# ------------ while文 ------------
# count = 0

# while count < 5:
#     print(count)
#     count += 1

"""
count を記述し忘れた場合は無限ループになってしまう
count が　0 で何も足されないので永遠に 5 より大きくなる事はない
"""

# break を使用した場合
# count = 0

# while True:
#     if count >= 5:
#         break

#     if count == 2:
#         count += 1
#         continue

#     print(count)
#     count += 1

"""
continue の場合は break の様に program から抜けるのではなく
スキップをさせる = print が出力されない
2 が表示されない
"""

# while else
# count = 0

# while count < 5:
#     print(count)
#     count += 1
# else:
#     print('done')

"""
else　は break で抜けなければ else にいく(実行される)
break の場合は実行している program から抜けるので以下の
program は実行されなくなる
"""


# ----- input(関数): while文とよく使用される -----
# while True:
#     word = input('Enter:')
#     if word == 'ok':
#         break
#     print('next')


"""
上記の場合は string型(文字列)
input は console 上で何か入力されたら次の program が実行される
input = ('Enter') console 上で表示されて文字
loop を終了するには、返り値のを指定しなければならない
指定した値でなければ、エンドレスで loop し続ける
"""

# input の word を型変換する : intger(整数)に対応できる
# while True:
#     word = input('Enter')
#     num = int(word)
#     if num == 100:
#         break
#     print('next')


# ------------ for文・break文------------
some_list = [1, 2, 3, 4, 5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1
""""
for文の場合
while文を使用してわざわざ上記の様な記述をしなくて良い
"""
# 反復処理をする物 : iterator(イテレーター)

# for i in some_list:
#     print(i)

# for s in 'abcde':
#     print(s)

# for word in ['My', 'name', 'is', 'MoTo']:
#     if word == "name":
#         break
#     print(word)

# for word in ['My', 'name', 'is', 'MoTo']:
#     if word == "name":
#         continue
#     print(word)


# ----- for else文 -----
# for fruit in ['apple', 'banana', 'orange']:
#     if fruit == 'banana':
#         print(
#             'stop eating'
#         )
#         break
#     print(fruit)
# else:
#     print('I ate all')


# ----- range 関数 -----
# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in num_list:
#     print(i)

"""
上記の様な記述は非常に手間がかかる
range 関数を使用すればわざわざ自分自身で list を作る必要がない
"""

# for i in range(10):
#     print(i)

# index 2 から始めたい場合
# for i in range(2, 10):
#     print(i)

# 3個飛ばしで表示したい場合
# for i in range(2, 10, 3):
#     print(i)

# for i in range(10):
#     print(i, 'hello')

"""
App 開発で後々 i(index)は不要になる場合は
下記のようにアンダースコア代入する
そうすることによって明示的にこの program では
ind(index)は使う必要がないとわかる
"""
# for _ in range(10):
#     print('hello')


# ----- enumerate 関数 -----
# i = 0
# for fruit in ['apple', 'banana', 'orange']:
#     print(i, fruit)
#     i += 1

"""
enumerate 関数を使用すればもっと簡単に index を取得できる
"""

# for i, fruit in enumerate(['apple', 'banana', 'orange']):
#     print(i, fruit)


# ----- zip 関数 -----
# days = ['Mon', 'Tue', 'Wed']
# fruits = ['apple', 'banana', 'orange']
# drinks = ['coffee', 'tea', 'beer']

# 同時に出力したい場合
# for i in range(len(days)):
#     print(days[i], fruits[i], drinks[i])

"""
上記の記述の仕方だと、code が解読しづらい
あまり良い coding とは言えない
"""

# for day, fruit, drink in zip(days, fruits, drinks):
#     print(day, fruit, drink)

"""
index を使用しないでも複数を出力できる
code の見た目もわかりやすい
"""

# ----- dictionary を for文で処理 -----
# d = {'x': 100, 'y': 200}

# for v in d:
#     print(v)

# key と value を両方出力したい場合
# print(d.items())
# for k, v in d.items():
#     print(k, ':', v)

"""
dictionary の loop も非常に多く使用される
dict_items([('x', 100), ('y', 200)])
dictionary の中に tuple型で unpacking されている
"""

# tuple unpacking
# num_tuple = (10, 20)
# print(num_tuple)
# # (10, 20)
# s
# x, y = num_tuple
# print(x, y)
# 10 20


# ---------- function 関数定義 ----------
# def say_something():
#     print("Hi")

# print(type(say_something))
# f = say_something
# f()


# 返り値 : result
# def say_something():
#     s = 'hi'
#     return s


# result = say_something()
# print(result)

# params (引数)
# def what_is_this(color):
#     print(color)


# what_is_this('red')

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"


result = what_is_this('red')
# result = what_is_this('green')
# result = what_is_this('yellow')
print(result)

"""
if文など何度も呼び出したい場合に、function(関数)定義してあげる
color を何度も code で記述しなくてもよくなる
基本的に何度も呼び出す code は function に入れて呼び出していく
"""

# ----- function の補足 -----
"""
下記の様に型宣言はできるが、引数をstring(文字列)にしても
実行はできてしまう。
program を書く人はわかるが、python は error として出力しない
ので注意する
"""


def add_num(a: int, b: int) -> int:
    return a + b


result = add_num('a', 'b')
print(result)


# ----- function の引数 -----
def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)


menu(entree='beef', drink='beer', dessert='ice')

"""
引数の順番が重要
間違いを無くしたい場合は、keyword augment を使用する
そうすると順不同でも間違いなく出力される
"""


# ----- default 引数 -----


def menu(entree='beef', drink='beer', dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)


# menu()
menu(entree='chiken')
"""
引数を与えなかった場合は default 引数が代入される
引数を与えた場合は、上書きされる
"""

# ----- default 引数の注意事項 -----


# def test_func(x, l=[]):
#     l.append(x)
#     return l


# y = [1, 2, 3]
# result = test_func(100, y)
# print(result)

# y = [1, 2, 3]
# result = test_func(200, y)
# print(result)

# r = test_func(100)
# print(r)

# r = test_func(100)
# print(r)
"""
上記の記述の仕方は Bug につながるので、pythonでは
list [] は default 引数に与えるべきではないと
暗黙の了解がある。
list は参照渡しだから、一番最初に実行したメモリを2回目も見にいくので
2回目の引数に list の値を入れなくても、一番最初で list を生成(保存)
しているから、それに追加する形で data が上書き・反映される
dictionary も参照渡しなので注意する。 default 引数では使用しない
"""

# 上記の解決方法 : 毎回空の list を使用したい事はある


def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


r = test_func(100)
print(r)

r = test_func(100)
print(r)

"""
引数に何か値が入っていれば、そのままappend(追加)するし
引数に何も入っていなければ、if文にいって空の list を初期化して
渡してあげる。
"""


# ----- 位置引数の tuple化 -----
# def say_something(word, word2, word3):
#     print(word, word2, word3)


# say_something('hi', 'Mike', 'Nance')

# 上記をまとめてくれるような引数がある
# def say_something(word, *args):
#     print('word=', word)
#     for arg in args:
#         print(arg)


# say_something('Hi', 'Mike', 'Nance')

"""
上記の様な使い方は、１つ目の引数は必ず使用したい
その他の引数はいくつ入ってくるか分からないので *args にする事によって
何個引数が与えられても追加できるし、for loop を使用して出力できる
"""

# 自分で tuple を作って *t で展開する: tuple を unpacking して渡す
# t = ('Mike', 'Nance')
# say_something('Hi', *t)


# ----- keyword 引数による dictionary化 -----
# def menu(entree='beef', drink='wine'):
#     print(entree, drink)


# menu(entree='beef', drink='coffee')

"""
{'entree': 'beef', 'drink': 'coffee'} dictionary型で返ってくる
"""

# 上記を簡単にする引数


def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


"""
menu(entree='beef', drink='coffee')
下記のにも記述できる **(アスタリスク)2つ付けてあげる事により展開される
dictionary型に **(アスタリスク)2つ付けて渡してあげるケースもよくある
"""

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}

menu(**d)


def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)


menu(
    'banana',
    'apple',
    'orange',
    entree='beef',
    drink='coffee'
)

"""
順序が大切で、*args の前に **kwargs がきてしまうと error になってしまう
"""


# ----- Docstrings -----
"""
function(関数)のドキュメントの記述の仕方
Wコーテーション3つで下記の様に記述する
記述する場所は function内に記述
どの様な関数か？の説明

Args:
    param1 (int): 説明
    param2 (str): 説明
Returns:
    bool: 説明

"""


# ----- inner function(関数内関数) -----
def outer(a, b):

    def plus(c, d):
        return c + d

    r = plus(a, b)
    print(r)


outer(1, 2)


# ----- closure(クロージャー) -----
# def outer(a, b):

#     def inner():
#         return a + b

#     return inner


# f = outer(1, 2)
# r = f()
# print(r)
"""
1 + 2 を今すぐには実行したくない場合に使用する
program が全て実行した後に実行したいなどの時
"""


def circle_area_func(pi):
    def cercle_area(radius):
        return pi * radius ** 2

    return cercle_area


ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))
"""
はじめに設定した引数を元にして後々使い回したい時に使用
"""


# ---------- decorator(デコレーター) ----------
"""
関数の前後処理をしたい場合
function の前後に何かしたい場合には、@function(decorator)を使用する
decorator を一度記載してしまえば、何度も違う関数で同じ前後処理ができる
"""


def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


@print_info
def add_num(a, b):
    return a + b


r = add_num(10, 20)
print(r)


@print_info
def sub_num(a, b):
    return a - b


r = sub_num(10, 20)
print(r)


# f = print_info(add_num)
# r = f(10, 20)
# print(r)

# print('start')
# r = add_num(10, 20)
# print('end')

# print(r)

""""
下記の様に２つ decorator を使用することもできる
しかし、順序で出力結果が違ってくるので注意する

デコレーターは包み込んで感じのイメージ
ネストに近い感じ = 入子状の状態
"""


def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper


@print_info
@print_more
def add_num(a, b):
    return a + b


r = add_num(10, 20)
print(r)


# ---------- lambda(ラムダ) ----------
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


def change_word(words, func):
    for word in words:
        print(func(word))


# def sample_func(word):
#     return word.capitalize()

# def sample_func2(word):
#     return word.lower()

# lambda で 1行にまとめる事ができる
# sample_func = lambda word: word.capitalize()

change_word(l, lambda word: word.capitalize())
change_word(l, lambda word: word.lower())

"""
大文字・小文字が入り組んで間違えている記述があった場合の直し方
※ 普通はキャピタル(頭文字は大文字)でなければいけない

function を引数とするモノは lambda を使用して定義すれば
無駄な code の記述が減らせて、ミスも減らせて、解読しやすい code になる
"""


# ---------- generator(ジェネレーター) ----------
"""
反復処理をする物 : iterator(イテレーター), list, dictionary を
for文で回していく

generator : 反復処理をする時に 1要素取り出してそれを生成していく
yield = 算出する
"""
l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)


print('###################')


def counter(num=10):
    for _ in range(10):
        yield 'run'


def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'


# for g in greeting():
#     print(g)
g = greeting()
c = counter()

print(next(g))

print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))

print(next(g))

"""
for loop だと一気に反復処理で出力するので上記の様に間に出力はできない
generator だと1回1回 loop を抜けて出力、抜けて出力の繰り返しなので
上記のように間に新たなprintの出力ができる

generator には return というものが無い
yield を見ると generator として判断する

yield と yield の間に重たい処理の program をして 1回1回重たい処理をする
一気に処理をするわけでは無いので負荷を避ける事ができる
"""


# ---------- list 内包表記 ----------
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)

# list 内包表記は上記を１行の code にまとめる事ができる

r = [i for i in t if i % 2 == 0]
print(r)


r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

# list 内包表記
r = [i * j for i in t for j in t2]
print(r)

"""
list を生成する行が１行で済む
あまりメモリを使わないので速い
短い for loop の場合は list 内包表記で記述しても良い

code が読みにくいと開発スピードが遅れたり、 bug の原因になるので
list 内包表記は使えるからといって、全部に使用する必要はない
TPO を考えて、code が読みやすくて、code 量が減らせるのであれば使用する
"""


# ---------- dictionary 辞書内包表記 ----------
w = ['Mon', 'Tes', 'Wed']
f = ['coffee', 'milk', 'water']

d = {}

for x, y in zip(w, f):
    d[x] = y

print(d)

d = {x: y for x, y in zip(w, f)}
print(d)


# ---------- set() 集合内包表記 ----------
s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)
