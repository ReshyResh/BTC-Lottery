import asyncio
import aiohttp
import time
from bs4 import BeautifulSoup
import requests
from random import randrange

i = 0
rand = randrange(904625697166532776746648320380374280100293470930272690489102837043110636675)


async def get(
    session: aiohttp.ClientSession,
    address: str,

    **kwargs
) -> dict:
    global i
    url = f"https://explorer.digiassets.net/api/addr/{address}/balance"
    try:
        resp = await session.request('GET', url=url, **kwargs)
        data = await resp.json(content_type=None)
        bal = int(data)

        i += 1
        if bal > 0:
            loot = f"Collision found at address: {address}\nPage no. :{rand}\n"
            print(loot)
            print("Writing to loot.txt...")
            lootxt = open("loot.txt", 'a')
            lootxt.write(loot)
            lootxt.close()

        time.sleep(5)
        return data
    except asyncio.TimeoutError:
        pass
    except Exception as e:
        print("Error: " + repr(e))
        time.sleep(5)


async def main(addresses, **kwargs):
    global i
    async with aiohttp.ClientSession() as session:
        htmls = await asyncio.gather(*[get(session, address, **kwargs) for address in addresses])
        return htmls


if __name__ == '__main__':
    n = 0
    while True:
        addresses = []
        try:
            URL = f'https://lbc.cryptoguru.org/dio/{rand}'
            page = requests.get(URL)
            priv = []
            pub = []
            pub2 = []
            print(f"Page no. :{rand}")
            print("\n\n--------------------------------------------\n\n")
            soup = BeautifulSoup(page.content, 'html.parser')
            for each_span in soup.findAll('span'):
                address = each_span.text
                row = address.split()
                if n % 2 == 0:
                    priv.append(row[1])
                    pub.append(row[2])
                    pub2.append(row[3])
                n += 1
            for item in pub:
                addresses.append(item)
            for item in pub2:
                addresses.append(item)
            rand += 1
        except Exception as e:
            print("Error: " + repr(e))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(addresses))
