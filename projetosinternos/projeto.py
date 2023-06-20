import sys
import time
import tkinter as tk
from tkinter import ttk

def download_video():
    url = entry.get()
    for i in range(11):
        time.sleep(1)
        progress_bar['value'] = i * 10
        window.update_idletasks()

window = tk.Tk()

window.geometry("400x200")

window.title("Download de Vídeo")

label = tk.Label(window, text="Cole o link aqui para baixar", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 12), width=40)
entry.pack()

progress_bar = ttk.Progressbar(window, orient=tk.HORIZONTAL, length=300, mode='determinate')
progress_bar.pack(pady=10)

button = tk.Button(window, text="Baixar", font=("Arial", 12), command=download_video)
button.pack(pady=10)

window.mainloop()
