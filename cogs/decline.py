import disnake
from disnake.ext import commands
from config.config import Config
from database.database import Database

class Decline(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()

    @commands.slash_command(name="decline", description="Decline a suggestion")
    async def decline(self, inter: disnake.AppCmdInter, suggestion_id: int):

        if not any(role.id in Config.ADMIN_ROLES for role in inter.user.roles):
            await inter.response.send_message("You don't have permission to decline suggestions.", ephemeral=True)
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
        embed.title = f"Suggestion #{suggestion_id} Declined"
        embed.color = disnake.Color.red()
        
        await message.edit(embed=embed)

        self.db.update_status(suggestion_id, "declined")

        await inter.response.send_message(f"Suggestion #{suggestion_id} has been declined.", ephemeral=True)

def setup(bot):
    bot.add_cog(Decline(bot))