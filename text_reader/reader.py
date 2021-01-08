from gtts import gTTS
import os
counter = 0
def read(str):
    language = 'en'
    global counter
    myObj = gTTS(text=str, lang=language, slow=False)
    counter+=1
    # path = 'audio'+str(counter) + ".mp3"
    # myObj.save("static/{x}".format(x=path))

    myObj.save("static/test.mp3")