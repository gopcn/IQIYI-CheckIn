import json
import requests
from fake_useragent import UserAgent

URL = "https://glados.rocks/api/user/checkin"
URL2 = "https://glados.rocks/api/user/status"
REFERER = 'https://glados.rocks/console/checkin'
ORIGIN = "https://glados.rocks"
UA = UserAgent()

def CheckIn(cookie):
    useragent = get_random_user_agent()
    payload = {
        'token': 'glados.one'
    }
    headers = {
        'cookie': cookie,
        'referer': REFERER,
        'origin': ORIGIN,
        'user-agent': useragent,
        'content-type': 'application/json;charset=UTF-8'
    }

    checkin = requests.post(URL, headers=headers, json=payload)
    state = requests.get(URL2, headers=headers)

    mess = checkin.json()['message']
    time = state.json()['data']['leftDays']
    days = time.split('.')[0]
    msg = f'checkin: {checkin.status_code} | state: {state.status_code}\n{mess}\n剩余天数：{days}天'

    checkin.close()
    state.close()
    return f'{mess}，剩余{days}天', msg

def get_random_user_agent():
    random_user_agent = UA.random
    return random_user_agent