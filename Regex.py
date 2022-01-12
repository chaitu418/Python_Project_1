import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*&%@#!}{"))

a="this string has ip 192.156.43.23 and 1.2.3.4 and 127.0.0.1 and 239.254.254.254 "
pat=r'(\d+\.){3}\d+'
new_pat=r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

#255or 249 or 199 or 99 -->same as ()\.){3} or 255|249|249\199|99


#grep only valid ip addresses
# 1.0.0.0 to 126.255.255.255
# 128.0.0.0 to 191.255.255.255
# 192.0.0.0 to 223.255.255.255
# 224.0.0.0 to 239.255.255.255
# 240.0.0.0 to 245.255.255.255


output=re.findall(pat,a)
output_1=re.findall(new_pat,a)
print(output)
print(output_1)
for i in output:
    print(i)
    if(i[0]==2 and i[1]==4):
        print("invalid",i[0])