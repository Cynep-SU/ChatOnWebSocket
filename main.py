import asyncio
import os

import aiofiles as aiofiles
import websockets

TOKEN = 'asjkldkasjkldasjkldjaklsjkdaskljdkasjdklasjkldasjldjasldlasdjlasdjlasjldjasljdlasjdlaskdjasklgdfhkjgfhkvsdncvnsdjkfdhjksbvkdfjshfsdkfnjlsdhfjksdbkvsdjklsdnsjkcvnsdhjkvsdjklfnsdnkmbvhjknsdjkvnjksdnvhjksdbvsdnvj,sdbhjksdhfkjsdbfhsdhvjksdbvsdhfvjksdvbsdvjksdvdjksjwerfyhuiosdfhvukozdxjfosdhfuiowsenjklsddjaspifghaskdjoaihfoassduasoufhohsuofhuiosdhfuiosdhfljksdjl,asdhfoaifjilasjfioasjflasjxcjk,vnsdjkjfsdaiolfhsdjkh'

async def echo(websocket):
    async for message in websocket:
        # print(message)
        async with aiofiles.open('log.txt', 'r') as file_r:
            text = await file_r.read()
        if message == TOKEN:
            await websocket.send(text)
            continue

        async with aiofiles.open('log.txt', 'w') as file:
            await file.write(text)
            await file.write("\n")
            await file.write(message)

        await websocket.send('ok')


async def main():
    port = int(os.environ.get("PORT", 5000))
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    async with websockets.serve(echo, "", port):
        await stop  # run forever


asyncio.run(main())
