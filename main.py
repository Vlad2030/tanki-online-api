import asyncio
import time

import api.online.test_server
import api.profile.stat
import api.utils.format
import api.utils.json


async def async_main() -> None:
    response = await api.online.test_server.async_get_current_online(format=True)
    print(response)

def main() -> None:
    response = api.online.test_server.get_current_online(format=True)
    print(response)


if __name__ == "__main__":
    # async     0.3s speed
    # sync      0.6s speed
    start1: float = time.perf_counter()
    asyncio.run(async_main())
    end1: float = time.perf_counter() - start1
    start2: float = time.perf_counter()
    main()
    end2: float = time.perf_counter() - start2
    print(
        f"Async {end1:.3} sec\n"
        f"Sync {end2:.3} sec\n"
        f"Async faster than {end2/end1:.3} times"
    )