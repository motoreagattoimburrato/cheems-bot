from discord.ext import commands
from cheemsbot.helpers import reddit, config, nekoimg, random_operations
import os

bot = commands.Bot(command_prefix='>')
config_path = os.path.abspath("config.json")
file_load = open(config_path, 'r').read()

session_config = config.Configuration(file_load)


class FunWithCheemsCog(commands.Cog, name="Fun with cheemsburger"):
    @commands.command(name='ask', aliases=['8b'])
    async def ask(self, ctx, *, question=None):
        if question == None:
            await ctx.send("I meed you to amsk somethimg")
        else:
            ask_answer = random_operations.get_8_ball()
        await ctx.send(f"{ctx.author.mention}, "+ask_answer)

    def __init__(self, bot, configuration=None):
        self.bot = bot
        self.session_config = configuration

    @commands.command(name='gf')
    async def girlfriend(self, ctx):
        reddit_post = reddit.RedditPost(self.session_config.reddit_client_id,
                                        self.session_config.reddit_client_secret, self.session_config.reddit_user_agent, self.session_config.reddit_user, self.session_config.reddit_password, "gentlemanboners")
        await ctx.send(reddit_post.post_image)

    @commands.command(name='bf')
    async def boyfriend(self, ctx):
        reddit_post = reddit.RedditPost(self.session_config.reddit_client_id,
                                        self.session_config.reddit_client_secret, self.session_config.reddit_user_agent, self.session_config.reddit_user, self.session_config.reddit_password, "ladyboners")
        await ctx.send(reddit_post.post_image)

    # TODO: Here it should be r/femboy, however, we tried to fix it, and it refuses to work.
    # it returns a none type, this ofc makes an error, this however should be look up on
    # as many users have requested this feature to be r/femboy and not r/crossdressing
    # wen eta femboy command :(

    @commands.command(name='femboy')
    async def femboy(self, ctx):
        reddit_post = reddit.RedditPost(self.session_config.reddit_client_id,
                                        self.session_config.reddit_client_secret, self.session_config.reddit_user_agent, self.session_config.reddit_user, self.session_config.reddit_password,
                                        "crossdressing")
        await ctx.send(reddit_post.post_image)

    @commands.command(name='neko')
    async def neko(self, ctx):
        self.neko_img = nekoimg.get_neko_sfw()
        await ctx.send(self.neko_img)

    @commands.command(name='owofy')
    async def owofy(self, ctx, *, our_input=None):
        if our_input == None:
            await ctx.send("Gimve me a memsage")
        else:
            self.owofied_input = nekoimg.owo_text(our_input)
            await ctx.send(self.owofied_input)


def setup(bot):
    bot.add_cog(FunWithCheemsCog(bot, session_config))
