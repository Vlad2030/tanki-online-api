from json import loads
from typing import Any


def parse(data: Any) -> dict:
    """Parse JSON data

    Args:
        data (Any): Your json

    Returns:
        dict: return your json
    """

    return loads(data)
