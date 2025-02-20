if you wish to run this with your own bot, remove in line 13-14

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

replace TOKEN in very last line which is bot.run(TOKEN) with your discord app's own token
