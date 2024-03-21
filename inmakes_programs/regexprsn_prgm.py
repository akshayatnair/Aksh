import re
pattern="jasmine"
content="jasmine are white coloured flower"
if re.match(pattern,content):
    print("matched")
else:
    print("not matched")