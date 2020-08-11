import discord
from discord.ext import commands
from helpers import config, reddit, embeds, random_operations, fourchan, nekoimg
import os
import random
import sys, traceback



bot = commands.Bot(command_prefix='>')
config_path = os.path.abspath("config.json")
file_load = open(config_path, 'r').read()

session_config = config.Configuration(file_load)

initial_extensions= ['cogs.fun']
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


@bot.command()
async def ping(ctx):
    random_cheems = random_operations.get_cheems_phrase()
    await ctx.send(random_cheems)


@bot.command()
async def dogememe(ctx):
    reddit_post = reddit.RedditPost(session_config.reddit_client_id,
                                    session_config.reddit_client_secret, session_config.reddit_user_agent, session_config.reddit_user, session_config.reddit_password, "dogelore")
    embed_message = embeds.RedditEmbedMessage(discord.Color.orange(), reddit_post.post_title, reddit_post.post_image,
                                              reddit_post.post_subreddit, reddit_post.post_author, reddit_post.post_author_avatar, reddit_post.post_link).getEmbedMessage()
    await ctx.send(embed=embed_message)


@bot.command()
async def ask(ctx, *, question=None):
    if question == None:
        await ctx.send("I meed you to amsk somethimg")
    else:
        ask_answer = random_operations.get_8_ball()
        await ctx.send(f"{ctx.author.mention}, "+ask_answer)


@bot.command()
async def tech(ctx):
    target_board = 'g'
    fourchan_post = fourchan.FourChanImage(target_board)
    embed_message = embeds.FourChanEmbed(discord.Color.green(
    ), fourchan_post.topic, fourchan_post.image_url, target_board, fourchan_post.url).getEmbedMessage()
    await ctx.send(embed=embed_message)


@bot.command()
async def girlfriend(ctx):
    reddit_post = reddit.RedditPost(session_config.reddit_client_id,
                                    session_config.reddit_client_secret, session_config.reddit_user_agent, session_config.reddit_user, session_config.reddit_password, "gentlemanboners")
    await ctx.send(reddit_post.post_image)


@bot.command()
async def boyfriend(ctx):
    reddit_post = reddit.RedditPost(session_config.reddit_client_id,
                                    session_config.reddit_client_secret, session_config.reddit_user_agent, session_config.reddit_user, session_config.reddit_password, "ladyboners")
    await ctx.send(reddit_post.post_image)


# TODO: Here it should be r/femboy, however, we tried to fix it, and it refuses to work.
# it returns a none type, this ofc makes an error, this however should be look up on
# as many users have requested this feature to be r/femboy and not r/crossdressing
# wen eta femboy command :(
@bot.command()
async def femboy(ctx):
    reddit_post = reddit.RedditPost(session_config.reddit_client_id,
                                    session_config.reddit_client_secret, session_config.reddit_user_agent, session_config.reddit_user, session_config.reddit_password,
                                    "crossdressing")
    await ctx.send(reddit_post.post_image)


@bot.command()
async def lewdfemboy(ctx):
    if ctx.channel.is_nsfw():
        reddit_post = reddit.RedditPost(session_config.reddit_client_id,
                                        session_config.reddit_client_secret, session_config.reddit_user_agent, session_config.reddit_user, session_config.reddit_password,
                                        "femboys")
        await ctx.send(reddit_post.post_image)
    else:
        await ctx.send('Not infromt of the childmren.')


@bot.command()
async def neko(ctx):
    await ctx.send(nekoimg.get_neko_sfw())


@bot.command()
async def lewdneko(ctx):
    if ctx.channel.is_nsfw():
        await ctx.send(nekoimg.get_neko_nsfw())
    else:
        await ctx.send("Not infromt of the childmren.")


@bot.command()
async def redditmeme(ctx, *, subreddit=None):
    if subreddit == None:
        await ctx.send("Gimve me a sumbreddit")
    else:
        reddit_post = reddit.RedditPost(session_config.reddit_client_id,
                                        session_config.reddit_client_secret, session_config.reddit_user_agent, session_config.reddit_user, session_config.reddit_password,
                                        subreddit)
        if reddit_post.is_nsfw:
            await ctx.send("Not infromt of the childdrem")
            return
        embed_message = embeds.RedditEmbedMessage(discord.Color.orange(), reddit_post.post_title, reddit_post.post_image,
                                                  reddit_post.post_subreddit, reddit_post.post_author, reddit_post.post_author_avatar, reddit_post.post_link).getEmbedMessage()
        await ctx.send(embed=embed_message)


@bot.command()
async def owofy(ctx, *, text=None):
    if text == None:
        await ctx.send("Gimve me a memsage")
    else:
        await ctx.send(nekoimg.owo_text(text))


@bot.command()
async def cuddle(ctx, member: discord.User = None):
    if member == None:
        await ctx.send("Gimve me a user")
    else:
        neko_action = embeds.NekoEmbed(discord.Color.blurple(), nekoimg.NekoActions.neko_cuddle(
        ), ctx.author.name, str(member.name), 'cuddle').getEmbedMessage()
        await ctx.send(embed=neko_action)


@bot.command()
async def headpat(ctx, member: discord.User = None):
    if member == None:
        await ctx.send("Gimve me a user")
    else:
        neko_action = embeds.NekoEmbed(discord.Color.blurple(), nekoimg.NekoActions.neko_pat(
        ), ctx.author.name, str(member.name), 'pat').getEmbedMessage()
        await ctx.send(embed=neko_action)


@bot.command()
async def kiss(ctx, member: discord.User = None):
    if member == None:
        await ctx.send("Gimve me a user")
    else:
        neko_action = embeds.NekoEmbed(discord.Color.blurple(), nekoimg.NekoActions.neko_kiss(
        ), ctx.author.name, str(member.name), 'kiss').getEmbedMessage()
        await ctx.send(embed=neko_action)


@bot.command()
async def slap(ctx, member: discord.User = None):
    if member == None:
        await ctx.send("Gimve me a user")
    else:
        neko_action = embeds.NekoEmbed(discord.Color.blurple(), nekoimg.NekoActions.neko_slap(
        ), ctx.author.name, str(member.name), 'slap').getEmbedMessage()
        await ctx.send(embed=neko_action)


@bot.command()
async def ischad(ctx, member: discord.User = None):
    if member == None:
        await ctx.send("Gimve me a user")
    else:
        randomno = random.randint(0, 100)
        if randomno >= 50:
            await ctx.send(f"{member.mention} is a chad! <:chad:741875439940665365>")
        if randomno <= 49:
            await ctx.send(f"{member.mention} is a beta! <:virgin:741907301627199499>")


bot.run(session_config.discord_token)