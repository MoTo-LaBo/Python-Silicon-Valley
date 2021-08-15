import math

# 変数宣言
num = 1
name = '1'
is_ok = True


# 型変換
new_num = int(name)
print(new_num, type(new_num))

print('Hi', 'Mike', sep=',', end='.\n')
print('Hi', 'Mike', sep=',')
print('Hi', 'Mike', sep=',')

result = math.sqrt(25)
print(result)

y = math.log2(10)

print(y)

print(help(math))

# 文字列
s = 'test'
print(s)
print('hello')
print("hello")
print("I don't know")
print('say "I don\'t know"')
print("say \"I don't know\"")

print('hello.\nHow are you?')
print(r'C:\name\name')

print("##############")
print("""\
line1
line2
line3\
""")
print("##########")

print('Hi' * 3 + 'Mike')
s = ('aaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)
word = 'python'
print(word[0])
print(word[1])
print(word[-1])

print(word[0:2])
print(word[:2])
print(word[1:])

word = 'j' + word[1:]
print(word)
n = len(word)
print(n)

# method
s = 'My name is Mike. Hi Mike'
print(s)
# is_start の最初の文字は My かどうか？
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('x')
print(is_start)

# index number
print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))

print(r.count(3))

if 5 in r:
    print('exist')

# こちらは表示されない
if 100 in r:
    print('exist')

r.sort()
print(r)

r.sort(reverse=True)
print(r)

print(r)
r.reverse()
print(r)

s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)

print(help(list))

i = [1, 2, 3, 4, 5]

# tuple unpacking

chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)

# dictionary
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

l = [
    ['apple', 100],
    ['banana', 200],
    ['orange', 300],
]

# ハッシュタグtable：検索スピードが早い
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}

print(fruits['apple'])

# 集合
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)

# list -> 集合へ型変換
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)
