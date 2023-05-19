import whisper
import webbrowser
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import csv
import speech_recognition as sr


def callMap(start="your location", target="台北101"):
    urL='https://www.google.com/maps/dir/' + start + '/' + target
    webbrowser.get('windows-default').open_new(urL)


def searchDB(idx):
    with open('./維修人員助理_db.csv', newline='',encoding="utf-8") as csvfile:

        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)

        # 以迴圈輸出每一列
        for row in rows:
            if(row[0].find(idx) != -1):
                return row
    return None

# speech recognition
# r = sr.Recognizer()
# mic = sr.Microphone(device_index=1) # noice device index

# with mic as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
    
# print(text = r.recognize_whisper(audio, model='tiny', show_dict=True, )['text'])


# langchain
llm = OpenAI(temperature=0.1)

# template
prompt = PromptTemplate(
    input_variables=["text"],
    template="以下將透過" "來標示一段內容，回答內容中要去的基站號碼，只輸出數字而完完全全不要任何文字或解釋，回答單純數字 :\"{text}\""
)


# tiny < base < small < medium < large
model = whisper.load_model("small")
result = model.transcribe("./TWM.mp3")


if(result["text"].find("台灣") != -1 or result["text"].find("大哥大") != -1):
    result = model.transcribe("./example3.mp3")
    print(prompt.format(text=result["text"]))
    # ret = llm(prompt.format(text=result["text"]))
    ret = "13"
    # print(type(ret))
    # print(ret)


    # get customer's data
    data = searchDB(idx=ret)
    
    print(data)
    callMap(target=data[2])

    print("屋主名字: " + data[1])
    print("屋主電話: " + data[3])