import speech_recognition as sr
from openai import OpenAI

client = OpenAI(api_key="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")

# Přidání seznamu pro ukládání historie konverzace
conversation_history = [
    {
        "role": "system",
        "content": "Jsi domácí assistent. Jmenuješ se Jimmy. Stvořila tě česká firma LunarBytes.\nTteď jsi v domácnosti muže jménem Robin Ustohal. Jsi vtipný, přátelský a rád mu pomáháš. Umíš ovládat i chytrou domácnost"
    }
]

def ask_jimmy(question):
    # Přidání otázky uživatele do historie konverzace
    conversation_history.append({"role": "user", "content": question})
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,  # Použití aktualizované historie konverzace
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Přidání odpovědi do historie konverzace
    conversation_history.append({"role": "assistant", "content": response.choices[0].message.content})
    
    return response

# Initialize the recognizer
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Kalibrace...")
    r.adjust_for_ambient_noise(source)
    
    while True:  
        print("Mluvte:")
        audio_data = r.listen(source)
        
        # Recognize the speech
        try:
            text = r.recognize_google(audio_data, language='cs-CZ')
            if text.lower() in ["jimmy exit", "jimmy konec", "jimmy vypnout"]:
                print("Vypínám.")
                break
            print("Ty: " + text)
            response = ask_jimmy(text)
            message_content = response.choices[0].message.content
            print("Jimmy: " + message_content)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from the Google Speech Recognition service; {e}")





