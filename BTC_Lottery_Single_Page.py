import asyncio
import aiohttp  # pip install aiohttp aiodns
import time
from bs4 import BeautifulSoup
import urllib.request,requests,json
from random import randrange
i=0
async def get(
    session: aiohttp.ClientSession,
    addr: str,
    **kwargs
) -> dict:
    global i
    url = f"https://blockchain.info/address/{addr}?format=json"
    try:
        resp = await session.request('GET', url=url, **kwargs)
        data = await resp.json(content_type=None)
        bal=data['n_tx']
        print(i,"-   Transactions for " + addr + " : " + str(data['n_tx']))
        i+=1
        if bal > 0:
            loot = "Collision found at address: "+addr+"\nPage no. :"+str(rand)+"\n"
            print (loot)
            print ("Writing to loot.txt...")
            lootxt = open("loot.txt", 'a')
            lootxt.write(loot)
            lootxt.close()
        return data
    except asyncio.TimeoutError:
            pass
    except Exception as e:
            print("Error: "+repr(e))


async def main(arr, **kwargs):
    global i
    async with aiohttp.ClientSession() as session:
        tasks = []
        for a in arr:
            tasks.append(get(session=session, addr=a, **kwargs))
        htmls = await asyncio.gather(*tasks, return_exceptions=False)
        return htmls


if __name__ == '__main__':
    n=0
    arr = []
    while True:
        rand=input("Insert page number: \n")
        try:
            URL = 'https://lbc.cryptoguru.org/dio/'+str(rand)
            page = requests.get(URL)
            priv=[]
            pub=[]
            pub2=[]
            print("Page no. :",rand)
            print("\n\n--------------------------------------------\n\n")
            soup = BeautifulSoup(page.content, 'html.parser')
            for each_span in soup.findAll('span'):
                address=each_span.text
                row=address.split()
                if n%2==0:
                    priv.append(row[1])
                    pub.append(row[2])
                    pub2.append(row[3])
                n+=1
            for item in pub:
                arr.append(item)
            for item in pub2:
                arr.append(item)
        except Exception as e:
            print("Error: "+repr(e))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(arr))
        arr.clear()
        i=0