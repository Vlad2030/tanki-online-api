from typing import Dict, AnyStr

import api.utils.request
import api.utils.format
import api.utils.json
import config.routes

url_params: dict = {
        "v="
    }

async def async_get_current_online(format: bool = False) -> Dict[AnyStr, int]:
    responce: dict = await api.utils.request.async_get(
        url=config.routes.TEST_API_URL,
        params={"v": ""},
    )
    json: list = api.utils.json.parse(data=responce)
    formated: str = api.utils.format.online(data=json)

    if format:
        return formated

    return responce


def get_current_online(format: bool = False) -> Dict[AnyStr, int]:
    responce: dict = api.utils.request.get(
        url=config.routes.TEST_API_URL,
        params=url_params
    )
    json: list = api.utils.json.parse(data=responce)
    formated: str = api.utils.format.online(data=json)

    if not isinstance(format, bool):
        TypeError("Only bool arguments")

    if format:
        return formated

    return responce


    """
    Example JSON output
    [
        {
            "Release":"deploy5-pubto",
            "Domain":"public-deploy5.test-eu.tankionline.com",
            "Url":"https://public-deploy5.test-eu.tankionline.com/desktop/index.html?resources=../resources&config=https://c1.public-deploy5.test-eu.tankionline.com/config.xml",
            "UserCount":181
        },
        {
            "Release":"deploy8-pubto",
            "Domain":"public-deploy8.test-eu.tankionline.com",
            "Url":"https://public-deploy8.test-eu.tankionline.com/desktop/index.html?resources=../resources&config=https://c1.public-deploy8.test-eu.tankionline.com/config.xml",
            "UserCount":16
        }
    ]
    """
