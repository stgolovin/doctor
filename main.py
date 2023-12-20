from datetime import datetime, timedelta
from pprint import pprint

def find_free_slots(busy: list) -> list:
    '''
    Возвращает список слотов свободного времени доктора по 30 минут.
            Параметры:
                    busy (list): список слотов, когда доктор занят
            Возвращаемое значение:
                    free_slots (list): список слотов, когда доктор свободен 
    '''
    start_time = datetime.strptime('09:00', '%H:%M')
    end_time = datetime.strptime('21:00', '%H:%M')
    slot_duration = timedelta(minutes=30)

    busy_slots = [(datetime.strptime(interval['start'], '%H:%M'), datetime.strptime(interval['stop'], '%H:%M')) for interval in busy]
    
    free_slots = []
    current_time = start_time

    for busy_start, busy_stop in sorted(busy_slots):
        if current_time < busy_start:
            while current_time + slot_duration <= busy_start:
                free_slots.append({'start': current_time.strftime('%H:%M'), 'stop': (current_time + slot_duration).strftime('%H:%M')})
                current_time += slot_duration

        current_time = max(current_time, busy_stop)

    if current_time < end_time:
        while current_time + slot_duration <= end_time:
            free_slots.append({'start': current_time.strftime('%H:%M'), 'stop': (current_time + slot_duration).strftime('%H:%M')})
            current_time += slot_duration

    return free_slots

busy = [
    {'start': '10:30', 'stop': '10:50'},
    {'start': '18:40', 'stop': '18:50'},
    {'start': '14:40', 'stop': '15:50'},
    {'start': '16:40', 'stop': '17:20'},
    {'start': '20:05', 'stop': '20:20'}
]

free_slots = find_free_slots(busy)
pprint(free_slots)
