import re
pattern="red"
content="It is the primary color in the rgb color model,red is the long wavelength end of the spectrum of light"
if re.search(pattern,content):
    print("matched")
else:
    print("not matched")