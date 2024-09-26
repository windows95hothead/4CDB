import discord
from discord.ext import commands
import COM


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir bilgisayar tanıtım botuyum!')

@bot.command()
async def ne_yapacağız(ctx):
    await ctx.send("rastgele bir bilgisayar fotoğrafı göndereceksin, biz senin fotoğrafını yorumlayacağız(SADECE ESKİ BİLGİSAYAR)")

@bot.command()
async def ing(ctx):
    if ctx.message.attachments:
        for pic in ctx.message.attachments:
            await pic.save(f"resimler/{pic.filename}")
            sınıf,score = COM.comp(f"resimler/{pic.filename}")
            if sınıf == "macintosh\n":
                await ctx.send("Macintosh, kısaca \"Mac\" olarak da bilinir, Apple tarafından geliştirilen bir kişisel bilgisayar markasıdır. İlk Macintosh bilgisayarı 24 Ocak 1984 tarihinde piyasaya sürülmüştür. Bilgisayar dünyasında devrim yaratan Macintosh, grafiksel kullanıcı arayüzü (GUI) ve fare kullanımını yaygınlaştırmasıyla tanınır.")
            elif sınıf == "IBM\n":
                await ctx.send("IBM PC, International Business Machines Corporation (IBM) tarafından geliştirilen ve 12 Ağustos 1981'de piyasaya sürülen ilk kişisel bilgisayarlardan biridir. IBM PC (Model 5150), kişisel bilgisayarların yaygınlaşmasında büyük bir dönüm noktası olarak kabul edilir ve \"PC\" terimi, bu modelin başarısı sayesinde yaygın bir şekilde kullanılmaya başlamıştır.")
            elif sınıf == "PET\n":
                await ctx.send("Commodore PET (Personal Electronic Transactor), 1977'de Commodore International tarafından geliştirilen ve piyasaya sürülen ilk kişisel bilgisayarlardan biridir. PET, özellikle ev ve eğitim kullanıcıları için tasarlanmış, ticari olarak başarılı olan ilk kişisel bilgisayar modellerinden biridir.")
            elif sınıf == "toshiba T1910cs\n":
                await ctx.send("Toshiba T1910CS, 1990'ların başında Toshiba tarafından üretilen bir dizüstü bilgisayar modelidir. Bu bilgisayar, o dönemin taşınabilir bilgisayar teknolojisini temsil eden bir modeldir ve iş dünyasında sıkça kullanılmıştır. Toshiba, 1980'lerin sonu ve 1990'ların başında dizüstü bilgisayar pazarının önde gelen üreticilerinden biri olmuştur.")
            else:
                await ctx.send("ERROR ALINDI:developer hatası:(")
    else:
        await ctx.send("ERROR ALINDI:resim yok:(")


bot.run("")