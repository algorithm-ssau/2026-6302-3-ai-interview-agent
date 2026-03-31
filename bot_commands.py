from aiogram.types import BotCommand

async def set_bot_commands(bot):
    """Устанавливает команды в меню бота"""
    commands = [
        BotCommand(command="start", description="🚀 Начать интервью"),
        BotCommand(command="help", description="📖 Инструкция и команды"),
        BotCommand(command="stats", description="📊 Моя статистика"),
    ]
    await bot.set_my_commands(commands)