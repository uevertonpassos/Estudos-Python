import speech_recognition as sr

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Comece a falar. O programa transcreverá o que você diz em tempo real.")
        recognizer.adjust_for_ambient_noise(source)
        
        try:
            while True:
                audio = recognizer.listen(source)
                recognized_text = recognizer.recognize_google(audio, language="pt-BR")

                print("Você disse:", recognized_text)

        except KeyboardInterrupt:
            print("Programa interrompido pelo usuário.")
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio.")
        except sr.RequestError as e:
            print(f"Ocorreu um erro na solicitação ao serviço Google: {e}")

if __name__ == "__main__":
    main()
