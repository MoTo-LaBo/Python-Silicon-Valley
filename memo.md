## code
    # python file 実行(terminal)
    control + command + P

    # terminal へ移動
    control + command + T

    # file 切り替え
    command + P

    # 改行増やす
    ctr + o

    # 改行削除
    ctr + p
## data 構造
### 値渡しと参照私
- 値渡し(int:整数)
- 整数型で代入するとそのまま代入した整数に入れ替わる
- x, y はそれぞれ違う ID を持っている
#### sample
    x = 20
    y = x
    y = 5
    print(y) -> 5
### 参照渡し(list, dictionary)
- list型, dictionary型
- 代入した値のアドレスをそのまま引き継ぐ形で新たな変数に取り込む形になる
- x, y どちらも同じ id を持っている
#### sample
    x = ['a', 'b']
    y = x
    y[0] = 'p'
    print(y)
    print(x)
- bug の原因にならないように注意する
## tar file 展開
### 1. tar 展開（tarminal）: directory内に tar file　
    tar -zxvf python_programming_demo_app-0.0.1.tar.gz
### 1. zip 展開 (tarminal) : directory内に zip file
    unzip python_programming_demo_app-0.0.1.zip
## pytho code style
### pep8 -> pycodestyle に名前変更
    pip install pep8 -> pip install pycodestyle
    # terminal
    pycodestyle <file name>
- 優しめの code チェック
### flake8
    pip install flake8
    # terminal
    flake8 <file name>
- pycodestyle より少し厳し目
### pylint
    pip install pylint
    # terminal
    pylint <file name>
- かなりしっかりとしたチェック
