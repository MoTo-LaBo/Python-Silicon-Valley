# App Prototype（venv）
### 1. 仮想環境 venv:app
    python -m venv app
### 2. 仮想環境立ち上げ
    source app/bin/activate
### 3. pip upgrade
    pip install --upgrade pip
### 4. 仮想環境から出る
    deactivate
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
