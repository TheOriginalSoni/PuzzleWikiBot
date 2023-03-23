import nextcord
import os
from nextcord.ext import commands
from emoji import UNICODE_EMOJI
from typing import Union
import constants
from utils import discord_utils, logging_utils, command_predicates


class MiscCog(commands.Cog, name="Misc"):
    """A collection of Misc useful/fun commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="about", aliases=["aboutthebot", "github"])
    async def about(self, ctx):
        """A quick primer about BBN and what it does

        Usage : `~about`
        """
        logging_utils.log_command("about", ctx.guild, ctx.channel, ctx.author)
        embed = discord_utils.create_embed()

        emoji = None
        owner = await self.bot.fetch_user(os.getenv("BOT_OWNER_DISCORD_ID"))

        embed.add_field(
            name=f"About Me!",
            value=f"Hello!\n"
            f"PuzzleWikiBot is a discord bot\n"
            f"To learn more about the bot or useful functions, use `{constants.DEFAULT_BOT_PREFIX}startup`\n"
            f"Any problems? Let {owner.mention} know.",
            inline=False,
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MiscCog(bot))
