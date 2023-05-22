import webbrowser
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import speech_recognition as sr
import csv
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play

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

def speech_to_text(audio_path):
    # audio_file=open(audio_path, "rb")
    # transcript = openai.Audio.transcribe("whisper-1", audio_file)
    # decode_text = json.loads('"' + transcript.text + '"')
    
    # return decode_text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        text = r.recognize_whisper_api(audio)
        print(f"Whisper API thinks you said {text}")
        return text
    
    except sr.RequestError as e:
        print("Could not request results from Whisper API")
        return

def langchain(text):
    llm = OpenAI(temperature=0.1)

    prompt = PromptTemplate(
        input_variables=["text"],
        template="以下將透過" "來標示一段內容，回答內容中要去的基站號碼，只輸出數字而完完全全不要任何文字或解釋，回答單純數字 :\"{text}\""
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(text)

    return result[2]

#播放音檔
def play_audio_file(file_path):
    audio = AudioSegment.from_file(file_path)
    play(audio)


def text_to_speech(text, output_file=None):
    # 建立語音合成器物件
    engine = pyttsx3.init()

    # 設定語音合成引擎的參數
    engine.setProperty('rate', 150)  # 設定語速，預設為 200

    # 設定中文語音合成引擎
    engine.setProperty('voice', 'zh')  # 使用中文語音合成引擎

    if output_file:
        # 將語音合成輸出到音訊檔案
        engine.save_to_file(text, output_file)
        engine.runAndWait()
    else:
        # 直接播放語音合成結果
        engine.say(text)
        engine.runAndWait()

if __name__ == "__main__":
    question = speech_to_text("D:\TzuWei\Interest\side_project\ITG\example1.mp3")
    number = langchain(question)
    data = searchDB(number)

    text_to_speech(f"屋主名字： {data[1]}，屋主電話： {data[3]}，地址： {data[2]}，將為您開啟地圖", output_file="output.wav")
    print("屋主名字: " + data[1])
    print("屋主電話: " + data[3])
    print("屋主地址: " + data[2])
    play_audio_file("output.wav")
    callMap(target=data[2])
    

