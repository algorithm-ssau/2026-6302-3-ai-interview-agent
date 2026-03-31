import asyncio
from aiogram import Bot, Dispatcher

from config.settings import BOT_TOKEN
from handlers import start, interview
from bot_commands import set_bot_commands

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(interview.router)

async def main():

    await set_bot_commands(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())