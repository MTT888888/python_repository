import re

# mat=re.search(r'[1-9]\d{5}','ft 100081')
# if mat:
#     print(mat.group(0))
# mat=re.match(r'[1-9]\d{5}','100026 fgf')
# if mat:
#     print(mat.group(0))
# ls=re.findall(r'[1-9]\d{5}','ggy100086 hum741007')
# print(ls)
# ss=re.split(r'[1-9]\d{5}','hehfhv123456 hu234567',maxsplit=1)
# print(ss)
# for m in re.finditer(r'[1-9]\d{5}','hehfhv123456 hu234567'):
#     if m:
#         print(m.group(0))
bc=re.sub(r'[1-9]\d{5}','：字母','hehfhv123456 hu234567')
print(bc)