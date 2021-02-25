import discord
import requests
channel_id = 780184205404405862

bot = discord.Client()

@bot.event
async def on_message(message):
	if message.content == "give me image nasachan uwu":
		req = requests.get("https://api.nasa.gov/planetary/apod?api_key=Nq9M6UvRIxpwIizuBDT5dUT4CtAKMF0aDwqu4PZ1&count=1")
		embed = discord.Embed(title="Random NASA Image Of the Day", url=req.json()[0]['hdurl'], description=req.json()[0]['explanation'], color=discord.Color.blue())
		embed.set_thumbnail(url=req.json()[0]['url'])
		await message.channel.send(embed=embed) 

@bot.event
async def on_ready():
	print("Bot running")
	global channel
	channel = bot.get_channel(channel_id)
	await channel.send("Test")

bot.run("ODE0MzM5NzY1Njg3NDE4OTQy.YDcbAQ.nsRSJBc5QvaImWn_xQlmrDaONhU")