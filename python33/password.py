import PySimpleGUI as sg
import hashlib

def protect():
    
    layout = [
        [sg.Text("Enter you email address: "), sg.Input(key = "-EMAIL-", do_not_clear=False, size=(30,1))],
        [sg.Text("Enter Password", size=(15,1)), sg.InputText('', key="-PASSWORD-", password_char="*", size = (15,1))],
        [sg.Button("Submit"), sg.Button("Exit")]
    ]

    password_window = sg.Window('Login', layout, modal=True)

    def verify_password(password):
        hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
        password_utf = password.encode('utf-8')
        password_hash = hashlib.sha256(password_utf).hexdigest()
        if hash == password_hash:
            return True
        return False

    def verify_email(email_address):
        user_email_address = ["nick.nickhall.co.za", "nick@gmail.com", "nick@yahoo.com"]
        if email_address in user_email_address:
            return True
        return False

    while True:
        event, values = password_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            exit()
        elif event == "Submit":
            email_input_value = values["-EMAIL-"]
            password_input_value = values["-PASSWORD-"]
            if verify_password(password_input_value) and verify_email(email_input_value):
                break
            else:
                continue
    password_window.close()