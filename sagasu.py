import re

s = 'aaa@xxx.com'
m = re.match(r'[a-z]+@[a-z]+\.[a-z]+', s)
print(m)
print(m.group())
try:
    k=0
    r_message="25:11"
    r_message=r_message.split(":")
    print(r_message)
    for i in r_message:
        r_message[k]=int(i)
        k+=1
    print(r_message)

    if r_message[0]>=25 or r_message[1]>=60:
        print("NG")
        error_flag=1
except:
    print("NG")
    error_flag=1


