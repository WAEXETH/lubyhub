
import discord
from discord.ext import commands

TOKEN = "MTUyMTgxMDI4MDgwMjE2MDc2MQ.Gh677r.lT8bhU6OFcC0LxR_QfANezuiN4sZSvzMBn_FyA"
ALLOWED_CHANNEL = 1384468170433101927


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="!", intents=intents)

# รายการ Scripts
SCRIPTS = {
    "Sakura Stand": """if not game:IsLoaded() then
    repeat
        game.Loaded:Wait()
    until game:IsLoaded()
end

loadstring(game:HttpGet("https://raw.githubusercontent.com/WAEXETH/RubyHub.luau/refs/heads/main/SakuraStand.lua"))()
""",

    "Rogue Piece": """if not game:IsLoaded() then
    repeat
        game.Loaded:Wait()
    until game:IsLoaded()
end

loadstring(game:HttpGet("https://raw.githubusercontent.com/WAEXETH/RubyHub.luau/refs/heads/main/RoguePiece.lua"))()
""",

    "Rider World": """if not game:IsLoaded() then
    repeat
        game.Loaded:Wait()
    until game:IsLoaded()
end

loadstring(game:HttpGet("https://raw.githubusercontent.com/WAEXETH/RubyHub.luau/refs/heads/main/RiderWorld.lua"))()
""",

    "AUT": """if not game:IsLoaded() then
    repeat
        game.Loaded:Wait()
    until game:IsLoaded()
end

loadstring(game:HttpGet("https://raw.githubusercontent.com/WAEXETH/RubyHub.luau/refs/heads/main/AUT.lua"))()
""",

    "Last Run": """loadstring(game:HttpGet("https://raw.githubusercontent.com/WAEXETH/RubyHub.luau/refs/heads/main/LastRun.lua"))()
""",

    "Feed Your Teto": """loadstring(game:HttpGet("https://raw.githubusercontent.com/WAEXETH/RubyHub.luau/refs/heads/main/FeedYourTeto.lua"))()
""",

    "MTC": """loadstring(game:HttpGet("https://raw.githubusercontent.com/WAEXETH/RubyHub.luau/refs/heads/main/MTC.lua"))()
""",

    "CTS": """loadstring(game:HttpGet("https://raw.githubusercontent.com/WAEXETH/RubyHub.luau/refs/heads/main/ESPCTS.lua"))()
"""
}


class ScriptSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label=name, value=name)
            for name in SCRIPTS.keys()
        ]

        super().__init__(
            placeholder="เลือกเกม",
            options=options,
            custom_id="script_select"
        )

    async def callback(self, interaction: discord.Interaction):
        script = SCRIPTS.get(self.values[0], "ไม่พบสคริปต์")
        
        embed = discord.Embed(
            title=f"📜 {self.values[0]}",
            description=f"```lua\n{script}\n```",
            color=0x00ff00
        )
        embed.set_footer(text="คัดลอกโค้ดไปใช้ใน")

        await interaction.response.send_message(embed=embed, ephemeral=True)


class ScriptView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ScriptSelect())

# คลาสสำหรับปุ่มหลัก
class ButtonView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="📜 ɢᴇᴛ-ꜱᴄʀɪᴘᴛ",
        style=discord.ButtonStyle.green,
        custom_id="get_script"
    )
    async def get_script(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        embed = discord.Embed(
            title="เลือกเกม",
            description="เลือกเกมที่ต้องการจะเล่น",
            color=0x3498db
        )
        await interaction.response.send_message(embed=embed, view=ScriptView(), ephemeral=True)


@bot.event
async def on_ready():
    
    bot.add_view(ButtonView())
    bot.add_view(ScriptView())
    print(f"✅ Bot พร้อมทำงานแล้ว! Login as: {bot.user}")
    print(f"📊 จำนวนเซิร์ฟเวอร์: {len(bot.guilds)}")
    print(f"🎮 สคริปต์ทั้งหมด: {len(SCRIPTS)} เกม")


@bot.command()
async def panel(ctx):
    
    if ctx.guild is None:
        await ctx.reply("❌ ไม่สามารถใช้คำสั่งนี้ใน DM ได้", mention_author=False, delete_after=5)
        return

    
    if ctx.channel.id != ALLOWED_CHANNEL:
        await ctx.reply(
            f"❌ ใช้คำสั่งนี้ได้เฉพาะห้อง <#{ALLOWED_CHANNEL}>",
            mention_author=False,
            delete_after=5
        )
        return

    embed = discord.Embed(
        title="Ruby Hub Script",
        description="📜ɢᴇᴛ-ꜱᴄʀɪᴘᴛ",
        color=0xff69b4
    )

    await ctx.send(embed=embed, view=ButtonView())


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)


if __name__ == "__main__":
    if TOKEN == "":
        print("⚠️ กรุณาใส่ Token ในไฟล์")
    else:
        try:
            bot.run(TOKEN)
        except discord.LoginFailure:
            print("❌ Token ไม่ถูกต้อง กรุณาตรวจสอบ")
        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาด: {e}")