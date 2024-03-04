import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    welcome_message = f"Welcome {member.mention} to the server."

    embed = discord.Embed(
        title="Welcome",
        description=welcome_message,
        color=discord.Colour.green()
    )

    embed.add_field(name="Rules", value="Remember to follow the rules.")
    embed.set_thumbnail(url=member.avatar_url)

    # ersetzt CHANNEL_ID zu deiner Eigenen Id
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(embed=embed)

# HIER DEIN TOKEN
bot.run('YOUR_BOT_TOKEN')
