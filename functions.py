from datetime import datetime, timedelta

def find_available_slots(booked_slots, visit_duration):
    # Початковий та кінцевий час роботи притулку
    start_time = datetime(2023, 8, 1, 8, 0)
    end_time = datetime(2023, 8, 1, 18, 0)

    # Створення списку всіх доступних часових інтервалів
    available_slots = []
    current_time = start_time

    while current_time + timedelta(minutes=visit_duration) <= end_time:
        # Перевірка, чи поточний інтервал не перетинається з броньованими інтервалами
        is_slot_available = True
        for booked_slot in booked_slots:
            if current_time >= booked_slot[0] and current_time < booked_slot[1]:
                is_slot_available = False
                break

        if is_slot_available:
            available_slots.append(current_time.strftime("%H:%M"))

        # Перейти до наступного інтервалу через 15 хвилин
        current_time += timedelta(minutes=15)

    return available_slots

# Приклад
x = [(datetime(2023, 8, 1, 8, 0), datetime(2023, 8, 1, 9, 0))]
y = 2
available_slots = find_available_slots(x, y)
print(available_slots)
