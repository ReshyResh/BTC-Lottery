import asyncio
import aiohttp  # pip install aiohttp aiodns
import time
from bs4 import BeautifulSoup
import urllib.request,requests,json
from random import randrange
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 9000  # Set Duration To 1000 ms == 1 second
i=0
#api_key = "Tg Api Key here"
#chat_id = "Tg chat id here"
rand=randrange(904625697166532776746648320380374280100293470930272690489102837043110636675)
async def get(
    session: aiohttp.ClientSession,
    add: str,
    **kwargs
) -> dict:
    global i
    url = f"https://blockchain.coinmarketcap.com/api/address?address={add}&symbol=BTC&start=1&limit=10"
    try:
        resp = await session.request('GET', url=url, **kwargs)
        data = await resp.json(content_type=None)
        bal=data['transaction_count']
        print(i,"-   Transactions for " + add + " : " + str(data['transaction_count']))
        i+=1
        if bal > 0:
            loot = "Collision found at address: "+add+"\nPage no. :"+str(rand)+"\n"
            print (loot)
            print ("Writing to loot.txt...")
            lootxt = open("loot.txt", 'a')
            lootxt.write(loot)
            winsound.Beep(frequency, duration)
            lootxt.close()
            #s = "Collision found at address: "+add+"\nPage no. :"+str(rand)+"\n"
            #s.replace(" ", "%20")
            #urltg = "https://api.telegram.org/bot"+ api_key + "/sendMessage?chat_id=" + chat_id + "&text="
            #msg = urltg + s
            #ret = requests.get(msg)
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
            tasks.append(get(session=session, add=a, **kwargs))
        htmls = await asyncio.gather(*tasks, return_exceptions=False)
        return htmls


if __name__ == '__main__':
    n=0
    while True:
        arr = []
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
            rand+=1
        except Exception as e:
            print("Error: "+repr(e))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(arr))
