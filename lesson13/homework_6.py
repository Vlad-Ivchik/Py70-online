# 6.	В справочной аэропорта хранится расписание вылета самолетов на следующие сутки. Для каждого рейса указаны номер рейса,
# пункт назначения, время вылета. Вывести все номера рейсов и время вылета самолета для заданного пункта назначения.
# Пример файла flights.json

import json

def find_flights(filename, destination):
    with open(filename, 'r', encoding='utf-8') as file:
        flights = json.load(file)

    print(f"Рейсы в {destination}:")

    for flight in flights:
        if flight['destination'].lower() == destination.lower():
            print(f"Номер: {flight['flight_number']}, Время: {flight['departure_time']}")


find_flights('flights.json', 'Москва')
find_flights('flights.json', 'Варшава')