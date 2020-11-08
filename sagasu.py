import re

s = 'aaa@xxx.com'
m = re.match(r'[a-z]+@[a-z]+\.[a-z]+', s)
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


pattern = r'(0?[1-9]|1[0-2])[/\-月](0?[1-9]|[12][0-9]|3[01])日?$'
print(bool(re.match(pattern,"11月8日")))