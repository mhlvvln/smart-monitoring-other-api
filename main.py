from auth import getToken
import requests
from json import loads
from fastapi import FastAPI, Response

from call import call
from diagrams import generateChart, generateTimeChart

app = FastAPI(title="Получение предложений действий от И")


def getModels():
    url = "https://gigachat.devices.sberbank.ru/api/v1/models"
    token = getToken()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers, verify=False)
    result = loads(response.text)
    return result


def getAnswer(messages: list[dict], temperature: float = 0.87) -> dict:
    """
    "messages": [
            {
                "role": "user",
                "content": "Когда уже ИИ захватит этот мир?"
            },
            {
                "role": "assistant",
                "content": "Пока что это не является неизбежным событием. Несмотря на то, что искусственный интеллект (ИИ) развивается быстрыми темпами и может выполнять сложные задачи все более эффективно, он по-прежнему ограничен в своих возможностях и не может заменить полностью человека во многих областях. Кроме того, существуют этические и правовые вопросы, связанные с использованием ИИ, которые необходимо учитывать при его разработке и внедрении."
            },
            {
                "role": "user",
                "content": "Думаешь, у нас еще есть шанс?"
            }
        ],

        temperature = number <float> [ 0 .. 2 ]
        По умолчанию: 0.87
        Температура выборки в диапазоне от ноля до двух. Чем выше значение, тем более случайным будет ответ модели.
    """

    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {getToken()}"
    }

    data = {
        "model": "GigaChat:latest",
        "messages": messages,
        "temperature": temperature
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    result = loads(response.text)
    return result


messages = [
    {
        "role": "user",
        "content": "чем fastapi лучше других?"
    }
]


@app.post("/sendMessage")
def get_message(messages: list[dict], temperature: float = 0.87):
    """"
        messages - массив сообщений, минимум одно сообщение должно быть.
        temperature - случайность выбора
    """
    return getAnswer(messages, temperature)


@app.post("/callAdmin")
def call_admin(phone_number: str):
    return call(phone_number)


@app.get("/generate_chart/{total_space}/{used_space}")
def generate_chart(total_space: float, used_space: float):
    chart_data = generateChart(total_space, used_space)
    return Response(content=chart_data, media_type="image/png")


@app.post("/generateTimeChart")
def generate_time_chart(data: dict):
    chart_data = generateTimeChart(data["data"])
    return Response(content=chart_data, media_type="image/png")