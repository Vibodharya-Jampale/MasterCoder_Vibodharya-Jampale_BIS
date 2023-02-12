# Use Cases:
# Q1: What time is a specific event on a specific day?
# Q2: What event is on a specific time on a specific day?

# Binary Search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Partition a calendar based on date
def create_partitioned_calendar(cal):
    calendar_dict = {}
    for element in cal:
        key = element[0]
        if key not in calendar_dict:
            calendar_dict[key] = [[element[1], element[2], element[3]]]
        else:
            calendar_dict[key].append([element[1], element[2], element[3]])
    return calendar_dict


# Given the event name and date, find the time of the event
def find_time_of_event_on_a_day(cal, event_name, event_date):
    if event_date not in cal:
        return f'There are no events for: {event_date}'

    list_of_events = cal[event_date]
    sorted_list_of_events = sorted(list_of_events, key=lambda x: x[1])
    array_of_event_names = []
    for event in sorted_list_of_events:
        array_of_event_names.append(event[1])

    index = (binary_search(array_of_event_names, event_name))
    if index >= 0:
        return f'The time of {event_name} on {event_date} is {sorted_list_of_events[index][0]} '
    else:
        return f'{event_name} doesn\'t exist in the calendar for: {event_date}'


# Given the event date and time, find the name of the event
def find_event_on_time_of_day(cal, event_date, event_time):
    if event_date not in cal:
        return f'There are no events for: {event_date}'

    list_of_events = cal[event_date]
    sorted_list_of_events = sorted(list_of_events, key=lambda x: x[0])

    time_event_list = []
    for event in sorted_list_of_events:
        time = event[0]
        name = event[1]
        duration = event[2]
        time_event_list.append([time, name])
        for _ in range(0, duration):
            time_hour = int(time.split(':')[0])
            time_min = int(time.split(':')[1])
            time_min += 1
            if time_min >= 60:
                time_hour += 1
                time_min %= 60
            if time_hour < 10:
                time = f'0{time_hour}'
            else:
                time = f'{time_hour}'
            if time_min < 10:
                time = f'{time}:0{time_min}'
            else:
                time = f'{time}:{time_min}'
            time_event_list.append([time, name])

    array_of_event_times = []
    for event in time_event_list:
        array_of_event_times.append(event[0])

    index = (binary_search(array_of_event_times, event_time))
    if index >= 0:
        return f'The name of the event at {event_time} on {event_date} is {time_event_list[index][1]} '
    else:
        return f'{event_time} doesn\'t exist in the calendar for: {event_date}'


if __name__ == '__main__':
    calendar = [['11-2-2023', '08:30', 'School Meeting', 45],
                ['11-2-2023', '05:30', 'Work Meeting', 30],
                ['11-2-2023', '21:30', 'House Meeting', 25],
                ['11-2-2023', '22:30', 'Restaurant Meeting', 55],
                ['12-2-2023', '08:30', 'School Meeting', 60],
                ['12-2-2023', '05:30', 'Work Meeting', 35],
                ['12-2-2023', '21:30', 'House Meeting', 45],
                ['12-2-2023', '23:30', 'Restaurant Meeting', 45]]
    partitioned_calendar = create_partitioned_calendar(calendar)

    # Q1: What time is a specific event on a specific day?
    print(find_time_of_event_on_a_day(partitioned_calendar, 'House Meeting', '11-2-2023'))

    # Q2: What event is on a specific time on a specific day?
    print(find_event_on_time_of_day(partitioned_calendar, '12-2-2023', '06:05'))
