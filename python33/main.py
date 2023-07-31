import PySimpleGUI as sg
import password

layout = [
    [sg.Text("Please input your name", key = '-TEXT1-')],
    [sg.Input(key = '-INPUT1-')],
    [sg.Text("Please input your age", key = '-TEXT2-')],
    [sg.Input(key = '-INPUT2-')],
    [sg.Text("Please input your password", key = '-TEXT3-')],
    [sg.Input(key = '-INPUT3-')],
    [sg.Button("Submit", key = '-BUTTON1-'), sg.Button("Exit") ]
]

window = sg.Window('User Details', layout, element_justification= 'center')
password.protect()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    
    if event == '-BUTTON1-':
        print("Details collected")
window.close()
