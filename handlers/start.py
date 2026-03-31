from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards.level_keyboard import level_keyboard
from states.interview_states import InterviewState

router = Router()

@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await state.set_state(InterviewState.choosing_level)

    await message.answer(
        "Привет! Я AI-интервьюер 🚀\nВыбери уровень:",
        reply_markup=level_keyboard()
    )

@router.message(Command("help"))
async def help_command(message: Message):
    """Отправляет инструкцию по использованию бота"""
    
    help_text = """
🤖 *AI-Интервьюер — инструкция*

*Как пользоваться:*
1️⃣ Выберите уровень сложности: Junior / Middle / Senior
2️⃣ Отвечайте на вопросы голосом
3️⃣ После ответа получите оценку от 0 до 10 и обратную связь
4️⃣ Используйте кнопки управления:
   • ⏭ *Пропустить* — перейти к следующему вопросу
   • ❌ *Завершить* — завершить интервью досрочно

*Доступные команды:*
/start — начать новое интервью
/help — показать эту инструкцию
/stats — посмотреть статистику прошлых интервью

*Советы:*
• Отвечайте развернуто, это повышает оценку
• Голосовые сообщения автоматически расшифровываются
• Результаты сохраняются в вашу статистику

Удачи! 🚀
"""
    
    await message.answer(
        help_text,
        parse_mode="Markdown"
    )