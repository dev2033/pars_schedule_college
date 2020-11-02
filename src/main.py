"""
Главный файл, запускающий проект
"""
from time import sleep
from scrap import pars_img
from send_mail import send_mail
from my_logger import logger


@logger.catch
def main():
    pars_img()
    sleep(20)
    logger.info("Картинка скачана! Щас отправлю на mail.ru \n...\n...")
    send_mail()
    logger.info("Отправил...")


if __name__ == '__main__':
    main()
