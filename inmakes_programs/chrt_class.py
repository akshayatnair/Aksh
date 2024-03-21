import re
pattern = "[A-Z][0-9][a-z]"
if re.search(pattern, "U8k"):
    print("matched")
else:
    print("not matched")