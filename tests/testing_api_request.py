import asyncio

from api.profile.stat import async_get_profile, get_profile
from api.utils.json import parse


async def main() -> None:
    responce = await async_get_profile(username="BabyLaFlare")
    jsoned = parse(data=responce)
    print(jsoned)

if __name__ == "__main__":
    asyncio.run(main=main())

    response = get_profile(username="BabyLaFlare")
    print(response)