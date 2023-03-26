from typing import Any, AnyStr, Dict

from aiohttp import ClientSession, http_exceptions
from requests import Session, exceptions


async def async_get(
        url: str,
        params: Dict[AnyStr, int],
        encoding: str = "UTF-8",
) -> Dict | AnyStr:
    """Get async URL response

    Args:
        url (str): Your URL
        params (Dict[AnyStr]): Parameters
        data (AnyStr, optional): Data. Defaults to None.
        encoding (str, optional): Encoding. Defaults to "UTF-8".

    Returns:
        Dict | AnyStr: Text response
    """
    async with ClientSession() as session:
        async with session.get(url=url, params=params) as response:
            if not response.status == 200:
                return http_exceptions.HttpBadRequest(
                    message="Request Failed"
                )
            
            return await response.text(encoding=encoding)


def get(
        url: str,
        params: Dict[AnyStr, int],
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
    with Session() as session:
        with session.get(url=url, params=params) as response:
            if not response == 200:
                exceptions.RequestException("Request Failed")

            return response.text
