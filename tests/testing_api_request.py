import asyncio

import api.profile.stat
import api.aio.request


async def main() -> None:
    responce = await api.profile.stat.get_profile(username="BabyLaFlare")
    jsoned = api.aio.request.json_parse(data=responce)
    print(jsoned)


asyncio.run(main=main())