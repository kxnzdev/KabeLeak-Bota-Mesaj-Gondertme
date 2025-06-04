import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Eğer içerik okumak istiyorsan gerekli

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')

    channel_id = 1373419432340230244  # MESAJ GÖNDERİLECEK KANALIN ID'Sİ
    channel = bot.get_channel(channel_id)

    if channel:
        await channel.send("göndericeğiniz mesaj")
    else:
        print("Kanal bulunamadı.")

# TOKEN'INI BURAYA YAPIŞTIR
bot.run('botun tokenini yazın')