import whisper
import pyaudio


chunk = 1024                     # 記錄聲音的樣本區塊大小
sample_format = pyaudio.paInt16  # 樣本格式，可使用 paFloat32、paInt32、paInt24、paInt16、paInt8、paUInt8、paCustomFormat
channels = 2                     # 聲道數量
fs = 44100                       # 取樣頻率，常見值為 44100 ( CD )、48000 ( DVD )、22050、24000、12000 和 11025。
seconds = 5                      # 錄音秒數
filename = "oxxostudio.wav"      # 錄音檔名

p = pyaudio.PyAudio()            # 建立 pyaudio 物件

print("開始錄音...")

# 開啟錄音串流
stream = p.open(format=sample_format, channels=channels, rate=fs, frames_per_buffer=chunk, input=True)

# tiny < base < small < medium < large
model = whisper.load_model("small")
result = model.transcribe("./TWM.mp3")
print(result["text"])

if(result["text"].find("台灣") != -1 or result["text"].find("大哥大") != -1):
    result = model.transcribe("./total_end.mp3")
    print(result["text"])
    exit(0)
    # do 
