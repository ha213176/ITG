# from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
# from langchain.memory import ConversationBufferWindowMemory

# prompt = PromptTemplate(
#     input_variables=["history", "human_input"], 
#     template=template
# )


# chatgpt_chain = LLMChain(
#     llm=OpenAI(temperature=0), 
#     prompt=prompt, 
#     verbose=True, 
#     memory=ConversationBufferWindowMemory(k=2),
# )

import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    # mp3 = sr.AudioFile('./total_end.mp3')
    with sr.Microphone() as source:
    # with mp3 as source:
        print('Calibrating...')
        r.adjust_for_ambient_noise(source, duration=5)
        # optional parameters to adjust microphone sensitivity
        # r.energy_threshold = 200
        # r.pause_threshold=0.5    
        
        print('Okay, go!')
        while(1):
            text = ''
            print('listening now...')
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=30)
                print('Recognizing...')
                # whisper model options are found here: https://github.com/openai/whisper#available-models-and-languages
                # other speech recognition models are also available.
                text = r.recognize_whisper(audio, model='medium.en', show_dict=True, )['text']
            except Exception as e:
                unrecognized_speech_text = f'Sorry, I didn\'t catch that. Exception was: {e}s'
                text = unrecognized_speech_text
            print(text)

            
            # response_text = chatgpt_chain.predict(human_input=text)
            # print(response_text)

def main():
    listen()

if __name__ == "__main__":
    main()