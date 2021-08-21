# ------------ comment ------------

print('XXXXX')
# test
print('XXXXX')
"""
comment は横にもかけるが python の記述の際には
"""
# Apple price
some_value = 100  # Apple price

"""
暗黙の了解で commento は上に記述する
pythonic code を心がける
可読性を重視した高水準のマルチパラダイムプログラミング言語
Pythonは、「Pythonの禅」別名では PEP 20と呼ばれるルール
に従って開発、保守され、幅広く使用されている言語
"""
s = 'aaaaaaaaaaaa' \
    + 'bbbbbbbb'
print(s)

x = 1 + 1 + 1 \
    + 1 + 1 + 1
print(x)

x = (1 + 1 + 1
     + 1 + 1 + 1)
print(x)

# python の場合は 80 文字記述したら次の行にいくべきと言われいる

# ------------ if文 ------------
x = 10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('10')
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

# ------------ 論理演算子 ------------
a = 1
b = 1

# a = b
print(a == b)

if a == b:
    print('equal')

# a が b と異なる
print(a != b)

# a が　b より小さい
print(a < b)

# a　が　b　よりも大きい
print(a > b)

# a　が　b 以下である (同じ数値は含む)
print(a <= b)

# a　が b　以上である (同じ数値は含む)
print(a >= b)

# a も b 真であれば真 (両方当てはまれば)
print(a > 0 and b > 0)

if a > 0 and b > 0:
    print('a and b are positive')

# a または b が真であれば真 (どちらかが当てはまれば)
print(a > 0 or b > 0)

if a > 0 or b > 0:
    print('a or b is positive')


# In, Not
y = [1, 2, 3]
x = 1

# y に x は入っていますか？
if x in y:
    print('in')

if 100 not in y:
    print('not in')


a = 1
b = 2

# a と b は等しくない
if not a == b:
    print('Not equle')

"""
python では上記の様な記述の仕方は進められていない
なぜかというと、!= で表せる
数字の違いを見るときは Not は好ましくない
"""

if a != b:
    print('Not equle')

# では not をどの様な時に使用するのか？
# 下記のように bool(boolean)型を否定するときに使用する
is_ok = True

if not is_ok:
    print('hello')
"""
boolean型の時は not を使用する
"""


# ------------ if での判定式でよく使用する ------------
# is_ok = True
# is_ok = 1
# is_ok = 0
# is_ok = 100
# is_ok = ''
# is_ok = 'string'
# is_ok = []
is_ok = [1, 2, 3, 4]

if is_ok:
    print('OK!')
else:
    print('No!')


"""
要は変数に何か値が入っていれば、python は True を返す
変数に何も入っていない場合は False を返す
False : 0, 0.0, ' ', [], {}, (), set()
' ' からの文字列かどうかを確認する時によく使用される
list が一番有効に使用できる
"""

# None(object が無い)
is_enpty = None
# print(is_enpty)

"""
変数は宣言(定義)するが何も入れたくない場合に使用
"""
# 下記のような判定の仕方は python では == None 判定は進められていない
if is_enpty == None:
    print("None")

# 修正後：is が進められている
if is_enpty is None:
    print('None')

# None 出ない場合なので表示されない
if is_enpty is not None:
    print('None')

"""
is とは？…
object 同士が同一の物(同じモノ)とならなければ真(True)とはならない
is -> None object の時に一番使用される
None と is はセット
"""
print(1 == True)
print(1 is True)
print(1 is 2)
print(True is True)
print(None is None)

a = 1
b = 1

print(a == b)

"""
変数の値が一緒かどうかを判定するときは == を使用する
None かどうかの判定は is
"""
