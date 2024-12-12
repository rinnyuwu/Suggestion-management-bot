import disnake
from disnake.ext import commands
from config.config import Config
from database.database import Database

class Suggest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()

    @commands.slash_command(name="suggest", description="Submit a suggestion")
    async def suggest(self, inter: disnake.AppCmdInter, text: str):
        
        channel = self.bot.get_channel(Config.SUGGESTIONS_CHANNEL_ID)
        
        if not channel:
            await inter.response.send_message("Someone forgot to set up the bot configuration.", ephemeral=True)
            return
        
        embed = disnake.Embed(
            title=f"Suggestion #{self.get_new_suggestion_id()}",
            description=text,
            color=disnake.Color.blue(),
        )
        embed.set_footer(text=f"Submitted by {inter.user.name}", icon_url=inter.user.avatar.url)
        
        sent_message = await channel.send(embed=embed)
        
        self.db.add_suggestion(inter.user.id, sent_message.id)

        await inter.response.send_message(f"Your suggestion has been submitted successfully!", ephemeral=True)

    def get_new_suggestion_id(self):
        last_suggestion = self.db.get_last_suggestion_id()
        return last_suggestion + 1 if last_suggestion else 1

def setup(bot):
    bot.add_cog(Suggest(bot))