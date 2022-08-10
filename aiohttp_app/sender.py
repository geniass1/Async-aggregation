import aiohttp
import asyncio

URLS = ['http://flask_2:5002/', 'http://flask_1:5001/']


async def send_image_request(url, img):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64, verify_ssl=False)) as session:
        async with session.post(url, data={"img": img}, ssl=False) as resp:
            return await resp.text()


async def send_request(request):
    data = await request.post()
    image = data['image'].file.read()
    tasks = [asyncio.ensure_future(
        send_image_request(url, image)) for url in URLS]

    torch_result = await asyncio.gather(*tasks)

    for name in torch_result:
        print(name)