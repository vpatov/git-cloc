import subprocess

logs = subprocess.run(["git","log"],cwd="/home/vasia/repos/522/",shell=True,stdout=subprocess.PIPE)
print(logs.stdout.decode())
