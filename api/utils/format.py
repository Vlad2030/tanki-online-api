from typing import AnyStr, Dict, List


def player_stat(data: Dict[AnyStr, int]) -> AnyStr:
    if not isinstance(data, Dict[AnyStr, int]):
        raise TypeError("Data argument need a dict type")


def online(data: List[AnyStr], debug: bool = False) -> AnyStr:
    response: list = []

    if not isinstance(data, list):
        raise TypeError("Data argument need a dict type")

    for server in data:
        release: str = server["Release"]
        domain: str = server["Domain"]
        url: str = server["Url"]
        usercount: str = server["UserCount"]
        response.append(
                f"Release:\t{release}\n"
                f"Server Domain:\t{domain}\n"
                f"XML Url:\t{url}\n"
                f"UserCount:\t{usercount}\n"
                f"All response:\t{server}\n"
            )

        if debug:
            print(response)

    return '\n'.join(response)
