import disnake
from disnake.ext import commands
from config.config import Config
from database.database import Database

class Accept(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()

    @commands.slash_command(name="accept", description="Accept a suggestion")
    async def accept(self, inter: disnake.AppCmdInter, suggestion_id: int):

        if not any(role.id in Config.ADMIN_ROLES for role in inter.user.roles):
            await inter.response.send_message("You don't have permission to accept suggestions.", ephemeral=True)
            return
        
        suggestion = self.db.get_suggestion(suggestion_id)
        
        if not suggestion:
            await inter.response.send_message("Suggestion not found.", ephemeral=True)
            return
        
        message_id = suggestion[2]
        
        channel = self.bot.get_channel(Config.SUGGESTIONS_CHANNEL_ID)
        
        try:
            message = await channel.fetch_message(message_id)
        except disnake.NotFound:
            await inter.response.send_message("Message not found.", ephemeral=True)
            return

        embed = message.embeds[0]
        embed.title = f"Suggestion #{suggestion_id} Approved"
        embed.color = disnake.Color.green()
        
        await message.edit(embed=embed)

        self.db.update_status(suggestion_id, "approved")

        await inter.response.send_message(f"Suggestion #{suggestion_id} has been accepted!", ephemeral=True)

def setup(bot):
    bot.add_cog(Accept(bot))