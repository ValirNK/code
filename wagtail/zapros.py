import requests
import time
import datetime
import asyncio
import os

async def rm_files():
    resultdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'binance')
    resultdir = os.path.join(resultdir, 'result')
    for f in os.listdir(resultdir):
        os.remove(resultdir + '/' + f)

async def get_json():
    tm = tm = int(time.time())
    req = requests.post('http://127.0.0.1:8001', data={'unixtime':tm})
    if req.status_code != 200:
        print(req.status_code)
        return req.status_code
    return req.json()

async def start_requests():
    while True:
        try:
            response = await get_json()
            await asyncio.sleep(3)
            print(response)
            # await rm_files()
            continue
        except:
            print('except')
            continue


if __name__ == '__main__':
    asyncio.run(start_requests())