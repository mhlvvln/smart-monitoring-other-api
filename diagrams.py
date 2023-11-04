import matplotlib.pyplot as plt
from io import BytesIO


def generateChart(total_space, used_space):
    labels = 'Использованное', 'Свободное'
    sizes = [used_space, total_space - used_space]
    colors = ['#ff3333', '#66b3ff']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.set_title('Использованное пространство на диске')
    ax1.axis('equal')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    return buffer.getvalue()

