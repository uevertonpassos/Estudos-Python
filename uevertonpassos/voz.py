import speech_recognition as sr
import subprocess

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Erro ao executar o comando:", command)

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Aguardando o comando 'LAW'...")
        recognizer.adjust_for_ambient_noise(source)
        
        while True:
            audio = recognizer.listen(source)
            
            try:
                recognized_text = recognizer.recognize_google(audio).lower()
                print("Comando detectado:", recognized_text)
                
                if "law" in recognized_text:
                    if "open the terminal" in recognized_text:
                        execute_command("start cmd")  
                    
                    
            except sr.UnknownValueError:
                print("Não foi possível entender o áudio.")
            except sr.RequestError as e:
                print("Erro na solicitação ao Google Speech Recognition:", e)

if __name__ == "__main__":
    main()
