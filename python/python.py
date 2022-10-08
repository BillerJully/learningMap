from asyncio import QueueEmpty
import queue


DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':  
        friends_list = ''
        for names in DATABASE.keys():
            friends_list += names + ' '
        return("Твои друзья: " + friends_list)
    elif query == 'Где все мои друзья?':
        city_list = ''
        for city in DATABASE.values():
            city_list += city + ' '
        return ("Твои друзья  в городах: " + city_list) 
    else:
        return '<неизвестный запрос>'

# Не изменяйте следующий код
print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))