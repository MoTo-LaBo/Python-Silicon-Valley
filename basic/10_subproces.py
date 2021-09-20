import subprocess


subprocess.run(['ls', '-al'])

# shell=True は推奨されていない
# subprocess.run('ls -al | grep test', shell=True)

# r = subprocess.run('lsa', shell=True, check=True)
# print(r.returncode)
# print('####')
