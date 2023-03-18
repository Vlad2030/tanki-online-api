import asyncio
import time

import api.online.test_server
import api.profile.stat
import api.utils.format
import api.utils.json


async def async_main() -> None:
    response = await api.online.test_server.async_get_current_online(format=True)
    print(response)

def main() -> None:
    response = api.online.test_server.get_current_online(format=True)
    print(response)

def loop_get_online() -> None:
    while True:
        request: dict = api.online.test_server.get_current_online(format=False)
        json: list = api.utils.json.parse(request)
        print(f' 1 TEST SERVER ONLINE:\t{json[0]["UserCount"]}\t\t2 TEST SERVER ONLINE:\t{json[1]["UserCount"]}', end="\r")
        time.sleep(0.01)

if __name__ == "__main__":
    # async     0.3s speed
    # sync      0.6s speed
    loop_get_online()