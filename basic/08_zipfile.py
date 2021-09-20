import glob
import zipfile

with zipfile.ZipFile('basic/test.zip', 'w') as z:
    # z.write('basic/test_dir')
    # z.write('basic/test_dir/sub_dir/test.txt')
    for f in glob.glob('basic/test_dir/**', recursive=True):
        print(f)
        z.write(f)

"""
terminal zip file 解凍 command
unzip  test.zip -d zzz
"""

# zip 読み込み
with zipfile.ZipFile('basic/test.zip', 'r') as z:
    # z.extractall('zzz2')
    # １つだけ読み込む場合
    with z.open('basic/test_dir/sub_dir/test.txt') as f:
        print(f.read())
