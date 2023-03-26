from typing import AnyStr, Dict

from api.utils.request import async_get, get
from config.languages import LANG
from config.routes import API_URL


async def async_get_profile(
        username: AnyStr,
        lang: str = "ru"
) -> Dict[AnyStr, int]:
    """Async get Profile Statistics

    Args:
        username (AnyStr): Username from tankionline.com
        lang (str, optional): Output language text. Defaults to "ru".

    Returns:
        Dict[AnyStr]: Output data of account
    """
    url: str = f"{API_URL}/eu/profile/"
    url_params: dict = {
        "user": username,
        "lang": lang,
    }

    if lang not in LANG:
        raise ValueError(
            "Language is not in the list of available languages. "
            "Try use default"
        )

    if not isinstance(username, str):
        raise TypeError("Username must be string")

    if not username:
        raise ValueError("Username should not be empty")

    profile_stat: dict = await async_get(url=url, params=url_params)

    return profile_stat


def get_profile(
        username: AnyStr,
        lang: str = "ru"
) -> Dict[AnyStr, int]:
    """Get Profile Statistics

    Args:
        username (AnyStr): Username from tankionline.com
        lang (str, optional): Output language text. Defaults to "ru".

    Returns:
        Dict[AnyStr]: Output data of account
    """
    url: str = f"{API_URL}/eu/profile/"
    url_params: dict = {
        "user": username,
        "lang": lang,
    }
    if lang not in LANG:
        raise ValueError(
            "Language is not in the list of available languages. "
            "Try use default"
        )

    if not isinstance(username, str):
        raise TypeError("Username must be string")

    if not username:
        raise ValueError("Username should not be empty")

    profile_stat: dict = get(url=url, params=url_params)

    return profile_stat
