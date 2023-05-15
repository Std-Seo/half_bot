import discord
from discord.ext import commands # 모듈 불러오기
import datetime, asyncio, random

token = 'YOUR TOKEN'
bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready(): # 봇이 준비되었을 때
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('잡생각'))
    print("봇 준비 완료!")
    print(bot.user)
    print("======================")

@bot.event
async def on_message(msg):
    if msg.author.bot: return None
    await bot.process_commands(msg)

@bot.command()
# 명령어 입력
async def 도움말(ctx):
    embed = discord.Embed(colour = discord.Colour.dark_gold(), title = "_하프 도움말_", description = "하프가 할 수 있는 일 목록이에요.")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/893782683321249793/896401992052797521/db3511e0c3a0b3c7.png")
    embed.add_field(name = '?내정보 :mens:', value = '명령어를 쓰신 분의 정보를 알려드려요!')
    embed.add_field(name = '?도움말 :question:', value = '하프가 할 수 있는 것들을 보여줘요!')
    embed.add_field(name = '?랜덤 :keycap_ten:', value = '1부터 10까지의 수에서 랜덤으로 하나를 출력해요!')
    embed.add_field(name = '10초 타이머 :clock1:', value = '10초를 센 뒤 불러드려요!')
    embed.add_field(name = '?하프정보 :heart:', value = '제 정보를 알려드릴게요!')
    await ctx.channel.send(embed = embed)

@bot.command()
async def 하프정보(ctx):
    embed = discord.Embed(colour = discord.Colour.blurple(), title='하프를 소개합니다!', description='Server_1 최강 귀요미 봇 하프')
    embed.add_field(name = '> 이름', value='(최강 귀요미)하프')
    embed.add_field(name = '> 할 수 있는 것', value='만능이라서 모두 가능!')
    await ctx.channel.send(embed = embed)

@bot.command()
async def 내정보(ctx):
    user = ctx.author
    date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
    await ctx.channel.send(f"{ctx.author}님의 정보!")
    await ctx.channel.send(f"{ctx.author.mention}님은 {date.year}년 {date.month}월 {date.day}일에 가입하셨어요!")
    await ctx.channel.send(f"{ctx.author.mention}님의 멋진 아바타 사진! {user.avatar_url}")

# 하프 정보
# @bot.command()
# async def 가입정보(ctx):
#     user = discord.abc.User()
#     date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
#     await ctx.channel.send(f"{user}님의 정보!")
#     await ctx.channel.send(f"{user}님은 {date.year}년 {date.month}월 {date.day}일에 가입하셨어요!")
#     await ctx.channel.send(f"{user}님의 멋진 아바타 사진! {user.avatar_url}")

@bot.command()
async def 랜덤(ctx):
    await ctx.channel.send(f"짜잔! {random.randint(1, 10)}!")
    
@bot.command()
async def 타이머(ctx):
    await ctx.channel.send(f"10초 세기 시작합니다!")
    await asyncio.sleep(10)
    await ctx.channel.send(f"{ctx.author.mention} 10초 땡~!")



bot.run(token)
