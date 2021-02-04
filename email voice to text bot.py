import smtplib as sm
import speech_recognition as sr
import pyttsx3 as ts
from email.message import EmailMessage

listener = sr.Recognizer()
engine = ts.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = sm.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Needs to have access to your google account :)
    server.login('Sender_Email', 'Sender_Email_password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'person1': 'ps1@gmail.com',
    'person2': 'ps2@gmail.com',
    'person3': 'ps3@gmail.com',
    'person4': 'ps4@gmail.com'
}


def get_email_info():
    talk('Who is the recipient')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('What should we type')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Email sent successfully')
    talk('Maybe one more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()