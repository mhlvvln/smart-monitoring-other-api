from datetime import datetime
from random import randint

import matplotlib.pyplot as plt
from io import BytesIO


def generateChart(total_space, used_space):
    labels = 'Использованное', 'Свободное'
    sizes = [used_space, total_space - used_space]
    colors = ['#fe7777', '#66b3ff']

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, textprops={'fontweight': 'bold'})
    ax1.set_title('Использованное пространство на диске')
    ax1.axis('equal')
    ax1.legend(labels, loc='lower right')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    return buffer.getvalue()


def sort_times(data: list[dict]):
    """"
        сортируем по юникс времени
    """
    sorted_data = sorted(data, key=lambda x: x['unix_time'])
    return sorted_data


def generateTimeChart(data: list[dict]):
    """"
        unix_time - время юникс
        workload - загруженность
    """
    data = sorted(data, key=lambda x: x['unix_time'])

    for entry in data:
        entry['unix_time'] += 3600*3

    times = [datetime.utcfromtimestamp(entry['unix_time']).strftime('%H:%M') for entry in data]
    workloads = [entry['workload'] for entry in data]

    plt.plot(times, workloads, marker='o', linestyle='-', color='blue')

    plt.xlabel('Время')
    plt.ylabel('Загруженность')
    plt.xticks(rotation=45, ha="right")
    plt.title('График загруженности в зависимости от времени')
    plt.grid(True, linestyle='--', alpha=0.5)

    plt.legend(['Загруженность'])

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    return buffer.getvalue()


data = [
    {
        'unix_time': randint(1699106712-86000*5, 1699106712+86000*5),
        'workload':randint(5, 15)
    },
    {
        'unix_time': randint(1699106712-86000*5, 1699106712+86000*5),
        'workload': randint(5, 15)
    },
    {
        'unix_time': randint(1699106712-86000*5, 1699106712+86000*5),
        'workload': randint(5, 15)
    },
    {
        'unix_time': randint(1699106712-86000*5, 1699106712+86000*5),
        'workload': randint(5, 15)
    },
    {
        'unix_time': randint(1699106712-86000*5, 1699106712+86000*5),
        'workload': randint(5, 15)
    },
    {
        'unix_time': randint(1699106712-86000*5, 1699106712+86000*5),
        'workload': randint(5, 15)
    },
    {
        'unix_time': randint(1699106712-86000*5, 1699106712+86000*5),
        'workload': randint(5, 15)
    },
    {
        'unix_time': randint(1699106712-86000*5, 1699106712+86000*5),
        'workload': randint(5, 15)
    },
    {
        'unix_time': randint(1699106712-86000*5, 1699106712+86000*5),
        'workload': randint(5, 15)
    },
]
