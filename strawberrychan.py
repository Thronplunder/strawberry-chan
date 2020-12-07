import discord
token = open('token.txt', 'r').read()

print(token)

strawberrychan = discord.Client()


@strawberrychan.event
async def on_ready():
    print("logged in as {0.user}", strawberrychan)


@strawberrychan.event
async def on_message(message):
    if message.author == strawberrychan.user:
        return
    else:
        print("{0.author} send the following: {0.content}", message)

strawberrychan.run(token)
