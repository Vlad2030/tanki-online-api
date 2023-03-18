import asyncio

import api.online.test_server
import api.profile.stat
import api.utils.format
import api.utils.json


async def main() -> None:
    response = await api.online.test_server.async_get_current_online(format=True)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())

    response = api.online.test_server.get_current_online(format=True)
    print(response)