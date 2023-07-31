import time, pwinput
import PySimpleGUI as sg
t = 3
# nameinput = input("Please enter your name - ")
# ageinput = input("Please enter your age - ")
# passwordinput = pwinput.pwinput(prompt='Please enter your password: ', mask='*')

def create_user(nameinput, ageinput, passwordinput):
    details = {}
    new_entries = (("name", nameinput),("age", ageinput), ("password", passwordinput))
    details.update(new_entries)
    return print("User saved, Please Login - ")
    while True:
        loginname = input("Please enter your name - ")
        loginpassword = input("Please enter your password - ")
        time.sleep(t)
        if details["name"] == loginname and details["password"] == loginpassword:
            return print("Logged in successfully")
            break
        else:
            return print("Wrong password or username. Please try again!")

layout = [
    [sg.Text('Please input your name', key = '-TEXT1-')],
    [sg.Input(key = '-INPUT-')],
    [sg.Text('Please input your password', key = '-TEXT3-')],
    [sg.Input(key = '-INPUT1-')],
    [sg.Button('Submit', key = '-BUTTON1-')]
]

window = sg.Window('User Details', layout, element_justification= 'center')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == '-BUTTON1-':
        name_value = values['-INPUT-']
        age_value = 20
        pass_value = values['-INPUT1-']
        a = create_user(name_value, age_value, pass_value)

window.close()
