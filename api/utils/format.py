from typing import AnyStr, Dict, List


def player_stat(data: Dict[AnyStr, int]) -> AnyStr:
    responce:               list = []

    if not isinstance(data, Dict[AnyStr, int]):
        raise TypeError("Data argument need a dict type")

    if not data["responceType"] == "OK":
        return "get player stat error"

    dict_data: dict = data["responce"]

    name:                   str = dict_data["name"]
    has_premium:           bool = dict_data["hasPremium"]
    gear_score:             int = dict_data["gearScore"]

    rank:                   int = dict_data["rank"]
    rank_score:             int = dict_data["score"]
    score_base:             int = dict_data["scoreBase"]
    score_next:             int = dict_data["scoreNext"]

    kills:                  int = dict_data["kills"]
    death:                  int = dict_data["deaths"]

    caught_golds:           int = dict_data["caughtGolds"]
    earned_crystals:        int = dict_data["earnedCrystals"]

    drones_info:           list = drones(data=dict_data["dronesPlayed"])


def drones(data: Dict[AnyStr]) -> AnyStr:
    responce: list = []

    for drone in data:
        grade:              int = drone["grade"]
        id:                 int = drone["id"]
        image_url:          str = drone["imageUrl"]
        drone_name:         str = drone["name"]
        properties:         None
        score_earned:       int = drone["scoreEarned"]
        time_played:        int = drone["timePlayed"]

        responce.append(
            f"Grade:\t{grade}"
            f"ID:\t{id}"
            f"Image URL:\t{image_url}"
            f"Drone name:\t{drone_name}"
            f"Properties:\t{properties}"
            f"Score earned:\t{score_earned}"
            f"Time played:\t{time_played}"
        )

    return "\n".join(responce)


def online(data: List[AnyStr], debug: bool = False) -> AnyStr:
    response: list = []

    if not isinstance(data, list):
        raise TypeError("Data argument need a dict type")

    for server in data:
        release:            str = server["Release"]
        domain:             str = server["Domain"]
        url:                str = server["Url"]
        usercount:          str = server["UserCount"]

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


def ranks(rank: int) -> str:
    return