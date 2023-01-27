async def join(client):
    try:
        await client.join_chat("HyperSupportQ")
        await client.join_chat("storyQi")
    except BaseException:
        pass
