import sys


def convert_to_minute(time):
    hour, minute = map(int, time.split(':'))
    return hour * 60 + minute


def convert_to_hour_minute(time_minute):
    hour = time_minute // 60
    minute = time_minute % 60
    if minute == 0:
        minute = '00'
    return f'{hour}:{minute}'


def main():
    times = []
    with open(sys.argv[1], 'r', encoding='utf8') as file:
        for visit in file:
            in_time, out_time = map(convert_to_minute, visit.split())
            times.append((in_time, 'start'))
            times.append((out_time, 'end'))
    times = sorted(times, key=lambda x: (x[0], len(x[1])))
    visits = dict()
    count, maxCount = 0, 0
    for time in times:
        if time[1] == 'start':
            count += 1
        else:
            count -= 1
        visits[time[0]] = count
        maxCount = max(count, maxCount)
    start_interval = False
    for time, count_vis in sorted(visits.items()):
        if count_vis == maxCount and not start_interval:
            start_time = time
            start_interval = True
        elif count_vis != maxCount and start_interval:
            print(*map(convert_to_hour_minute, (start_time, time)))
            start_interval = False


if __name__ == '__main__':
    main()
