"""
Конфигурационный файл.
В нем находятся почта mail.ru, пароль и почта
куда нужно отправлять сообщение
"""
import os


username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
mail_receiver = os.getenv("MAIL_RECEIVER")
