import json

def load_data():
    """ функция загружает весь json файл """
    with open('data2.json') as file:
        return json.load(file)

def load_data_monday():
    """функция загружает json файл, словарь в котором ключи значений: day_week - "пн" """
    with open('monday.json') as f:
        return json.load(f)

def load_infa_by_day(day_week):
    """ функция проходиться по всему словарю и возвращает список те словари, где где в значениях есть день недели, введенный пользоателем  """
    lessons = load_data()
    for lesson in lessons:
        if lesson['day_week'] == day_week:
            return lesson

def load_infa_by_subject(subj):
    """ функция проходиться по всему словарю и возвращает в список те словари, где где в значениях есть предмет, введенный пользоателем  """
    lessons = load_data()
    days = load_data()
    useful_days = []
    for day in days:
        if day['discipline'] == subj:
            useful_days.append(day)
    return useful_days

