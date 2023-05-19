import speech_recognition as sr
import pyttsx3
import os


# speech recognition
r = sr.Recognizer()
mic = sr.Microphone(device_index=3) # noice device index

with mic as source:
    r.adjust_for_ambient_noise(source)
    print("說些什麼吧！")
    audio = r.listen(source,timeout=10,phrase_time_limit=3)
    text = r.recognize_whisper(audio, model='small', show_dict=True)['text']
print("您說的是：" + text)




# # 設置語音引擎
# engine = pyttsx3.init()

# # 設置語音識別器
# r = sr.Recognizer()

# # 設置麥克風作為音訊來源
# with sr.Microphone(device_index=2) as source:
#     print("說些什麼吧！")
#     audio = r.listen(source)

# # 將語音轉換為文字
# try:
#     text = r.recognize_whisper(audio, model='tiny', show_dict=True, )['text']
#     print("您說的是：" + text)
# except sr.UnknownValueError:
#     print("語音無法識別！")
#     text = "語音無法識別"
# except sr.RequestError as e:
#     print("無法連接到語音識別服務： {0}".format(e))
#     text = "無法連接到語音識別服務"