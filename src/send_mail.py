"""
Отправка сообщения с картинкой
расписания на mail.ru
"""
import os
import smtplib

from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from my_logger import logger

from config import username, password, mail_receiver


def send_mail() -> None:
    """Отправляет сообщение с расписанием занятий"""
    try:
        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)

        # Формируем тело письма
        subject = input("Введи текст темы сообщения: ")
        main_body_text = input("Введи текст сообщения для отправки: ")

        # Отправка текста: (как альтернатива способу ниже)
        # msg_img = MIMEMultipart()
        # msg = MIMEText(body, 'plain', 'utf-8')
        # msg['Subject'] = Header(subject, 'utf-8')

        img_data = open('schedule/schedule.png', 'rb').read()

        msg = MIMEMultipart()

        image = MIMEImage(img_data, name=os.path.basename('schedule/schedule.png'))

        msg['Subject'] = Header(subject, 'utf-8')
        text = MIMEText(main_body_text)

        msg.attach(text)
        msg.attach(image)

        # Отправляем письмо
        server.login(username, password)
        server.sendmail(username, mail_receiver, msg.as_string())

        server.quit()
    except FileNotFoundError:
        logger.warning("NOT schedule.png")
