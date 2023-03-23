import os
import nextcord
from nextcord.ext import commands
import constants
from dotenv.main import load_dotenv

load_dotenv(override=True)


def get_prefix(client, message):
    """Gets prefix for the bot"""
    # Check if in new server or DM
    return constants.DEFAULT_BOT_PREFIX


def main():
    intents = nextcord.Intents.default()
    intents.members = True
    intents.message_content = True
    client = commands.Bot(
        command_prefix=get_prefix,
        intents=intents,
        help_command=None,
        case_insensitive=True,
    )

    # Get the modules of all cogs whose directory structure is modules/<module_name>/cog.py
    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            client.load_extension(f"modules.{folder}.cog")

    @client.event
    async def on_ready():
        """When the bot starts up"""
        await client.change_presence(
            activity=nextcord.Activity(
                type=nextcord.ActivityType.watching, name="you solve👀 | $help"
            )
        )
        for guild in client.guilds:
            print(
                f"{client.user.name} has connected to the following guild: "
                f"{guild.name} (id: {guild.id})"
            )
        # Populate default command list
        for command in client.commands:
            constants.DEFAULT_COMMANDS.append(command.qualified_name.lower())
            for alias in command.aliases:
                constants.DEFAULT_COMMANDS.append(alias.lower())

    @client.event
    async def on_guild_join(guild: nextcord.Guild):
        """When the bot joins a new guild, add it to the database for prefixes"""
        print(f"Joining {guild} -- Hi!")

    @client.event
    async def on_guild_remove(guild: nextcord.Guild):
        """When the bot leaves a guild, remove all database entries pertaining to that guild"""
        print(f"Leaving {guild} -- Bye bye!")

    @client.event
    async def on_message(message: nextcord.Message):
        # We only want to respond to user messages
        if message.is_system() or message.author.id == client.user.id:
            return

        command_prefix = get_prefix(client, message)

        if message.clean_content.startswith(command_prefix):
            # If the command is a default one, just run it.
            command_name = message.clean_content.split()[0][
                len(command_prefix) :
            ].lower()
            if command_name in constants.DEFAULT_COMMANDS:
                await client.process_commands(message)
            # Don't use custom commands for DMs also I think this fixes a bug which gets an error when someone
            # uses a command right as the box is starting up.

    client.run(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
    main()
