import asyncio
import os

import aioconsole
import websockets


async def check_console(ws):
    last_message = ''
    while True:
        await ws.send("asjkldkasjkldasjkldjaklsjkdaskljdkasjdklasjkldasjldjasldlasdjlasdjlasjldjasljdlasjdlaskdjasklgdfhkjgfhkvsdncvnsdjkfdhjksbvkdfjshfsdkfnjlsdhfjksdbkvsdjklsdnsjkcvnsdhjkvsdjklfnsdnkmbvhjknsdjkvnjksdnvhjksdbvsdnvj,sdbhjksdhfkjsdbfhsdhvjksdbvsdhfvjksdvbsdvjksdvdjksjwerfyhuiosdfhvukozdxjfosdhfuiowsenjklsddjaspifghaskdjoaihfoassduasoufhohsuofhuiosdhfuiosdhfljksdjl,asdhfoaifjilasjfioasjflasjxcjk,vnsdjkjfsdaiolfhsdjkh")
        message = await ws.recv()

        if last_message != message:
            last_message = message
            os.system("cls")
            print(message)
            print("[]:", end='')

        await asyncio.sleep(1)



async def main():
    name = input("Введите ваше имя: ")
    if name == '':
        raise Exception("Плохое имя")
    async with websockets.connect("ws://localhost:5000") as ws:
        asyncio.create_task(check_console(ws))
        while True:
            line = await aioconsole.ainput()
            await ws.send(name + ": " + line)
            await ws.recv()


asyncio.run(main())
