
def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if not '@' in recipient or not '@' in sender and sender.endswith(('.com', '.net', '.ru')) or not recipient.endswith(('.com', '.net', '.ru')):
        return f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}"
    elif recipient == sender:
        return "Нельзя отправить письмо самому себе!"
    elif sender == "university.help@gmail.com":
        return f"Письмо {message} успешно отправлено с адреса {sender} на адрес {recipient}."
    else:
        return f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо {message} отправлено с адреса {sender} на адрес {recipient}."
    
print(send_email("Привет!", "university.help@gmail.com"))
print(send_email("Привет!", "skuka@yandex.ru"))
print(send_email("Привет!", "skuka@yandex.ru", sender = "university.help@yandex.ru"))
print(send_email("Привет!", "skukayandex.ru", sender = "university.help@yandex.ru"))