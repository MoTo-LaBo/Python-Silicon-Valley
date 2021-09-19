# ---------- module・package ----------
# import lesson_package.utils  # 1
# from lesson_package.tools import human
# from lesson_package.tools import animal
# from lesson_package.tools import *
# from lesson_package import utils  # 2
# from lesson_package import utils as u  # 2
# from lesson_package.utils import say_twice  # 3

# r = lesson_package.utils.say_twice('hello')
# r = utils.say_twice('hello')
# r = u.say_twice('hello')
# r = say_twice('hello')

# print(r)

"""
3番目の使用の仕方は好まれてはいない。function の出どころが分からない
program が長くなって下の方になってきたら、say_twice は何処で使用している
function なのか?となる
コンフリクトを起こして Bug につながる事がある

1, 2 番目は,module の中の関数(function)として呼び出せるので、
program を読んでいても, 他の function(関数)とぶつかる事がない

会社によってルールは変わる。
フル path で読み込むか、moduleで読むか
最低限は module から読み込む事

module の名前を変更したい時は as <変更後> の用意する
module 名が分からなくなってしまうので、あまり as も
使用しない方が良いと言われている。 pythonic code (読みやすさ)

from lesson_package.tools import *
上記のようにアスタリスクを使用した時は、__init__.py fileに
__all__ = ['animal', 'human'] のようにlist内にfile名を
記述する事。そうしないと import error になる
これもあまり進められていない。 * を使用した import は避けたほうが良い
"""

# print(human.sing())
# print(human.cry())
# print(animal.sing())
# print(animal.cry())


# ---------- ImportError ----------
# try:

# from lesson_package import utils
# except ImportError:
#     from lesson_package.tools import utils

# utils.say_twice('word')


# ---------- 組み込み function ----------
"""
https://docs.python.org/ja/3/library/functions.html
"""

from basic import lesson_package
from collections import defaultdict
ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

# for key in ranking:
#     print(key)

# print(sorted(ranking, key=ranking.get))
print(sorted(ranking, key=ranking.get, reverse=True))


# ---------- 標準ライブラリ ----------
"""
https://docs.python.org/3.9/library/collections.html#collections.defaultdict
"""

s = 'kdjasigiheaighfghad;sgasdfh'
d = {}

for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1

print(d)

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1

print(d)


d = defaultdict(int)

for c in s:
    d[c] += 1

print(d)

print(d['a'])


# ---------- サードパーティーライブラリ ----------
"""
https://pypi.org/
pip install <library name>
terminal で install
"""


# ---------- import の際の注意 ----------
"""
1. python 標準 library
2. サードパティー library
3. 自分達の package
4. local package

・１~４までの間は１行開けて区切りをわかるようにする事
・各library の中でアルファベット順に並べる事

code を見た際に何処から取得してきたかすぐ分かるようにする事

1. 標準 library : python ver の中にそのまま格納されている
2. サードパーティー : site-packages に格納されている

print(library name.__file__) で出力できる
"""


# ---------- __name__,__main__ について ----------

def main():
    lesson_package.tool.animal.sing()


if __name__ == '__main__':
    main()
"""
上記のように記述する理由は、他のfunction を import した際に
実行されないようにする為
python ではこのような記述の仕方が安全とされている

実際の開発や現場では必ず上記のように記述する事
"""
