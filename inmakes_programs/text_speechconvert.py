from gtts import gTTS
import os
text="Hai akshaya"
output=gTTS(text=text,lang='en',slow=False)
output.save('output.mp4')
os.system('start output.mp4')