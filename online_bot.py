# import discord, os, asyncio, datetime, requests

# from discord.ext import tasks, commands
import discord
from discord.ext import commands, tasks

TOKEN = 'OTE1NTExNjgxNjE3MTA5MDQy.Ya8MKA.6bWryaYoia44JGZoJi7_S102hbk'
client = discord.Client()

# 915534732761120819

@client.event
async def test():
    #if user is == everyone
    how_channel = client.get_channel(int(915534732761120819))
    print("how_channel => ", how_channel)

    myEmbed = discord.Embed (
        title = "Title",
        description = "This is the description",
        colour = discord.Color.blue()
    )

    myEmbed.set_footer(text="This is the footer")
    myEmbed.set_image(url="https://cdn.icon-icons.com/icons2/2619/PNG/512/among_us_discord_icon_156922.png")
    myEmbed.set_thumbnail(url="https://cdn.icon-icons.com/icons2/2619/PNG/512/among_us_discord_icon_156922.png")
    myEmbed.set_author(name="Author name", icon_url="https://cdn.icon-icons.com/icons2/2619/PNG/512/among_us_discord_icon_156922.png")
    myEmbed.add_field(name="**Current Price**", value="$200", inline=True)
    myEmbed.add_field(name="Resell Price", value="$500", inline=True)
    myEmbed.add_field(name="Profitt", value="$300", inline=True)
    myEmbed.add_field(name="Url link:", value="**[CLICK ME](https://google.com)**", inline=True)
    myEmbed.add_field(name="Useful link:", value="**[Ebay](https://google.com) | [Cragslist](https://google.com)**", inline=True)
    myEmbed.add_field(name="Checkout link:", value="**[Checkout](https://google.com)**", inline=True)

    await how_channel.send(embed=myEmbed)
    # await message.channel.send(embed=myEmbed)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}! {client.user.display_name} - {client.user.friends} - {client.user.avatar_url}")
    # test()

# client.run(TOKEN, bot=False)

if __name__ == "__main__":
    print("*** Discord Bot Startted ***")
    client.run(TOKEN, bot=False)