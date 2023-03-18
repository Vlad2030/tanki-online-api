from typing import Any, AnyStr, Dict

from aiohttp import ClientSession
from requests import Session


class Async:
    async def __init__(
            self: Any,
            url: str,
            params: Dict[str, int],
            encoding: str
    ) -> None:
        self.url: str = url
        self.params: Dict[str, int] = params
        self.encoding: str = encoding

    async def get(
            url: str,
            params: Dict[AnyStr, int],
            encoding: str = "UTF-8",
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
        async with ClientSession() as session:
            async with session.get(url=url, params=params) as response:
                return await response.text(encoding=encoding)


class Sync:
    def __init__(
            self: Any,
            url: str,
            params: Dict[str, int],
            encoding: str
    ) -> None:
        self.url: str = url
        self.params: Dict[str, int] = params
        self.encoding: str = encoding

    def get(
            url: str,
            params: Dict[AnyStr, int],
            encoding: str = "UTF-8",
    ) -> Dict | AnyStr:
        with Session() as session:
            with session.get(url=url, params=params) as response:
                return response.text
