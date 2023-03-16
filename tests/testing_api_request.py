import asyncio

from api.profile.stat import get_profile_stat


async def main() -> None:
    responce = await get_profile_stat(username="BabyLaFlare")
    print(responce)


asyncio.run(main=main())