import sys

from pytube import YouTube


url = input(str("Cole o link para download: "))
video = YouTube(url)

stream = video.streams.get_highest_resolution()

# substitua pelo path da sua máquina
stream.download(r'C:\Users\Ueverton Passos\Videos\Downloads')

sys.exit()

