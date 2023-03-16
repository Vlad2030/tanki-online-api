import json
from typing import Any, AnyStr, Dict

import aiohttp


async def get(
        url: str,
        params: Dict[AnyStr],
        data: AnyStr = None,
        encoding: str = "UTF-8"
) -> Dict | AnyStr:
    """Get URL response

    Args:
        url (str): Your URL
        params (Dict[AnyStr]): Parameters
        data (AnyStr, optional): Data. Defaults to None.
        encoding (str, optional): Encoding. Defaults to "UTF-8".

    Returns:
        Dict | AnyStr: Text response
    """
    session = aiohttp.ClientSession()
    async with session.get(url=url, params=params) as response:
        return response.text(encoding=encoding)


def json_parse(data: Any) -> dict:
    """Parse JSON data

    Args:
        data (Any): Your json

    Returns:
        dict: return your json
    """

    return json.loads(data)
