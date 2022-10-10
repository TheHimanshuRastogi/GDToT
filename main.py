import helper, traceback
from pyrogram import Client, filters

bot = Client("Bot",
   api_id=11781837,
   api_hash="4e4135898bbc89c27c656aa4aeed6021",
   bot_token="5753964641:AAHhDHJJpPf5RE_GNT09GiDwx8YqSkjWNk0"
  )

@bot.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply("Hey, I'm Alive.") 
    
@bot.on_message(filters.private)
async def GDToT(bot, message):
    try:
        if not message.text.startswith('https://drive.google.com/uc?id='):
            return
        reply = await message.reply('Processing...')
        link = await helper.getGDToT(helper.getProperLink(message.text))
        await message.reply(link)
        await reply.delete()
    except Exception as e:
        await message.reply(f"**Traceback Info:**\n`{traceback.format_exc() }`\n**Error Text:**\n`{e}`")
        
print('\n\nBot Started Successfully.\n\n')
bot.run()
