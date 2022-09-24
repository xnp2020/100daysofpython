with open('a.txt','r') as f:
    content = f.read()
    print(content)


from io import StringIO

f= StringIO()
f.write('hello')
f.write(' world!')
print(f.getvalue())

f= StringIO('Hello\nworld!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())