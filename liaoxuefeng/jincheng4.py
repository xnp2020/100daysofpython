import subprocess

r = subprocess.call(['nslookup','www.baidu.com'])  # 子进程执行命令
print('Exit code: ',r)


p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n') #子进程命令交互
print(output.decode('utf-8'))
print('Exit code:', p.returncode)