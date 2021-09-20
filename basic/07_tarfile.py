import tarfile
import os
import pathlib

# os.mkdir('test_dir')
# os.mkdir('test_dir/sub_dir')
# pathlib.Path('test_dir/sub_dir/test.txt').touch()

# 上記で作成した dir, file を１つにまとめる
with tarfile.open('basic/test.tar.gz', 'w:gz') as tr:
    tr.add('basic/test_dir')

"""
terminal による tarfile の解凍 command

$ tar zxvf test.tar.gz -C /tmp
$ cat /tmp/test_dir/test.txt
"""

# python file内で tarfile を読み込む
with tarfile.open('basic/test.tar.gz', 'r:gz') as tr:
    # tr.extractall(path='test_tar')
    # 展開しないで中身だけを見る
    with tr.extractfile('basic/test_dir/sub_dir/test.txt') as f:
        print(f.read())

# pathlib.Path('08_zipfile.py').touch()
pathlib.Path('09_tempfile.py').touch()
