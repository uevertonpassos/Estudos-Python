from tkinter.constants import NUMERIC
from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkTeal')

layout = [ 
    [sg.Text("Login: "), sg.Input(key=('Login'),size=(20,1))],
    [sg.Text('Senha:'), sg.Input(key= ('Senha'), password_char='*',size=(20,1))],
    [sg.Button("Enter")]
]

window = sg.Window('Faça Login', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Enter":
        if values ['Login'] == 'Batata' and values ['Senha'] == '1234':
            print('Bem vindo ao sistema!')

            # teste
