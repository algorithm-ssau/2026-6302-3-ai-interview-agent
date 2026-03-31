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