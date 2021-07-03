import math

# 変数宣言
num = 1
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# 型変換
num = name
print(num, type(num))

name = '1'
new_name = int(name)
print(new_name, type(new_name))

# print
print('hi', 'Mike')
print('hi', 'Mike', sep=',')  # sep -> カンマで区切ることができる
print('hi', 'Mike', sep=',', end='.\n')  # \n 改行

# 変数
print(2 + 2)

# math を import すれば math の method で数学関数を使用する事ができる
result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)
# print(help(math))

# 文字列
s = 'test'
print(s)
print('hello')
print('I don\'t know')
print('say"I don\'t know"')
print("say\"I don't know\"")

print('hello. How are you?')
print('hello.\nHow are you?')
print('C:\name\name')
print(r'C:\name\name')

print('################')
print("""
line1
line2
line3
""")
print('################')


print('################')
print("""line1
line2
line3""")
print('################')
print('################')
print("""\
line1
line2
line3\
""")
print('################')

# ''(シングルコーテートで囲うモノ) = リテラル
print('Hi.' * 3 + 'Mike')
print('py' + 'thon')
prefix = 'py'
print(prefix + 'thon')

# 一行で記述しているのと同じ
s = ('aaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbb')
print(s)
# \ (バックスラッシュ)でも同じ記述はできるが… 見易さから考えると()が良い
s = 'aaaaaaaaaaaaaaaaa'\
     'bbbbbbbbbbbbbbbbb'
print(s)