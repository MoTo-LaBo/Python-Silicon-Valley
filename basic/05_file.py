# file 操作

# --------------- file 新規作成 , wirting ------------
"""
w は書き込み / a は追加 / print()関数を使用しても書き込める
"""
"""
f = open('basic/test.txt', 'w')
f.write('Test\n')
print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
f.close()
"""


# --------------- with ステートメント ----------------
"""
f.close() を記述しないと、メモリを使用してしまう
file open -> 必ず close : 忘れる事がある
with は自動で close()してくれる
推奨される記述の仕方
"""

# s = """\
# AAA
# BBB
# CCC
# DDD
# """

# with open('basic/test.txt', 'w') as f:
#     f.write(s)

# --------------- with ステートメント/ reading ----------------
"""
print()で一気に表示させる事もできるが...
f.readline = で１行１行読み込ませ、その後に処理を実行させるという事もできる
chunk = (チャンク)文字数指定をして読み込む / ネットワークのパケットを読み込む時に使用
"""
"""
with open('basic/test.txt', 'r') as f:
    # print(f.read())
    while True:
        chunk = 2
        line = f.read(chunk)
        # line = f.readline()          # 1行1行読み込んで表示させる
        # print(line, end='')          # default で 改行が入る / end=''改行なし
        print(line)
        if not line:
            break
"""

# --------------- seekを使って移動する ----------------
"""
f.tell() : 今いる位置が 0 そこから programe を実行
f.seek(5) : 指定した数値進んで programe を実行
指定した場所から読み込みたい・戻って読み込みたい場合などに seek() を使用する
"""
"""
with open('basic/test.txt', 'r') as f:
    print(f.tell())
    print(f.read(1))
    f.seek(5)
    print(f.read(1))
    f.seek(14)
    print(f.read(1))
    f.seek(15)
    print(f.read(1))
    f.seek(5)
    print(f.read(1))
"""

# --------------- 書き込み・読み込みモード ----------------
"""
read, write を両方やりたい場合
w+ を追記 / f.seek(0) で先頭に戻ってから、 f.read()する
"""


# s = """\
# AAA
# BBB
# CCC
# DDD
# """

# with open('basic/test.txt', 'w+') as f:
#     f.write(s)
#     f.seek(0)
#     print(f.read())

"""
print(f.read()) だけだと、書き込む為に新たにシートが作成
されて今までの .txt が削除されるので注意する
"""
# with open('basic/test.txt', 'w+') as f:
#     print(f.read())


"""
r+ 読み込んで・書き込む
読み込めないと error になってしまうので注意
"""

# with open('basic/test.txt', 'r+') as f:
#     print(f.read())
#     f.seek(0)
#     f.write(s)


# --------------- テンプレート ----------------
"""
読み込み専用として Template() は使用する
s を Template(s)として t に代入して使用する事により
s の text が壊される心配がない(sに他のtextを置き換えたり)

team 内にあまり開発(app)の事が分からない人がいる場合など…
design 専門の人と分けて使用する
"""


# s = """\

# Hi $name.

# $contents

# Have a good day
# """
# import string
# with open('basic/lesson_package/design/email_template.txt') as f:
#     t = string.Template(f.read())

# # t = string.Template(s)
# contents = t.substitute(name='Mike', contents='How are you?')
# print(contents)

"""
designer は text を編集して programmer は Template をして読み込むだけ
そうする事によって text file を壊す危険がなくなる　
"""

# --------------- csv file 操作 ----------------

import csv
from os import name, write
with open('basic/test.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})

with open('basic/test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])
