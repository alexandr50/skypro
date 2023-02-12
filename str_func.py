def get_upper(text: str):
    """Функция преобразующая текст в текст с заглавными буквами"""

    return text.upper()


def get_title(text: str):
    """Функция прелбразующая первые буквы в заглавные"""

    return ' '.join([x.title() for x in text.split(' ')])
